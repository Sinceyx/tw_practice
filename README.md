# tw_practice

语言版本：Python 3.8.2
入职第一周的练习项目，主要用于熟悉python的基础语法及语言规范。

### 目录结构说明

- `src` 目录存放需求实现代码
- `tests` 目录存放单元测试代码
- `resource` 目录存放代码中依赖的非代码文件


### 主体介绍
从功能上分为三部分：
- hello_world
- extractor
- spider

***hello_world*** 自不必说。

***extractor*** 中使用了 [jq](https://github.com/mwilliamson/jq.py) 库， jq 的典型使用方法：`jq.compile(".").input("hello").first() == "hello"`，其中把要查找的关键字jq_path前置，把待查对象放在后面，比较特殊，让人印象深刻。

***spider*** 爬取一个固定网页 https://www.atrealty.com.au/buy/ 上的前5项产品数据，根据其返回确定真实获取数据的请求地址。依据获得地址，再去请求需要的数据集合，使用 extractor 中的函数对数据做解析，抽取目标数据。

### 单元测试

目前使用的python版本3.8中，unittest集成了mock，复杂的测试可以使用mock及patch。
