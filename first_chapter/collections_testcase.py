'''
@Project ：py-master 
@File    ：collections_testcase.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2024/8/14 7:48 
'''

import collections
from random import choice

User = collections.namedtuple('User', ['name', 'age', 'gender'])
# User = collections.namedtuple('User', 'name age gender')

user = User('zhangsan', '23', 'male')

print(f"user:{user}")
print(f"name:{user.name}")

class Student:
    name_list = ["zhangsan","lisi", "wangwu","zhaoliu","liuqi", "maba","qianjiu"]
    age_list = [18, 17, 15, 14, 20, 21, 22]
    gender_list = ['male','male','male','female','male','male', 'female']
    def __init__(self):
        self._users = [User(name, age, gender) for name in self.name_list
                       for age in self.age_list
                       for gender in self.gender_list]
        for user in self._users:
            print(f"{user.name} {user.age} {user.gender}")

    def __len__(self):
        return len(self._users)

    def __getitem__(self, index):
        return self._users[index]

if __name__ == '__main__':
    stu = Student()
    print(f"type of stu:{type(stu)}")
    l = len(stu)
    print(f"l_stu:{l}")
    print(f"stu[0]:{stu[0]}")
    print(f"c1:{choice(stu)}")
    print(f"c2:{choice(stu)}")
    print(f"c3:{choice(stu)}")

