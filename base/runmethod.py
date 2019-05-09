#请求方法的封装
import requests,json
from util.operation_json import Operation_Josn
class RunMethod:
    def __init__(self):
        #实例化一个叫做session类,让session发送get,或者post等请求
        self.send=requests.session()
    def post_main(self,url,data,header=None):
        if header!=None:
            res = self.send.post(url=url, json=data, headers=header,verify=False).json()
        else:
            res=self.send.post(url=url,json=data,verify=False).json()
        return res
    def get_main(self,url,data,header=None):
        if header!=None:
            res = self.send.get(url=url, params=data, headers=header,verify=False).json()
        else:
            res = self.send.get(url=url, params=data, verify=False).json()
        return res
    def put_main(self,url,data,header=None):
        if header!=None:
            res = requests.put(url=url, json=data, headers=header,verify=False)
        else:
            res=requests.put(url=url,json=data,verify=False)
        return res
    def delete_main(self,url,data,header=None):
        if header!=None:
            res = requests.delete(url=url, params=data,headers=header, verify=False)
        else:
            res=requests.delete(url=url,params=data,verify=False)
        return res
    def run_main(self,method,url,data=None,header=None):
        if method=="post":
            res= self.post_main(url,data,header)
        elif method=="get":
            res=self.get_main(url,data,header)
        elif method=="put":
            res=self.put_main(url,data)
        else:
            res=self.delete_main(url,data)
        # return res
        return json.dumps(res,ensure_ascii=False,indent=4)
if __name__ == '__main__':
    read = Operation_Josn()
    run=RunMethod()
    url = "http://www.yunchejinrong.com:8090/api/v1/employee/login"
    data = read.get_data('login')
    aa=run.run_main('post',url,data)
    print(aa)





