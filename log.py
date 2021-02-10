import time
import logging

class LogOutput():
    def logOutput(self,log_dir,name_project):
        '''
        :param log_dir: 日志路径
        :param name_project: 项目名称=>用于日志命名
        :return:
        '''
        # sys.path.append(os.chdir('../log'))
        now = time.strftime("%Y_%m_%d %H_%M_%S")
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=log_dir+ now +'-'+name_project+'_test_log.log',
                            filemode='w')
        logging.debug('我的debug信息')
        logging.info('我的info信息')
        logging.warning('我的warning信息')
        logging.error('我的error信息')
        logging.critical('我的critical信息')
        logger = logging.getLogger()
        logger.info(self)