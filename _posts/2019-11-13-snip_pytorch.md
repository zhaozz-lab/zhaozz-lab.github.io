---
layout: post
title: "部分pytorch函数说明 "
categories: misc
---

# pytorch 部分函数的使用
## torch.nn.functional使用自定义卷积

```python
# 相等于用8个4*3*3的卷积核去和inputs进行卷积，output为输出的channels
filters = torch.randn(8,4,3,3)
inputs = torch.randn(1,4,5,5)
outputs = F.conv2d(inputs, filters, padding=1)
print(outputs.shape)
# torch.Size([1, 8, 5, 5])
```

## pytorch 计算非0值的索引
```python
    b = torch.tensor([[0,1,2],[0,1,2]])
    x = torch.eq(b,1)
    print(x.nonzero())
# tensor([[0, 1],
#        [1, 1]])
```