#操作json文件
import json
class Operation_Josn:
    def __init__(self,file_path=None):
        if file_path:
            self.file_path = file_path
        else:
            self.file_path='../data_config/send_data.json'
            # self.data = self.read_data()
    def read_data(self):
        """读取json文件"""
        with open(self.file_path, "r",encoding='utf-8') as json_file:
            data = json.load(json_file)
            json_file.close()
            return data
    def get_data(self,key):
        """通过关键字key,获取数据"""
        self.data = self.read_data()
        return self.data[key]
    def write_data(self,data=None,):
        """写入json"""
        json_path='../data_config/send_data.json'
        with open(json_path, 'wb') as fp:
            fp.write(json.dumps(data,ensure_ascii=False,indent=4).encode(encoding='utf-8'))
if __name__ == '__main__':
    read=Operation_Josn()



