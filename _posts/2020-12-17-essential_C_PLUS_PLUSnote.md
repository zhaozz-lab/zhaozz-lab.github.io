---
layout: post
title: "essencial c++"
categories: Algorithm
---
# c++
## 1 编程基础
### 1.6 指针的使用
```c++
const int seq_cnt = 3;
vector<int> *seq_addrs[seq_cnt] = {&fib,&lucas,$pell};
```
### 1.7 文件的读写
```c++
#include <fstream>
ofstream outfile("seq_data.txt");
```

## 2 function
### 函数重载
一般而言，如果函数具备多种实现方式，我们可将它重载，其每份实例提供的是相同的通用服务。如果我们希望让程序代码的主体不变，仅仅改变其中用到的数据类型，可以通过function template实现。
函数重载的条件，参数类型不同，或者参数个数不同，只有返回值不同，不能作为函数重载。
```c++
template <typename elemType>
void display_message(const string &msg,const vector<elemType> &vec)
{
    cout<<message;


    for(int ix=0;i<vec.size();++ix){
        elemType t = vec[ix];
    }
}
```
function template 同时也可以是重载函数
```c++
template <typename elemType>
void display_message(const string &msg,const vector<elemType> &vec);

template <typename elemType>
void display_message(const string &msg,const list<elemType> &vec);
```
### 函数指针
```c++
int add(int x,int y ) {

	return x+y;
}

int* (*func)() = 0;

int testtime(int x,int y ,int (*func)(int,int)) {
	auto start = std::chrono::steady_clock::now();
	func(x, y);
	auto end = std::chrono::steady_clock::now();
	std::chrono::duration<double> elapsed = end - start;
	printf("the spend time is %f", elapsed.count());
	return -1;
}
```
 


## 3.泛型编程风格
### 泛型算法实现find
```c++
template <typename elemType>
elemType* find(const elemType* array, int size, const elemType& value) {

	if (!array || size < 1)
	{
		return 0;
	}
	for (int ix = 0; ix < size; ++ix) {
		if (array[ix] == value)
			return &array[ix];
	}
	return 0;
}


template <typename elemType>
elemType* find(const elemType* first, const elemType* last, const elemType& value) {

	if (!first || !last)
	{
		return 0;
	}
	for (; first != last;++first) {
		if (*first == value)
			return first;
	}
	return 0;
}


void test_pointer_algorithm() {
	int ia[8] = { 1,2,3,4,5,6,7,8 };
	float fa[8] = { 1,2,3,4,5,6,7,8 };
	char sa[4] = { 't','s','3','2' };
	
	int* pi = find(ia, ia + 8, ia[3]);
	int* pi0 = find(ia, ia + 8, 0);

	float* pf = find(fa, fa + 8, fa[3]);
	float* pf0 = find(fa, fa + 8, 0);

	char* ps = find(sa, sa + 4, sa[3]);
	char* ps0 = find(sa, sa + 4, 0);

}
```

### 3.6如何设计一个泛型算法
```c++
bool less_than(int v1, int v2) {
	return v1 < v2 ? true: false;
}

bool greater_than(int v1, int v2) {
	return v1 > v2 ? true: false;
}
//泛型算法
vector<int> filter(const vector<int>& vec, int filter_value, bool(*pred)(int, int)) {
	vector<int> nvec;
	for (int ix = 0; ix < vec.size(); ++ix)
		if (pred(vec[ix], filter_value))
			nvec.push_back(vec[ix]);
	return nvec;
}


void testfilter() {
	vector<int> input{ 1,2,3,4,5,6 };
	vector<int> output = filter(input, 3, less_than);
	//采用lambda表达式进行计算
	vector<int> output1 = filter(input, 3, [](int x, int y) {return x < y; });
}
```

## 4.基于对象的编程风格
### 4.3 mutable 和 const
```c++
class Triangular{
    int length() const {return length;}
    int beg_pos() const {return _beg_pos;}
    int elem(int pos) const;

    bool next(int &val);
    void next_reset(){
        _next = _beg
    }
}

```










