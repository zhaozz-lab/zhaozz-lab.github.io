# pytorch 不常用函数的使用
## torch.nn.functional使用自定义卷积

```
# 相等于用8个4*3*3的卷积核去和inputs进行卷积，output为输出的channels
filters = torch.randn(8,4,3,3)
inputs = torch.randn(1,4,5,5)
outputs = F.conv2d(inputs, filters, padding=1)
print(outputs.shape)
# torch.Size([1, 8, 5, 5])
```