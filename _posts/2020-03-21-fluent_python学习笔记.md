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





