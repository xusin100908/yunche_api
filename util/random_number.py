import string,random
class RandomNumber:
    #这是一个随机生成邮箱,身份证号,手机号,用户名的类
    def mobile(self):
        """随机生成手机号"""
        mobile_head = ['134', '135', '188', '185', '172', '152']
        mobile_tail=''.join(random.sample(string.digits,8))
        mobile=random.choice(mobile_head)+mobile_tail
        return mobile
    def email(self):
        """随机生成邮箱"""
        h_email=['@qq.com','@163.com','@199.com']
        email_head = str(random.randint(111111, 999999))
        user_email=email_head+random.choice(h_email)
        return user_email
    def idCard(self):
        """随机生成身份证号"""
        icard_head = str(random.randint(111111,999999))
        icard_tail = str(random.randint(11111,99999))
        icard = icard_head+ str(1993020)+icard_tail
        return icard
    def name(self):
        """随机生成用户名"""
        haed_name=['张','赵','徐','欧阳','黄','陈','李','王','龙','东方','独孤','西门']
        tail_name=['甄','贤','政','倩','丽','利','伟','伟','洋','阳','微','智','强']
        return random.choice(haed_name)+random.choice(tail_name)
    def get_random_date(self,random_name):
        if random_name=="mobile":
            randoms =self.mobile()
        elif random_name=="email":
            randoms =self.email()
        elif random_name=="idCard":
            randoms=self.idCard()
        else:
            randoms =self.name()
        return randoms

if __name__ == '__main__':
    aa=RandomNumber()
    print(aa.get_random_date('idCard'))
