使用第三库SkPy，连接 Skype 的 bing 聊天机器人（new bing），做到与官方的 Skype 一样，发、收信息（最基础的功能）。

## 修改代码：

1、修改account中的__init__.py

改为自己的skpye账号和密码

2、修改所有含有如下代码的 .py 文件：

```
chat = sk.chats["28:cf0e6215-34fe-xxx-xxxx-xxxxxxxxxxxx"]
```

修改引号中的内容，如果你也想连接bing聊天机器人，就要要加上前缀"**28:**"，它的含义是标识**聊天机器人用户**，**普通用户**则是"**8:**"，当然还有其它数字为开头的，这里用不到，感兴趣的自己查询。

怎么找自己的"**28:cf0e6215-34fe-xxx-xxxx-xxxxxxxxxxxx**"，观察**demo01**和**demo2**的运行结果，就知道与谁聊天，这里就怎么写。

观察**demo03**的运行结果，就知道你有没有写错"**28:cf0e6215-34fe-xxx-xxxx-xxxxxxxxxxxx**"。

## 参考资料：

SkPy学习文档：https://skpy.t.allofti.me/index.html
https://github.com/Terrance/SkPy

案例：https://github.com/DimitriChrysafis/SkypeBots

