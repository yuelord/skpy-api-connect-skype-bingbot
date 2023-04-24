from skpy import Skype
# 从__init__中读取skpye账号和密码
from account import skpye_name, password

# 登录Skype
sk = Skype(skpye_name, password)
print("查看所有联系人：")
all_li = [x for x in sk.contacts]
# print(all_li)
for item in all_li:
    f_id = item.id
    f_name = item.name
    print("联系人的名称：", f_name, "联系人的ID：", f_id)

"""
查看所有联系人：
联系人的名称： Bing 联系人的ID： cf0e6215-34fe-xxx-xxxx-xxxxxxxxxxxx
联系人的名称： Skype 联系人的ID： concierge
联系人的名称： Echo / Sound Test Service . 联系人的ID： echo123
"""
