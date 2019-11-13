import torch
import torch.nn.functional as F
# convolution test
filters = torch.randn(8,4,3,3)
inputs = torch.randn(1,4,5,5)
outputs = F.conv2d(inputs, filters, padding=1)
print(outputs.shape)

# Simance net using 
filters = torch.randn(16,256,6,6)
inputs = torch.randn(1,16*256,22,22)
outputs = F.conv2d(inputs, filters,groups=16)
print(outputs.shape)