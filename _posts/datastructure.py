#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#冒泡排序的思想：
#比较相邻的元素，如果是逆序，则交换
# bubble
def bubble(a):
    ret = False
    while(not ret):
        for i in range(0,len(a)-1):
            if a[i] >a[i+1]:
                ret = True
            else:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                ret = False
    return a,ret


a = [0,5,32,58]
print(bubble(a))


#迭代与递归
#迭代
def sum(a):
    sum = 0
    for i in a:
        sum += i
    return sum
a = [0,5,32,58]
print(sum(a))

#递归
def sum_recursion(a,n):
    return 0 if n <1 else sum_recursion(a,n-1)+a[n-1]


# 二分递归
def sum_binary_recursion(a,lo,hi):
    if (hi-lo<2):
        return a[lo]
    mi = (lo+hi)>>1
    return sum_binary_recursion(a,lo,mi) + sum_binary_recursion(a,mi,hi)

b = [0,1,2,3]
print(b[0])
print(sum_recursion(b,4))
print(sum_binary_recursion(b,0,4))



#任意给子序列，求其中和最大的序列
## 暴力求解
def gs_BF(a):
    gs = a[0]
    for i in range(0,len(a)):
        for j in range(1,len(a)):
            s = 0
            for k in range(i,j):
                s += a[k]
            if s>gs:
                gs=s
    return gs
a = [1,2,-3,4]
print(gs_BF(a))
            
# 增量策略，计算从0-n,1-n,2-n 中间如果有负数，并不会更新gs的值
# incremental strategy
def gs_IC(a): 
    gs = a[0]
    for i in range(0,len(a)):
        s = 0
        for j in range(i,len(a)):
            s += a[j]
            if gs < s:
                gs = s
                
    return gs

a = [1,2,-3,4,6]
print(gs_BF(a))


# i=100
# print(i-1)
# print(i-1)
# print(i-1)


# ## 采用分而治之的策略
def gs_DC(a,lo,hi):
    if(hi-lo)<2:
        return a[lo]
    mi = int((lo+hi)/2)
    gsl = a[mi-1]
    sl = 0
    i = mi
    while lo<i-1:
        sl += a[i]
        if gsl < sl:
            gsl = sl
        i -= 1
    gsR = a[mi]
    sR = 0
    j = mi - 1
    while j+1 < hi:
        sR += a[j]
        if gsR < sR:
            gsR = sR
        j += 1
    return max(gsl+gsR,max(gs_DC(a,lo,mi),gs_DC(a,mi,hi)))
        
a = [1,2,-3,4,6]
print(gs_DC(a,0,4))


# def gs_LS(a,n):
#     gs,s,i,j = a[0],0,n-1,n
#     while 0<i:
#         s += a[i]
#         pass




# 在vector中，所有数据项的物理存放地址与逻辑次序完全重合，此时的逻辑次序也称为秩(rank)
# 在list中，逻辑上相邻的数据项物理上未必相邻，采用间接寻址的方式通过封装后的位置相互引用
# a = ['test']
# a.extend([1,2,3])
# print(a)
a = {}
a[(1,2)] =3
a[(2,2)] =4
a[(2,4)] =6
print(a)