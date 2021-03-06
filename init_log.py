import logging
import time

logger = logging.getLogger()

def init(self):
    # Log等级总开关
    self.logger.setLevel(logging.INFO)  
    # 第二步，创建一个handler，用于写入日志文件
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    log_path = '.\\Logs\\'
    log_name = log_path + rq + '.log'
    logfile = log_name
    fh = logging.FileHandler(logfile, mode='w', encoding="UTF-8")
    # 输出到file的log等级的开关
    fh.setLevel(logging.INFO)  
    # 第三步，定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    # 第四步，将logger添加到handler里面
    self.logger.addHandler(fh)

    # # 日志打印到屏幕上
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    self.logger.addHandler(ch)