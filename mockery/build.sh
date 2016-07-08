#!/bin/bash

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

MAVEN_REPO=http://nexus.sclab.intel.com:8080/content/groups/public
REPOSITORY=${1:-tap/data-catalog-mockery}
WIREMOCK_VERSION=2.1.0-beta
CURRENT_DIR=$(dirname $(readlink -f ${BASH_SOURCE[0]}))

pushd $(pwd)
cd $CURRENT_DIR

wget -q ${MAVEN_REPO}/com/github/tomakehurst/wiremock-standalone/${WIREMOCK_VERSION}/wiremock-standalone-${WIREMOCK_VERSION}.jar

docker build -t $REPOSITORY .
BUILD_RET=$?

rm wiremock-standalone-${WIREMOCK_VERSION}.jar

popd

exit $BUILD_RET
