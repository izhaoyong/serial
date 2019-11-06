### 程序相关环境

- python：3.8.0

- serial：

    安装最新版本就可以。

    ```
    pip install pyserial
    ```

    



### 程序说明

```
import serial

with serial.Serial('COM3') as ser:
	while True:
		line = ser.readline()
		print(line)

```

其中**COM3**是本地串口的`名称`，实际运行时需要先指定本地的串口名称。在__`设备管理器`__中可以找到串口的名称。



### 问题

程序只能在所有情况都正常的情况下运行，所以会有很多bug。比如：

1. 错误捕获以及处理
2. 黑窗口运行，要退出程序只能关闭黑窗口