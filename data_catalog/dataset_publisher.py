#
# Copyright (c) 2016 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import requests
import flask

from elasticsearch.exceptions import ConnectionError, NotFoundError
from data_catalog.bases import DataCatalogResource, DataCatalogModel
from data_catalog.metadata_entry import ORG_UUID_FIELD
from data_catalog.org_id_decoder import OrgIdDecoder


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
            result = self._elastic_search.get(
                index=self._config.elastic.elastic_index,
                doc_type=self._config.elastic.elastic_metadata_type,
                id=entry_id)

            dataset = result['_source']
            dataset[ORG_UUID_FIELD] = OrgIdDecoder.decode(dataset[ORG_UUID_FIELD])
            publish_url = self._config.services_url.dataset_publisher_url
            return self._post(publish_url, token, dataset)
        except NotFoundError:
            self._log.exception('Data set with the given ID not found.')
            return None, 404
        except ConnectionError:
            self._log.exception('No connection to the index.')
            return None, 500

    def _post(self, url, token, data=None):
        self._log.debug('Posting %s to: %s', data, url)
        response = requests.post(url, headers={'Authorization': token}, json=data)
        if response.status_code == 201:
            return response.json()
        else:
            self._log.exception('Failed to publish dataset.')
            return None, 500
