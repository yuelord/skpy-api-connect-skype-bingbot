使用第三库SkPy，连接 Skype 的 bing 聊天机器人（new bing），做到与官方的 Skype 一样，发、收信息（最基础的功能）。

<img src="images\web-skype.png" alt="Skype主页面"  />



## 一、使用条件

### 1、账号必须加入 new bing 候补名单 和 科学上网
账号没有加入new bing 或 没有科学上网时，bing 会回复你：
<img src="images\sorry01.png" alt="sorry01"  />

### 2、安装

```
python 3.11
SkPy (版本v0.15.0)
beautifulsoup4 (版本v4.12.0)
lxml (版本v4.9.2)
```

## 二、修改代码：

### 1、修改account中的__init__.py

改为自己的skpye账号、密码、skype_id（即bing聊天机器人的全局ID）

### 2、Skype ID 问题

```
chat = sk.chats[skype_id] # 本代码库，使用变量从__init__.py文件中引入对应的skype_id值
```

你也可以写在这里，直接使用

```
chat = sk.chats["28:cf0e6215-34fe-xxx-xxxx-xxxxxxxxxxxx"]
```

如果你也想连接bing聊天机器人，就要要加上前缀"**28:**"，它的含义是标识**bing聊天机器人用户**，**普通用户**则是"**8:**"，当然还有其它数字为开头的，这里用不到。

### 3、Skype ID 开头带有“8:”或者“28:”等数字的意义？

Skype ID开头带有“8:”或者“28:”等数字,是Skype对不同类型的用户账号做的标识。这些数字代表的含义如下:

```
8: 代表该Skype ID属于个人账号。这是Skype的普通个人用户。
28: 代表该Skype ID属于Microsoft账户。这通常是使用Microsoft账号(如Outlook、Hotmail邮箱)登录Skype的用户。
29: 代表该Skype ID属于Facebook账号。这是使用Facebook账号登录Skype的用户。
30: 代表该Skype ID属于LinkedIn账号。这是使用LinkedIn账号登录Skype的用户。
32: 代表该Skype ID属于企业帐户。这通常是公司提供的Skype for Business(旧称Lync)账号。
```
除此之外，Skype ID还可能以其他数字开头，代表不同的用户类型,比较常见的有:

```
18或19: 代表该Skype ID属于移动电话号码链接的账号。
50或59: 代表该Skype ID属于 landline电话号码链接的账号。
200-599: 代表该Skype ID属于开发人员账号。
600-699: 代表该Skype ID属于Skype测试人员账号。
```

### 4、怎么找自己账号对应的Bing的Skype ID "**28:cf0e6215-34fe-xxx-xxxx-xxxxxxxxxxxx**"。

观察**demo01**和**demo2**的运行结果，就知道与谁聊天，这里就怎么写。

### 5、怎么判断自己输入的Bing的Skype ID是否正确

观察**demo03**的运行结果，就知道你有没有写错"**28:cf0e6215-34fe-xxx-xxxx-xxxxxxxxxxxx**"。

## 三、使用第三方库skpy连接bing的优点与缺点

优点：

- 好像skpye中，与bing聊天(new bing)没有每天的次数限制，可以任意使用new bing的功能（没有验证）。
- 可以通过编写程序处理Skype聊天中实体字符，提取自己需要的信息。

<img src="images\error01.png" alt="error01"  />

<img src="images\error02.png" alt="error02"  />

<img src="images\error03.png" alt="error03"  />

缺点：

- 需要一个已经加入new bing的账号
- 需要科学上网

## 四、代码运行截图

<img src="images\skpye-show.png" alt="Skpye客户端显示如图"  />

<img src="images\runcode-demo08.png" alt="demo08_循环地发与收信息，并处理收到的信息.py 的运行效果"  />

## 五、参考资料

SkPy学习文档：https://skpy.t.allofti.me/index.html

https://github.com/Terrance/SkPy

案例：https://github.com/DimitriChrysafis/SkypeBots

