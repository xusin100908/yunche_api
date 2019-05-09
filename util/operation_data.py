from util.operation_dict import OpenrationDict
from util.random_number import RandomNumber
from util.operation_json import Operation_Josn
from data.get_data import GetData
from util.operation_Excel import OperationExcel
class OpenrationData:
    """
    这是一个更新请求数据,获取依赖数据并更新的类
    """
    def __init__(self):
        self.op_dict=OpenrationDict()
        self.random = RandomNumber()
        self.op_json=Operation_Josn()
        self.op_excel=OperationExcel()
        self.get_data=GetData()
    def update_requests(self,row):
        """
        更新请求数据,并存储
        :param dict_name: 更新的字典的名字
        :param key: 要更新的key
        :param get_json: 获取json数据
        :param my_dict: 要更新的字典
        :return:
        """
        get_json=self.op_json.read_data()
        dict_name=self.get_data.get_request_data(row)
        update_key=self.get_data.get_update_data(row)
        for key in update_key:
            my_dict = get_json[dict_name]
            random_data = self.random.get_random_date(key)
            self.op_dict.updata_data(my_dict,key,random_data)
            self.op_json.write_data(get_json)
    def replace_requests_data(self,depend_case,row):
        """替换请求数据"""
        depend_key=self.get_data.get_depend_key(row)#依赖字段
        replace_key=self.get_data.get_replace_key(row)#替换字段
        if depend_key and replace_key:
            col = self.op_excel.get_row_num(depend_case)#通过依赖case获取到行数
            result=self.get_data.get_result(col)#获取对应行数实际结果
            depend_data=self.op_dict.get_value(result,depend_key)#通过key提取出对应的值
            get_json=self.op_json.read_data()#json数据
            dict_name = self.get_data.get_request_data(row)#请求的key
            my_dict=get_json[dict_name]#通过key在json数据中找我请求数据
            self.op_dict.updata_data(my_dict, replace_key, depend_data)#更新字典中任意一个key对应的值
            self.op_json.write_data(get_json)#保存json数据
        else:
            print('依赖字段或者替换字段不能为空')
if __name__ == '__main__':
    od=OpenrationData()
    aa=od.replace_requests_data('test002',3)




