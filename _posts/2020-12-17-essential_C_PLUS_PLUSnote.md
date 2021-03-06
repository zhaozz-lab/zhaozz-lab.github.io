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

### 4.5 静态类成员
member function只有在“不访问任何non-static member”的条件下才能声明为static，声明方式是在声明之前加上关键字static；
```c++
static is_elem();
```

### 4.6 打造一个 Iteror class
* 运算符重载的规则：
* 不可以引入新的运算符，除了 . .* :: ?:,其他的运算符都可以被重载
* 运算符的操作数（operand）个数不可改变。每个二元运算符都需要两个操作数，每个一元都需要恰好一个操作数，因此，我们无法定义出一个equality运算符，并令他接受两个以上或者两个一下的操作数。
* 运算符的优先级不可以改变
* 运算符的参数列表中，必须至少一个参数为class类型，也就是说，我们无法为诸如，指针之类的non-class 类型，重新定义其原已经存在的运算符。 
```c++
inline int Triangular_iterator::
operator*() const
{
check_integrity();
return Triangular::_elems[_index];
}

```
也可以像non-member function 一样

```c++
inline int 
operator*(const  Triangular_iterator &rhs) const
{
rhs.check_integrity();
//注意，如果这是一个non-member function,就不具有访问non-public member的权力
return Triangular::_elems[_index];
}

```










