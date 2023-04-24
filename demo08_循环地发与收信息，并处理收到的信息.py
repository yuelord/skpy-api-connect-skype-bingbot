import time  # 调用来睡眠
import datetime  # 计算耗时,标记发送时间和标记消息接收的时间
import html  # 用来将实体字符转换为HTML标签,常用再有编程代码示例的消息中
from bs4 import BeautifulSoup  # 快速将带有HTML标签的字符去掉，保留网页的文本
import lxml  # 快速将获得的消息字符串,解释成网页,方便对消息中多余的HTML标签去除
from skpy import Skype
# 从__init__中读取skpye账号和密码
from account import skpye_name, password

# 登录Skype
sk = Skype(skpye_name, password)
# 与bing建立联系
chat = sk.chats['28:cf0e6215-34fe-xxx-xxxx-xxxxxxxxxxxx']


# 接收消息
def getNewMessage(sending_time):
    message = None
    flag = True
    """
    如果消息(问题)发送出去了,bing还没有处理好答案(消息),则循环获取消息,
    直到获到回复了问题(可能获得的消息不完整,只发了消息的前一段内容,至于完整的消息在里面中处理),才停止循环
    """
    while flag:
        # 先睡眠一会,不要着急获取信息，bing可能没有写完消息或者还在思考中（没有消息响应）
        time.sleep(3)
        # 首次接收消息
        mgs = chat.getMsgs()
        # 首次获取消息中的服务器时间，并将该时间换成北京时间(第一次，获取消息,消息中的服务器时间)
        first_server_time = mgs[0].time + datetime.timedelta(hours=8)
        # 判断获得的消息是否为bing回复的,判断时间的时间是否来自发送信息时间的后面,则执行if语句(选择新消息的内容)
        if (mgs[0].userId == "cf0e6215-34fe-409b-9e4b-135d7f3aa13b") and (first_server_time > sending_time):
            # 如果是当问题的回复，就不用while循环了（跳过下面的内容，重新从服务器获取信息）
            flag = False
            # clientId，用于判断消息是否还没发送完整
            clientId = mgs[0].clientId
            # 初次获得新消息
            message = mgs[0].content
            # print("初次获得：", message)
            # 防止消息没有接收完
            for i in range(2):
                # 睡眠,一方面等待bing把消息写完(预计bing写完),另一方面防止获取消息太过频繁
                time.sleep(3)
                # 再次接收消息(判断消息有没有写完)
                new_mgs = chat.getMsgs()

                # new_clientId，用于判断消息是否跟上面的clientId是否一样，即还有消息没有接收完整?
                new_clientId = new_mgs[0].clientId
                # print(new_mgs[0].time)
                # 获取消息中的服务器时间，并将该时间换成北京时间(这个时间是新获取的)
                server_time = new_mgs[0].time + datetime.timedelta(hours=8)
                # print("再次获取消息,消息中的服务器时间：", server_time)

                """
                if判断语句作用:
                一方面,判断回复的消息是否回复同一个问题，防止获取到的消息不是同一个问题(同一个消息),
                另一方面,通过消息中的服务器响应时间判断，时间新,且跟前面first_server_time获取消息
                的时间不同,而且新的,说明消息没有接受完,就再获取new_mgs[0].content,替换掉message
                """
                if hash(new_clientId) == hash(clientId) and server_time > first_server_time:
                    # 将最新消息中的服务器时间，传递给 first_server_time参数中，方便下次比较
                    first_server_time = server_time
                    # 再次读取消息的内容
                    new_content = new_mgs[0].content
                    print("再次获得消息，新消息的字符串长度为：", len(new_content), "旧消息的字符串长度为：", len(message))
                    # 新的消息内容覆盖旧的消息
                    message = new_content
        else:
            # 防止频繁执行getMsgs()方法，短时间内不断向服务器发送请求，获取消息，导致账号被封
            time.sleep(2)
    return message


# 格式化消息（把消息中HTML标签去掉）
def format_str(message):
    # html_doc的类型可以是字符串、文件对象、URL,这里使用的是字符串
    html_doc = message
    # 将字符串解析成网页的HTML格式，方便去除HTML标签
    soup = BeautifulSoup(html_doc, "lxml")
    # 提取网页的正文内容（文本内容）
    str_content = soup.text
    # 使用html.unescape()可以将HTML实体字符转换为HTML标签（这里使用到html库）
    return html.unescape(str_content)


# 计算从提问的问题回答消耗多久
def runtime(sending_time):
    end_time = datetime.datetime.now()
    # 用后一个时间减去前一个时间,得到一个timedelta对象（计算消耗的时间）
    time_delta = end_time - sending_time
    # 从timedelta对象中分别获取天, 秒等信息
    hours, remainder = divmod(time_delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    # 用需要的格式显示时间差信息
    elapsed_time = f"{minutes}:{seconds}"
    # 返回消逝的时间
    return elapsed_time


def main():
    flag = True
    while flag:
        # 发送信息
        send_msg = input("请输入问题：").strip()
        if send_msg != "exit":
            chat.sendMsg(send_msg)
            # 记录发送消息成功后的时间
            sending_time = datetime.datetime.now()
            print("本次的提问时间：", sending_time)
            # 睡眠5秒,等待bing的消息回复
            time.sleep(4)
            """
            接收消息，调用自己定义的format_str()函数,对获取到的消息进行处理（清除HTML标签,只保留文字）
            """
            message = format_str(getNewMessage(sending_time))
            print("最后的答案：", message, sep="\n")
            # 调用runtime函数，计算程序运行多久（计算从提问到回答的消耗时间）
            elapsed_time = runtime(sending_time)
            print("本次回答消耗时间：", elapsed_time)
        elif send_msg.lower() == "exit":
            flag = False


if __name__ == '__main__':
    main()
