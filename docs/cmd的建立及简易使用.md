#**在桌面上建立`cmd.exe`的快捷方式**

1.桌面空白处右键 - 新建 - 快捷方式

[![image.png](https://i.postimg.cc/PxYPHXhQ/image.png)](https://postimg.cc/S2Qy7pnn)

2.出现的对话框中输入cmd，按"下一步"

[![image.png](https://i.postimg.cc/fRPL0tRv/image.png)](https://postimg.cc/SnWqBK8X)

3.输入该快捷方式的名称，按"完成"

[![image.png](https://i.postimg.cc/4xVMpjJF/image.png)](https://postimg.cc/5X9nV7Qw)

4.桌面出现cmd.exe图标

[![image.png](https://i.postimg.cc/QNKqB1Nf/image.png)](https://postimg.cc/MXxBNcQB)


#**设置启动cmd.exe快捷方式后缺省进入指定目录**

1.在cmd.exe快捷方式上右键 - 属性

[![image.png](https://i.postimg.cc/wTLMsTmK/image.png)](https://postimg.cc/Vdsmxwg4)


2.出现的对话框中，将"起始位置"改为指定目录，按"确定"

[![image.png](https://i.postimg.cc/yYm68QMs/image.png)](https://postimg.cc/jLjY8XqF)

此后打开cmd即可进入指定目录（可建立多个cmd,方便直接进入不同的目录）

#**cmd基础指令**

1.手工输入命令，进入任意目录的方法
  - 出现的cmd窗口中，输入[`D:`],按回车,即可进入d盘
  
  - [![image.png](https://i.postimg.cc/NGbpvBMc/image.png)](https://postimg.cc/xqJKKrMx)
  
  - 出现[`D:\>`]后，再输入[`cd d:\test\debug`],按回车即可进入根目录
  
  - [![image.png](https://i.postimg.cc/Kcdr2j2C/image.png)](https://postimg.cc/bd920zdR)
 
 2.
 - 可用<以及>进行输入输出重定向，以及使用管道运算符|将前一个程序的输出当做后一个程序的输入
