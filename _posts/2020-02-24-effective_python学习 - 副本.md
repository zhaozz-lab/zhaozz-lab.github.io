---
layout: post
title: "Effective python阅读笔记"
categories: Python
---
# Effective Python 阅读笔记
## enumulate的使用
可以用enumulate来代替range,enumulate的第二个参数可以指定索引的起始点
```python
a = ['a','b','c']
for i,name in enumerate(a):
    print(i,name)

for i,name in enumerate(a,1):
    print(i,name)
```

