import logging
import datetime
from config.config import log_path
import os


def get_logger():
    t = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    logger = logging.getLogger(t)
    logger.setLevel(logging.INFO)
    format = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
                               datefmt='%Y-%m-%d %H:%M:%S')  # 日志格式
    cli_handler = logging.StreamHandler()  # 输出到屏幕的日志处理器
    logname = t + '.log'
    p = os.path.join(log_path, logname)
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    if os.path.exists(logname):
        os.rename(logname, logname + "~")
    file_handler = logging.FileHandler(filename=p, mode='a',
                                       encoding='utf-8')  # 输出到文件的日志处理器，mode默认是’a’，即添加到文件末尾，‘w’是覆盖写入

    cli_handler.setFormatter(format)  # 设置屏幕日志格式
    file_handler.setFormatter(format)  # 设置文件日志格式
    logger.handlers.clear()  # 清空已有处理器, 避免继承了其他logger的已有处理器
    logger.addHandler(cli_handler)  # 将屏幕日志处理器添加到logger
    logger.addHandler(file_handler)  # 将文件日志处理器添加到logger
    return logger


logger = get_logger()
