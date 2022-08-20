import logging
import datetime
from config.config import log_path
import os


def get_logger():
    t = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    logger = logging.getLogger(t)
    logger.setLevel(logging.INFO)
    format = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
                               datefmt='%Y-%m-%d %H:%M:%S')  # ��־��ʽ
    cli_handler = logging.StreamHandler()  # �������Ļ����־������
    logname = t + '.log'
    p = os.path.join(log_path, logname)
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    if os.path.exists(logname):
        os.rename(logname, logname + "~")
    file_handler = logging.FileHandler(filename=p, mode='a',
                                       encoding='utf-8')  # ������ļ�����־��������modeĬ���ǡ�a��������ӵ��ļ�ĩβ����w���Ǹ���д��

    cli_handler.setFormatter(format)  # ������Ļ��־��ʽ
    file_handler.setFormatter(format)  # �����ļ���־��ʽ
    logger.handlers.clear()  # ������д�����, ����̳�������logger�����д�����
    logger.addHandler(cli_handler)  # ����Ļ��־��������ӵ�logger
    logger.addHandler(file_handler)  # ���ļ���־��������ӵ�logger
    return logger


logger = get_logger()
