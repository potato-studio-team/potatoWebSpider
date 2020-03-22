# PotatoWebSpider应用开发文档

## PotatoStudio

### 欢迎使用子雨网页爬虫制作工具



#### 工具的介绍

子雨网页爬虫工具是一个主要使用python语言编写的面相于对计算机感兴趣的普通用户和入门程序员编写和测试简单地网站网页爬虫。此工具是一个工具集，可以使用特定的代码调用并执行，类似:

```posp
title=My first spider
url&get=http://www.potatost.xyz
file&new=result.txt
file&writeValue=textWeb
```

新建一个文件，随意命名为<u>**test.posp**</u>将上面这部分代码写入，保存文件，打开工具，输入go ，再输入你创建文件的路径。比如:E:\\\test.posp，点击回车。结果如下:

```psop
请输入子雨爬虫配置文件XXX.posp位置
>>>test.posp
My first spider
正在抓取http://www.potatost.xyz......
##抓取成功##
##网站抓取内容信息已写入##
```

网页内容已经抓取到了软件根目录的**result.txt**文件

#### posp语言介绍

posp是PotatoStudio开发的本工具中工具调用的表达语言，所有的爬虫工具调用都要使用posp语言表达。语言格式如下：

**key=value**(key = 键--工具代码; value = 值--参数)
`file&new=E:\\hello.posp` (调用file包的new工具，在E盘创建子雨网页爬虫配置文件hello.posp)



## posp代码说明：

### 一、文字展示

```posp
title=[文字]------显示一段[文字]
```

### 二、爬虫基本操作

#### 1.爬虫获取网页

```
url&get=http://www.potatost.xyz
```

