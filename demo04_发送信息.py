from skpy import Skype
# 从__init__中读取skpye账号和密码
from account import skpye_name, password

# 登录Skype
sk = Skype(skpye_name, password)

# 与bing机器人建立对话
chat = sk.chats["28:cf0e6215-34fe-xxx-xxxx-xxxxxxxxxxxx"]

# 发送消息
chat.sendMsg("你好！")
print("发送信息成功!")
