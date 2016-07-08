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
FROM tapimages.us.enableiot.com:8080/tap-base-java:java8-jessie

ENV WIREMOCK_VERSION 2.1.0-beta

COPY wiremock-standalone-$WIREMOCK_VERSION.jar /home/wiremock/
COPY __files  /home/wiremock/__files
COPY mappings /home/wiremock/mappings

WORKDIR /home/wiremock

EXPOSE 8080 8081

CMD java -jar wiremock-standalone-$WIREMOCK_VERSION.jar $WIREMOCK_ARGS
