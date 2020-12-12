---
layout: post
title: "Effective python阅读笔记"
categories: Python
---
# Fluent Python 阅读笔记
## 装饰器的使用
```python
registry = []
def register(func):
    print('running register (%s)'%func)
    registry.add(func)
    return func
@register
def f1():
    print('running f1()')
@register
def f2():
    print('running f2()')
    
def f3():
    print('running f3()')
```



## enumulate的使用
可以用enumerate来代替range,enumerate的第二个参数可以指定索引的起始点
```python
a = ['a','b','c']
for i,name in enumerate(a):
    print(i,name)

for i,name in enumerate(a,1):
    print(i,name)
```




