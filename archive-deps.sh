#!/bin/bash
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

# Builds an artifact that can be used in offline deployment of the application.

set -e
VENDOR=vendor/

# prepare dependencies
if [ -d $VENDOR ]; then
    rm -rf $VENDOR
fi
mkdir $VENDOR
pip install --no-cache-dir --exists-action=w --download $VENDOR -r requirements-normal.txt
pip install --no-cache-dir --download $VENDOR -r requirements-native.txt --no-use-wheel

# prepare build manifest
echo "commit_sha=$(git rev-parse HEAD)" > build_info.ini

# assemble the artifact
VERSION=$(grep current_version .bumpversion.cfg | cut -d " " -f 3)
FILE=data-catalog-deps-$VERSION.zip
zip -rj $FILE requirements.txt build_info.ini $VENDOR/*

echo "Next step: upload $FILE to a server, from which it could be downloaded by CI pipeline."
