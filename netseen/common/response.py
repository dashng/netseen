# Copyright 2015-2017 Cisco Systems, Inc.
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

# import re
# import traceback

import simplejson as json
from flask import Response

# from utils.logger import Logger


class JsonRet(dict):
    '''
    ret to json format
    '''

    def __init__(self, content=None, success=True, info=None, code=None):
        self.res = {"meta": {"status": success,
                             "info": info, "code": code}, "data": None}
        self._content = content
        try:
            if isinstance(content, str):
                try:
                    self._content = json.loads(content)
                except ValueError:
                    self._content = content
            self.res.update({"data": self._content})
        except StandardError as error:
            self.res.update(
                {"meta": {"status": False, "info": str(error)}, "data": None})
        super(JsonRet, self).__init__(self.res)


class JsonRes(Response):
    '''
    json response
    '''

    def __init__(self, content=None, success=True, info=None, code=None, err=None):
        if err:
            if isinstance(err, Exception):
                err_msg = str(err)
            elif isinstance(err, basestring):
                err_msg = err
            if isinstance(info, basestring):
                if '%s' not in info:
                    info = '%s, %s' % (info, err_msg)
                else:
                    info = info % err_msg
            # if isinstance(err, Exception):
                # log = Logger(name="error.track")
                # logger = log.get_logger()
                # logger.error(traceback.format_exc())
        content = json.dumps(
            JsonRet(content=content, success=success, info=info, code=code))
        super(JsonRes, self).__init__(content, status=200,
                                      mimetype="application/json")


class CSVRes(Response):
    '''
    cvs response
    '''

    def __init__(self, content=None, file_name='download.csv'):
        content = content.encode('utf-8-sig')
        super(CSVRes, self).\
            __init__(content,
                     mimetype="text/csv;charset=gb2312",
                     headers={"Content-disposition": "attachment; filename=%s" % file_name})
