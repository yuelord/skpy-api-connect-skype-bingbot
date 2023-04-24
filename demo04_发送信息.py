from skpy import Skype
# 从__init__中读取skpye账号和密码，bing聊天机器人的全局ID（skype_id）
from account import skpye_name, password, skype_id

# 登录Skype
sk = Skype(skpye_name, password)

# 与bing机器人建立对话
chat = sk.chats[skype_id]

# 发送消息
chat.sendMsg("你好！")
print("发送信息成功!")
