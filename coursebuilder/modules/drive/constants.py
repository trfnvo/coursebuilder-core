# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Drive module constants"""

__author__ = [
    'nretallack@google.com (Nick Retallack)',
]

import os
import appengine_config

MODULE_NAME = 'drive'
MODULE_TITLE = 'Drive'
SERVICE_ACCOUNT_JSON_FIELD_NAME = 'service_account_json'
TEMPLATE_DIR = os.path.join(
    appengine_config.BUNDLE_ROOT, 'modules', MODULE_NAME, 'templates')
