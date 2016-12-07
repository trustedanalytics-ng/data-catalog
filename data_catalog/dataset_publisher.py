import requests
import flask

from elasticsearch.exceptions import ConnectionError, NotFoundError
from data_catalog.bases import DataCatalogResource, DataCatalogModel


class TableResource(DataCatalogResource):

    def __init__(self):
        super(TableResource, self).__init__()
        self._publish = DatasetPublisher()

    def post(self, entry_id):
        token = flask.request.headers.get('Authorization')
        return self._publish(entry_id, token)


class DatasetPublisher(DataCatalogModel):

    def __call__(self, entry_id, token):
        try:
            # TODO: validate response
            dataset = self._elastic_search.get(
                index=self._config.elastic.elastic_index,
                doc_type=self._config.elastic.elastic_metadata_type,
                id=entry_id)

            publish_url = self._config.services_url.dataset_publisher_url
            return self._post(publish_url, token, dataset['_source'])
        except NotFoundError:
            self._log.exception('Data set with the given ID not found.')
            return None, 404
        except ConnectionError:
            self._log.exception('No connection to the index.')
            return None, 500

    def _post(self, url, token, data=None):
        self._log.debug('Posting %s to: %s', data, url)
        response = requests.post(url,
                                   headers={'Authorization': token},
                                   json=data)
        if response.status_code == 201:
            return response.json()
        else:
            self._log.exception('Failed to publish dataset.')
            return None, 500
