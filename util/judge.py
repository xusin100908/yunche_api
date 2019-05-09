#响应断言的封装
class Assert:
    def __init__(self,data):
        self.data=data
    def assertIn(self,expect,res,row):
        """
        判断是否包含
        :param expect: 预期结果
        :param res: 实际结果
        :return:
        """
        if expect in res:
            self.data.write_is_failure(row,'pass')
            flag=True
        else:
            self.data.write_is_failure(row, 'fault')
            flag=False
        self.data.write_result(row, res)
        self.data.write_time(row)
        return flag


