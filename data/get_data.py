from util.operation_Excel import OperationExcel
from util.operation_json import Operation_Josn
import json,time
class GetData:
	def __init__(self):
		self.opera_json = Operation_Josn()
		self.Id = 0  # caseid
		self.request_name=1#接口名称
		self.run = 2  # 是否执行
		self.url = 3  # url
		self.method = 4  # 请求方法
		self.data = 5  # 请求数据
		self.header = 6  # 请求头
		self.case_depend = 7  # 依赖case
		self.key_depend = 8  # 依赖字段
		self.replace = 9  # 替换字段
		self.update_way=10#是否更新入参
		self.updata_data=11#更新字段
		self.expect = 12  # 预期结果
		self.result = 13  # 实际结果
		self.failure = 14  # 是否通过
		self.time=15#当前时间
		self.opera_excel = OperationExcel()
	#去获取excel行数,就是我们的case个数	
	def get_case_lines(self):
		return self.opera_excel.get_lines()
	#获取可接名称
	def get_request_name(self,row):
		col = self.request_name
		request_name = self.opera_excel.get_cell_value(row, col)
		return request_name
	#获取是否执行
	def get_is_run(self,row):
		flag = None
		col = self.run
		run_model = self.opera_excel.get_cell_value(row,col)
		if run_model == 'yes':
			flag = True
		else:
			flag = False
		return flag
	#是否携带header
	def get_is_header(self,row):
		col = self.header
		header = self.opera_excel.get_cell_value(row,col)
		if header != '':
			headers=None
			if isinstance(header,dict):
				headers=header
			elif isinstance(header,str):
				headers=json.loads(header)
			else:
				headers="type错误"
			return headers
		else:
			return None
	#获取请求方式
	def get_request_method(self,row):
		col = self.method
		request_method = self.opera_excel.get_cell_value(row,col)
		return request_method
	#获取url
	def get_request_url(self,row):
		col = self.url
		url = self.opera_excel.get_cell_value(row,col)
		return url
	#获取请求数据
	def get_request_data(self,row):
		col = self.data
		data = self.opera_excel.get_cell_value(row,col)
		if data == '':
			return None
		return data
	#获取是否更新
	def get_is_update(self,row):
		flag = None
		col = self.update_way
		update_way = self.opera_excel.get_cell_value(row,col)
		if update_way == 'yes':
			flag = True
		else:
			flag = False
		return flag
	#获取更新数据
	def get_update_data(self,row):
		col = self.updata_data
		updata_data = (self.opera_excel.get_cell_value(row, col)).split()
		return updata_data
	#通过获取关键字拿到data数据
	def get_data_for_json(self,row):
		request_data = self.opera_json.get_data(self.get_request_data(row))
		return request_data

	#获取预期结果
	def get_expcet_data(self,row):
		col = self.expect
		expect = self.opera_excel.get_cell_value(row,col)
		if expect == '':
			return None
		return expect
	#写入实际结果
	def write_result(self,row,value):
		col = self.result
		self.opera_excel.write_value(row,col,value)
		return value
	#写入当前时间
	def write_time(self,row):
		value=time.strftime("%y-%m-%d %H:%M:%S")
		col = self.time
		self.opera_excel.write_value(row,col,value)
		return value
	# 获取实际结果
	def get_result(self, row):
		flat=None
		self.op_excel = OperationExcel()
		col = self.result
		data = self.op_excel.get_cell_value(row, col)
		if isinstance(data,dict):
			result=data
		else:
			result=json.loads(data)
		return result
	# 写入是否通过
	def write_is_failure(self,row,value):
		col = self.failure
		self.opera_excel.write_value(row,col,value)
	#判断是否有case依赖
	def get_is_depend(self,row):
		col = self.case_depend
		depend_case_id = self.opera_excel.get_cell_value(row,col)
		if depend_case_id == "":
			return None
		else:
			return depend_case_id
	#获取依赖字段
	def get_depend_key(self,row):
		col = self.key_depend
		depent_key = self.opera_excel.get_cell_value(row,col)
		if depent_key == "":
			return None
		else:
			return depent_key
	#获取替换字段
	def get_replace_key(self,row):
		col = self.replace
		data = self.opera_excel.get_cell_value(row,col)
		if data == "":
			return None
		else:
			return data
if __name__ == '__main__':
	aa=GetData()
	# print('获取用例行数:{}'.format(aa.get_case_lines()))
	# print('获取是否执行:{}'.format(aa.get_is_run(2)))
	# print('获取是否携带header:{}'.format(aa.get_is_header(8)))
	# print('获取请求方法:{}'.format(aa.get_request_method(2)))
	# print('获取URL:{}'.format(aa.get_request_url(2)))
	# print('获取请求数据:{}'.format(aa.get_request_data(2)))
	# print('获取是否更新:{}'.format(aa.get_is_update(2)))
	# print('获取更新数据:{}'.format(aa.get_update_data(2)))
	# print('获取关键字拿到data数据:{}'.format(aa.get_data_for_json(2)))
	# print('获取预期结果:{}'.format(aa.get_expcet_data(8)))
	# print('获取实际结果:{}'.format(aa.get_result(8)))
	# print('获取依赖case:{}'.format(aa.get_is_depend(3)))
	# print('获取依赖字段:{}'.format(aa.get_depend_key(3)))
	# print('获取替换字段:{}'.format(aa.get_replace_key(3)))
	a=aa.get_is_header(8)
	token='345534646'
	b=a['Authorization']+token
	print(b)
