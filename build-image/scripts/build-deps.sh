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

SCRIPTS_DIR="/usr/local/bin"

# Directory with packages to be installed 
SRC_DIR=/src
# Target directory
BUILD_DIR=/build

# Install dependencies, so that they were available for 'cryptograpy' package that
# needs cffi and other libraries during setup.
pip install --no-cache -r $SRC_DIR/requirements.txt --no-index --find-links file:$SRC_DIR

# Install deps into an isolated directory, so that they could be easily grabbed and packed into 
# Docker image.
pip install --no-cache -r $SRC_DIR/requirements.txt -t $BUILD_DIR/packages --no-index --find-links file:$SRC_DIR


# Copy scripts to a final dir. 
# Unfortunately it has to be done manually, because we cannot use an option 
# for putting scripts into a separate dir - --install-option="--install-scripts=/build/bin".
# The problem is that pip skips wheels when this option is enabled.

BUILD_BIN=$BUILD_DIR/bin
if [ ! -d $BUILD_BIN ]; then
  mkdir $BUILD_BIN
fi

cp $SCRIPTS_DIR/gunicorn \
   $SCRIPTS_DIR/gunicorn_django \
   $SCRIPTS_DIR/gunicorn_paster \
   $SCRIPTS_DIR/jwt \
   $SCRIPTS_DIR/pbr \
   $BUILD_BIN
