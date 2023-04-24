from skpy import Skype
# 从__init__中读取skpye账号和密码
from account import skpye_name, password

# 登录Skype
sk = Skype(skpye_name, password)

"""
在Skype中,每个聊天都有一个全局唯一的ID,格式通常为"数字:字母数字混合字符串"。
使用SkPy登录Skype后,我们可以通过聊天的ID直接获取对应的聊天对象,进行消息读取、发送以及其他交互。
"""
# 获取指定联系人ID的聊天【对象】，这里是：与bing机器人建立对话
# 注意要使用全局的ID
chat = sk.chats["28:cf0e6215-34fe-xxx-xxxx-xxxxxxxxxxxx"]
print(chat)

"""
[SkypeSingleChat]
Id: 28:cf0e6215-34fe-xxx-xxxx-xxxxxxxxxxxx
Alerts: True
UserId: cf0e6215-34fe-xxx-xxxx-xxxxxxxxxxxx
"""
