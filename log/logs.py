import json
import os
import logging
import datetime

#日志类
class Log:
#创建日志记录所需要的文件夹
    def test_dir(self):
        curDir = datetime.datetime.now().strftime('%Y-%m-%d')
        #在上一级relust目录下创建log目录，并以当前日期命名日志文件夹
        path = '../log/' + curDir
        # 去掉首尾空格
        path = path.strip()
        # 去掉尾部\符号
        # path = path.rstrip("\\")
        # print(path)
        isExists = os.path.exists(path)
        if not isExists:
            #创建以当前日期命名的文件夹，如果父目录不存在也一并创建makedirs
            os.makedirs(path)
            #返回目录地址
            return path
        else:
            return path

#记录接口请求输出日志
    def test_log(self,request_name,method_url,data,response):
        #调用创建目录的方法
        #Log.test_dir(self)
        #使用test_dir()方法中返回的path属性值
        path = Log.test_dir(self)
        logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
                            filename=path + '/' + 'data.log',#指定文件存储的路径以及文件名
                            # filename='./'+'data.log',
                            filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志a是追加模式，默认如果不写的话，就是追加模式
                            # 日志格式
                            format=
                            '%(asctime)s - %(levelname)s: %(message)s'
                            )
        logger = logging.getLogger(__name__)
        # 记录执行接口名称
        logger.info('testcase :'+request_name)
        #记录执行接口的方法和url
        logger.info('Method/Url '+method_url)
        #记录接口请求数据
        logger.info('RequestData:'+json.dumps(data,ensure_ascii=False,indent=4))
        # 记录接口响应数据
        logger.info('Response Data:'+response)
        # 记录异常信息
    def error_log(self,error):
        #调用创建目录的方法
        #Log.test_dir(self)
        #使用test_dir()方法中返回的path属性值
        path = Log.test_dir(self)
        logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
                            filename=path + '/' + 'error.log',#指定文件存储的路径以及文件名
                            # filename='./'+'data.log',
                            filemode='w',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志a是追加模式，默认如果不写的话，就是追加模式
                            # 日志格式
                            format=
                            '%(asctime)s - %(levelname)s: %(message)s'
                            )
        logger = logging.getLogger(__name__)
        # 记录异常信息
        logger.error(error)
if __name__ == '__main__':
    aa=Log()
    aa.error_log('错误日志打印')


