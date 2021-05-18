# 关于学习行为数据可视化！
本代码库浙江工业大学张歌斐《在线学习数据的交互式可视分析》毕业论文学习行为数据可视化网站。

网页首页：[production文件夹][index]；
前端框架：[Colorlib](https://colorlib.com)



# 安装Python-Flask
为大家提供的框架本身搭建非常简单，即使用Python-Flask构建。
Python的安装请参考[官方网站][pythonweb]，安装后请打开命令行，输入如下命令安装服务器端需要的flask库：
```
pip install flask flask_cors
```
如果安装成功，即可直接运行服务器。

# 启动服务器
进入项目根目录（包含main.py的目录），打开命令行并输入如下指令：
```
python main.py
```
若出现如下类似的信息则表示服务器启动成功：
```
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 331-382-827
 * Running on http://0.0.0.0:11666/ (Press CTRL+C to quit)
```

# 示例导航
* 操控SVG：[链接][control]
* 柱状图：[链接][barchart1]
* 柱状图，图元可交互：链接
* 堆叠柱状图：[链接][stackbarchart]
* Path：[链接][htmlpath]
* 折线图，带上下浮动动画：[链接][linechart]
* 动态气泡图：[链接][scatter1]
* 静态主题河流：[链接][themeriver]
* 动态主题河流与柱状图，从左到右逐渐展现流动过程，柱状图同时随主题河流发生改变：[链接][themeriverlr]
* 世界地图与交互：[链接][mapinteract]
* 力（Force）、节点（Node）与边（Link）：[链接][force]
* 力跟随：[链接][force-following]

# Acknowledgement

首先，非常感谢MOOC平台所提供的数据集，目前只针对部分数据进行了路径可视化呈现，后续的分析讲继续挖深....
感谢指导过我的教课学院的老师们，感谢你们提出的宝贵意见！
该网页非常的简单，一方面是作者技术限制，另一方面也是时间有限，作者对学习行为数据的可视化非常感兴趣，若您也感兴趣可继续关注，也欢迎提出宝贵意见。


