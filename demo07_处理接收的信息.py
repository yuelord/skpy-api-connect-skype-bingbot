from skpy import Skype
from bs4 import BeautifulSoup
# 从__init__中读取skpye账号和密码
from account import skpye_name, password
import html


# 登录Skype
sk = Skype(skpye_name, password)
# 与bing建立联系
chat = sk.chats['28:cf0e6215-34fe-xxx-xxxx-xxxxxxxxxxxx']

# 接收消息
chat = chat.getMsgs()
# 只要content的文本内容
html_doc = chat[0].content
soup = BeautifulSoup(html_doc, "html.parser")
str_content = soup.text
# 使用html.unescape()可以将HTML实体字符转换为HTML标签
# 使用html.escape()可以将HTML标签转换为HTML实体字符
print(html.unescape(str_content))
