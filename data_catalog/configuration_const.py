#
# Copyright (c) 2015 Intel Corporation
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

"""
Configuration values that change very seldom.
"""

METADATA_MAPPING = {
    '_all': {
        'enabled': False
    },
    'properties': {
        'title': {
            'type': 'string',
            'analyzer': 'autocomplete',
            'search_analyzer': 'standard',
            'fields': {
                'english': {
                    'type': 'string',
                    'analyzer': 'english'
                }
            },
        },
        'dataSample': {
            'type': 'string'
        },
        'format': {
            'type': 'string'
        },
        'category': {
            'type': 'string'
        },
        'size': {
            'type': 'long'
        },
        'recordCount': {
            'type': 'long'
        },
        'sourceUri': {
            'type': 'string',
            'analyzer': 'uri_analyzer'
        },
        'targetUri': {
            'type': 'string'
        },
        'storeType': {
            'type': 'string'
        },
        'creationTime': {
            'type': 'date'
        },
        'orgUUID': {
            'type': 'string',
            'index': 'not_analyzed'
        },
        'isPublic': {
            'type': 'boolean'
        }
    }
}

METADATA_SETTINGS = {
    'analysis': {
        'filter': {
            'uri_stop_filter': {
                'type': 'stop',
                'stopwords': ['http', 'https', 'ftp', 'www', 'com']
            },
            'autocomplete_filter': {
                'type': 'edge_ngram',
                'min_gram': 2,
                'max_gram': 16
            },
            'word_split_filter': {
                'type': 'word_delimiter',
                'generate_word_parts': True,
                'preserve_original': True
            }
        },
        'analyzer': {
            'uri_analyzer': {
                'type': 'custom',
                'tokenizer': 'lowercase',
                'filter': 'uri_stop_filter'
            },
            'autocomplete': {
                'type': 'custom',
                'tokenizer': 'standard',
                'filter': [
                    'lowercase',
                    'word_split_filter',
                    'autocomplete_filter'
                ]
            }
        }
    }
}
