#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
as-cnp-dev@cisco.com
Copyright 2015-2016 Cisco Systems, Inc.
All rights reserved.
'''

# import ast
# import datetime
import os
# import time
import logging
# from logging import Logger as DefaultLogger
# from logging import Handler
# from logging import LogRecord
from logging.handlers import RotatingFileHandler

# from bson.objectid import ObjectId
# from flask import session

# from flask_restful import current_app
# from utils.app_cfg import get_app_cfg
# from utils.db_conn import DBConn
try:
    from netseen.common.yaml_parser import YamlParser
    CFG = YamlParser().yaml_to_dict()
except ImportError:
    CFG = {'DEBUG': True}


# class DBLogRecord(dict):
#     '''
#     db log format
#     ['user', 'module', 'method', 'contents']
#     '''

#     def __init__(self, **kwargs):
#         secs = time.time()
#         log_time = datetime.datetime.fromtimestamp(secs).strftime("%Y%m%d%H%M")
#         kwargs.update({'time': log_time})
#         super(DBLogRecord, self).__init__(kwargs)


# class CustomLogRecord(LogRecord):
#     '''
#     customize log record
#     '''

#     def __init__(self, name, level, pathname, lineno, msg, args, exc_info, trans_time):
#         LogRecord.__init__(self, name, level, pathname,
#                            lineno, msg, args, exc_info)

#     def get_log(self):
#         '''
#         get log
#         '''
#         record = {}
#         _msg = None
#         try:
#             _msg = ast.literal_eval(self.msg)
#         except StandardError:
#             _msg = self.msg
#         if isinstance(_msg, dict):
#             record.update(_msg)
#         else:
#             record.update({
#                 'log': _msg
#             })
#         record.update({
#             'name': self.name,
#             'levelno': self.levelno,
#             'pathname': self.pathname,
#             'lineno': self.lineno
#         })
#         return record


# class CustomLogger(DefaultLogger):
#     '''
#     customize logger
#     '''

#     def __init__(self, name, level=logging.NOTSET):
#         DefaultLogger.__init__(self, name, level)

#     def makeRecord(self, name, level, fn, lno, msg, args, exc_info, func=None, extra=None):
#         """
#         A factory method which can be overridden in subclasses to create
#         specialized LogRecords.
#         """
#         r_v = CustomLogRecord(name, level, fn, lno, msg, args, exc_info, func)
#         if extra is not None:
#             for key in extra:
#                 if (key in ["message", "asctime"]) or (key in r_v.__dict__):
#                     raise KeyError(
#                         "Attempt to overwrite %r in LogRecord" % key)
#                 r_v.__dict__[key] = extra[key]
#         return r_v

# class DBHandler(Handler, DBConn):
#     '''
#     handler for saving logs to db
#     '''
#     def __init__(self, collection_name):
#         DBConn.__init__(self)
#         Handler.__init__(self)
#         self.set_col_name(collection_name)
#         expire_secs = get_app_cfg('LOGS_RETAIN') * 24 * 3600
#         self.conn.add_index("expireAt", expireAfterSeconds=expire_secs)

#     def format_db_time(self, record):
#         '''
#         format db time
#         '''
#         record.dbtime = time.strftime("#%m/%d/%Y#", time.localtime(record.created))

#     def emit(self, record):
#         self.format(record)
#         #now set the database time up
#         user = session.get('user')
#         self.format_db_time(record)
#         if record.exc_info:
#             record.exc_text = logging.Formatter().formatException(record.exc_info)
#         else:
#             record.exc_text = ""
#         # print record.get_log()
#         # data = record.__dict__
#         data = record.get_log()
#         data.update({"expireAt":  datetime.datetime.utcnow(), "_id": str(ObjectId())})
#         if user:
#             data.update(user)
#         self.conn.insert_multi_docs(data)

#     def close(self):
#         '''
#         close handler
#         '''
#         logging.Handler.close(self)


class Logger(object):
    '''
    handler for adding log to log file
    '''

    def __init__(self, name='default', formater=None):
        path = os.path.normpath(
            os.path.join(os.path.abspath(__file__), '../../../', './logs'))
        if not os.path.exists(path):
            os.makedirs(path)
        self._file = '%s/%s.log' % (path, name)
        self.name = name
        self._formater = formater or \
            "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s"
        super(Logger, self).__init__()

    def get_logger(self):
        '''
        get looger
        '''
        logger_name = '%s.%s' % (self.name, 'log')
        logger = logging.getLogger(logger_name)
        if not logger.handlers:
            logger.addHandler(self.get_handler())
        debug = CFG.get('DEBUG')
        if debug:
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)
        return logger

    # def get_db_logger(self, collection_name="LOG"):
    #     '''
    #     get db logger
    #     '''
    #     logging.setLoggerClass(CustomLogger)
    #     logger_name = '%s.%s'%(self.name, 'db')
    #     logger = logging.getLogger(logger_name)
    #     if not logger.handlers:
    #         db_handler = DBHandler(collection_name)
    #         logger.addHandler(db_handler)
    #     debug = CFG.get('DEBUG')
    #     if debug:
    #         logger.setLevel(logging.DEBUG)
    #     else:
    #         logger.setLevel(logging.INFO)
    #     return logger

    def get_handler(self, level=logging.DEBUG):
        '''
        get handler
        '''
        formatter = logging.Formatter(self._formater)
        handler = RotatingFileHandler(
            self._file, maxBytes=10 * 1024 * 1024, backupCount=5)
        handler.setFormatter(formatter)
        handler.setLevel(level)
        return handler

    def set_handler(self, logger):
        '''
        set logger handler
        '''
        logger.addHandler(self.get_handler())


if __name__ == '__main__':
    LOG = Logger(name='test').get_logger()
    LOG.info('Test message !!!')
