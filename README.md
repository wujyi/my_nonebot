# my_nonebot
高级语言程序设计课程用机器人

## 说明

该项目主要负责构建QQ机器人，从而帮忙完成同济大学高级语言程序设计课程群的管理工作，仅供学习用途。

该项目基于QQ机器人框架[`nonebot`](https://github.com/nonebot/nonebot)开发。

## nonebot 简介

NoneBot 是一个基于 [OneBot 标准](https://github.com/howmanybots/onebot)（原 CQHTTP） 的 Python 异步 QQ 机器人框架，它会对 QQ 机器人收到的消息进行解析和处理，并以插件化的形式，分发给消息所对应的命令处理器和自然语言处理器，来完成具体的功能。

除了起到解析消息的作用，NoneBot 还为插件提供了大量实用的预设操作和权限控制机制，尤其对于命令处理器，它更是提供了完善且易用的会话机制和内部调用机制，以分别适应命令的连续交互和插件内部功能复用等需求。

NoneBot 在其底层与 OneBot 实现交互的部分使用 [aiocqhttp](https://github.com/nonebot/aiocqhttp) 库，后者在 [Quart](https://pgjones.gitlab.io/quart/) 的基础上封装了与 OneBot 实现的网络交互。

得益于 Python 的 [asyncio](https://docs.python.org/3/library/asyncio.html) 机制，NoneBot 处理消息的吞吐量有了很大的保障，再配合 OneBot 标准的 WebSocket 通信方式（也是最建议的通信方式），NoneBot 的性能可以达到 HTTP 通信方式的两倍以上，相较于传统同步 I/O 的 HTTP 通信，更是有质的飞跃。

需要注意的是，NoneBot 仅支持 Python 3.7+。

## nonebot 安装

首先，请确保你的 Python 版本 >= 3.7。

然后，我们可以使用pip安装目前的发布的最新版本

[![1.png](https://i.postimg.cc/HsmJt5dY/1.png)](https://postimg.cc/9zxFmDDK)

从 [release](https://github.com/Mrs4s/go-cqhttp/releases)界面下载对应系统的 go-cqhttp 可执行文件，并解压。

[![image.png](https://i.postimg.cc/RhDppZk4/image.png)](https://postimg.cc/V0XFdmsV)

双击或在命令行中运行 go-cqhttp（Windows 上为 go-cqhttp.exe），在提示选择通信方式时，选择「反向 Websocket 通信」，程序将会自动生成默认配置文件。
打开 go-cqhttp 默认配置文件 config.yml 进行简单配置，修改 QQ 账号以及密码。再次运行 go-cqhttp，可能需要根据提示进行扫码或滑块验证，如果得到以下提示则登录成功：

[![image.png](https://i.postimg.cc/26pZGRcM/image.png)](https://postimg.cc/f3KyWFhf)

## 相关文档

下面是`nonebot`提供的一些相关开发文档与api及event文档：

- https://docs.nonebot.dev/api/
- https://aiocqhttp.nonebot.dev/module/aiocqhttp/index.html
- https://docs.go-cqhttp.org/api/#%E5%9F%BA%E7%A1%80%E4%BC%A0%E8%BE%93
- https://docs.go-cqhttp.org/event/#%E9%80%9A%E7%94%A8%E6%95%B0%E6%8D%AE

## 配置及初步指南

环境的配置以及初步教程请参考`docs/基本配置与指南.md

## 贡献

如果你在使用过程中发现任何问题，可以 [提交 issue](https://github.com/nonebot/nonebot/issues/new) 或自行 fork 修改后提交 pull request。

如果你要提交 pull request，请确保你的代码风格和项目已有的代码保持一致，遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/)，变量命名清晰，有适当的注释。
`
