from skpy import Skype
# 从__init__中读取skpye账号和密码
from account import skpye_name, password

# 登录Skype
sk = Skype(skpye_name, password)

# 获取您最近的 Skype 聊天会话列表的ID
recent_chats = [x for x in sk.chats.recent()]
print(recent_chats)
# ['28:cf0e6215-34fe-xxx-xxxx-xxxxxxxxxxxx', '28:concierge', '8:cf0e6215-34fe-xxx-xxxx-xxxxxxxxxxxx']