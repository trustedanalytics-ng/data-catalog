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


from data_catalog.org_id_decoder import OrgIdDecoder
from tests.base_test import DataCatalogTestCase
from hamcrest import *


class OrgIdDecoderTests(DataCatalogTestCase):

    def test_decode(self):
        org_uuid = "64656661-756c-7470-0000-000000000000"
        org_id = "defaultp"

        decoded = OrgIdDecoder.decode(org_uuid)

        assert_that(decoded, equal_to(org_id))
