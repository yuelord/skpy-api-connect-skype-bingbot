import time
import datetime
# 从__init__中读取skpye账号和密码，bing聊天机器人的全局ID（skype_id）
from account import skpye_name, password, skype_id
from skpy import Skype

# 登录Skype
sk = Skype(skpye_name, password)
# 与bing建立联系
chat = sk.chats[skype_id]


# 接收消息
def getNewMessage(sending_time):
    message = None
    flag = True
    while flag:
        # 不要着急获取信息，bing可能没有写完消息或者还在思考中（没有消息响应）
        time.sleep(3)
        # 首次接收消息
        mgs = chat.getMsgs()
        # 获取服务器的时间，并将服务器的时间换成北京时间(第一次，从服务器中获取响应消息的服务器时间)
        first_server_time = mgs[0].time + datetime.timedelta(hours=8)
        # 判断是否为回复当前的问题（最新消息且是bing回复）
        if (mgs[0].userId == "cf0e6215-34fe-409b-9e4b-135d7f3aa13b") and (first_server_time > sending_time):
            # 如果是当问题的回复，就不用while循环了（跳过下面的内容，重新从服务器获取信息）
            flag = False
            # clientId，用于判断消息是否还没发送完整
            clientId = mgs[0].clientId

            # 初次获得新消息
            message = mgs[0].content
            print("初次获得：", message)

            # 防止消息没有接收完
            for i in range(2):
                time.sleep(4)
                # 再次接收消息
                new_mgs = chat.getMsgs()

                # new_clientId，用于判断消息是否跟上面的一样，即还有消息没有接收完整
                new_clientId = new_mgs[0].clientId
                print(new_mgs[0].time)
                # 获取服务器的时间，并将服务器的时间换成北京时间(再次，从服务器中获取响应消息的服务器时间)
                server_time = new_mgs[0].time + datetime.timedelta(hours=8)
                print("当次获取的服务器时间：", server_time)

                new_now_time = datetime.datetime.now()
                print("当前电脑的时间：", new_now_time)

                # 判断回复的消息是否回复同一个问题，并且服务器响应时间是新的，跟之前获得服务器时间不同
                if hash(new_clientId) == hash(clientId) and server_time > first_server_time:
                    # 将获得服务器时间，替换 第一次从服务器的时间，方便下次比较
                    first_server_time = server_time
                    # 再次读取消息的内容
                    new_content = new_mgs[0].content
                    print("再次获取，新：", len(new_content), "旧：", len(message))
                    # 新的消息内容覆盖旧的消息
                    message = new_content
        else:
            # 防止频繁执行getMsgs()方法，短时间内不断向服务器发送请求，获取消息，导致账号被封
            time.sleep(2)
    return message


def main():
    while True:
        # 发送信息
        send_msg = input("请输入问题：").strip()
        if send_msg != "exit":
            chat.sendMsg(send_msg)
            # 记录发送消息成功后的时间
            sending_time = datetime.datetime.now()
            print("当前提问时间：", sending_time)
            time.sleep(10)
            # 接收消息
            message = getNewMessage(sending_time)
            print("最后答案：", message)


if __name__ == '__main__':
    main()
