from skpy import Skype
# 从__init__中读取skpye账号和密码，bing聊天机器人的全局ID（skype_id）
from account import skpye_name, password, skype_id
import datetime

# 登录Skype
sk = Skype(skpye_name, password)

# 与bing机器人建立对话,获取指定窗口的聊天对象
chat = sk.chats[skype_id]

# 发送信息

# 接送信息
msgs = chat.getMsgs()
# print("getMsgs() 收到的是", type(msgs))

for msg in msgs:
    # 没有参考价值
    print("消息ID：", msg.id)
    # getTime 代表获得的时间（api数据记录）
    getTime = msg.time
    print(type(getTime), getTime)
    # 将获得的时间格式化一下，顺便转换成中国当地的时间
    new_datatime = getTime + datetime.timedelta(hours=8)
    print(new_datatime)
    # new_datatime = f"{getTime.year}.{getTime.month}.{getTime.day} {getTime.hour + 8}:{getTime.minute}:{getTime.second}"
    print("消息的发送时间：", new_datatime)
    # 表示对话的全部内容，表示当前消息，如何没有写完，就会在发一条消息（因为前一条没有写完），最终结果去重再显示再Skype客户端。
    print("客户端ID", msg.clientId)
    # 自己的用户ID或bing的用户ID
    print("发送信息的用户ID", msg.userId)
    # 全是bing的ID
    print("chatID：", msg.chatId)
    print("聊天内容，content格式输出：")
    print(msg.content)
    # print("聊天内容，plain格式输出：")
    # print(msg.plain)
    # print("聊天内容，html格式输出：")
    # print(msg.html)
    print("----------------分割线----------------")

print("程序运行完毕！")
