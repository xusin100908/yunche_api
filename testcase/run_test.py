from base.runmethod import RunMethod
from data.get_data import GetData
from util.judge import Assert
from util.operation_data import OpenrationData
from log.logs import Log
import json
class RunTest:
	def __init__(self):
		self.run_method = RunMethod()
		self.data = GetData()
		self.asserts=Assert(self.data)
		self.od=OpenrationData()
		self.log=Log()
	def run_test_case(self):
		try:
			res = None
			rows_count = self.data.get_case_lines()
			for row in range(1, rows_count):
				is_run = self.data.get_is_run(row)
				if is_run:
					name = self.data.get_request_name(row)
					url = self.data.get_request_url(row)
					method = self.data.get_request_method(row)
					expect = self.data.get_expcet_data(row)
					is_update = self.data.get_is_update(row)
					header = self.data.get_is_header(row)
					depend_case = self.data.get_is_depend(row)
					if is_update:
						self.od.update_requests(row)
					if depend_case:
						self.od.replace_requests_data(depend_case,row)
					request_data = self.data.get_data_for_json(row)
					if header:
						res = self.run_method.run_main(method, url, request_data,header)
					else:
						res = self.run_method.run_main(method, url, request_data)
					self.asserts.assertIn(expect, res, row)
					self.log.test_log(name, method + '/' + url, request_data, res)
		except Exception as er:
			self.log.error_log(er)






if __name__ == '__main__':
	run = RunTest()
	run.run_test_case()

