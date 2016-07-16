# Copyright 2016 by Nedim Sabic (RabbitStack)
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from logbook import Logger, StreamHandler
import sys


class BaseAdapter(object):

    def __init__(self):
        StreamHandler(sys.stdout).push_application()
        self.logger = Logger()

    def emit(self, body, **kwargs):
        raise NotImplementedError()
