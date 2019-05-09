class OpenrationDict:
    """
    这是一个解析dict参数的类,
    可用于多参数的指定key,指定key集合解析key,更新指定key的值
    """
    def get_value(self,my_dict,key):
        """
        这是一个递归函数
        :param my_dict: 传入的字典
        :param key: 字典中的key
        :return:返回字典中某个key对应的值
        """
        if isinstance(my_dict,dict):
            if my_dict.get(key)or my_dict.get(key)==0 or my_dict.get(key)==''\
                    and my_dict.get(key) is False:
                return my_dict.get(key)
            for my_dict_key in my_dict:
                if self.get_value(my_dict.get(my_dict_key),key)or\
                    self.get_value(my_dict.get(my_dict_key),key)is False:
                    return self.get_value(my_dict.get(my_dict_key),key)
        if isinstance(my_dict,list):
            for my_dict_arr in my_dict:
                if self.get_value(my_dict_arr,key)\
                    or self.get_value(my_dict_arr,key)is False:
                    return self.get_value(my_dict_arr,key)
    def updata_data(self,my_dict,key,value):
        """
        更新字典中任意一个key对应的值
        :param my_dict: 传入的字典
        :param key: 字典中的key
        :param value: 更新对应key内容
        :return: 更新后的字典
        """
        if isinstance(my_dict,dict):
            if my_dict.get(key)or my_dict.get(key)==0 or my_dict.get(key)==''\
                    and my_dict.get(key) is False:
                my_dict[key]=value
                return my_dict
            for my_dict_key in my_dict:
                if self.updata_data(my_dict.get(my_dict_key),key,value)or\
                    self.updata_data(my_dict.get(my_dict_key),key,value)is False:
                    # return self.updata_data(my_dict.get(my_dict_key),key,value)
                    return my_dict
        if isinstance(my_dict,list):
            for my_dict_arr in my_dict:
                if self.updata_data(my_dict_arr,key,value)\
                    or self.updata_data(my_dict_arr,key,value)is False:
                    # return self.updata_data(my_dict_arr,key,value)
                    return my_dict
if __name__ == '__main__':
    a = {'a':{"b":{'c':{'d':[{'e':"4"},{'f':''}]}}}}
    op=OpenrationDict()
    print(op.get_value(a,"e"))
    print(op.updata_data(a,'f',1428))