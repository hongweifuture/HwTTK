#!/usr/bin/env python
# coding=utf-8

"""
History:
2019/9/30 9:58 : Created by zhaohongwei 
"""

__author__ = "zhaohongwei"
__email__ = "hongweifuture@163.com"
__contact__ = "https://blog.csdn.net/z_johnny"
__version__ = "0.1"
__date__ = "2019/9/30 9:58"
__maintainer__ = "zhaohongwei,"
__description__ = ""


from HwLogging import HwLogging
# from HwLoggingPy2 import HwLogging
# from HwLoggingPy3 import HwLogging


class LoggingTest():
    def __init__(self):
        config_logging = 'config/logConfig.ini'
        self.logging = HwLogging(config_logging).outputLog()

    def test(self):
        self.logging.debug('logger debug message 打印')
        self.logging.info('logger info message 打印')
        self.logging.warning('logger warning message 打印')
        self.logging.error('logger error message 打印')
        self.logging.critical('logger critical message 打印')

if __name__ == "__main__":
    loggingtest = LoggingTest()
    loggingtest.test()