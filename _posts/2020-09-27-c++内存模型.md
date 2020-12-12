---
layout: post
title: "c++内存模型"
categories: Algorithm
---
# C++内存模型
## 1.对象课程
### 进行封装的布局损失
#### c的实现
 在c语言中，一个数据抽象和操作是分开的,没有一种语言支持数据和函数之间的关系，称这种方法为面向过程的方法。
```c
//data
typedef struct point3d
{
    float x;
    float y;
    float z;
} Point3d;
```
```c
//operator
void Pointed_print(const Point3d *pd)
{
    printf("(%g,%g,%g)",pd->x,pd->y,pd->z);
}
```

```c
//more efficiency,could define macro
#define Point3d_print(pd) printf("(%g,%g,%g)",pd->x,pd->y,pd->z);
``` 
#### c++的实现   
在c++中的实现
```c++
class Point3d
{
public:
    Point3d(float x= 0.0,float y = 0.0,float z=0.0):_x(x),_y(y),_z(z){}
    float x(){ return _x;}
    float y(){ return _y;}
    float z(){ return _z;}

    void x(float xval){_x= xval;}
private:
    float _x;
    float _y;
    float _z;

inline ostream&
operator<<(ostream &os,const Point3d &pt)
{
    os<<"("<<pt.x()<<","<<pt.y()<<","<<pt.z()<<")"
}
}
```
或者通过两级或者三级的类结构实现
```c++
class Point{
    public:
        Point(float x= 0.0):_x(x){}
        float x(){return _x};
    protected:
        float _x;
}

class Point2d:public Point
{
    public:
    Point2d(float x=0.0,float y = 0.0):Point(x),_y(y){}

    float y(){return _y;}
    void y(float yval){_y = yval;}
    protected:
    float _y;
}

class Point3d:public Point2d
{
    public:
    Point3d(float x =0.0,float y=0.0,float z = 0.0):Point2d(x,y),_z(z){}
    float z(){return _z;}
    void z(float zval)
    {
        z=zval;
    }
    protected:
    float _z;
}
```
而且，这些类的执行可以参数化，根据坐标的类型去确定。
```c++
template <clsse type>
class Point3d{
    public:
    Point3d(type x=0.0,type y = 0.0,type z= 0.0):_x(x),_y(y),_z(z){}
    type x(){return _x;}
    void x(type xval){
        _x = xval;
    }

    private:
    type _x;
    type _y;
    type _z;
    
};
```
或者类型和坐标数都可以指定
```c++
template <clsse type,int dim>
class Point{
    public:
    Point();
    Point(type coords[dim]){
        for(int index=0;index < dim;index++)
        _coords[index] = coords[index];
    }

    type &operator[](int index){
        assert(index<dim && index > 0);
        return _coords[index];
    }
//const 的作用 1.函数体内，不能对类的数据成员作任何改动，2.一个const型类对象，只能调用const类型的函数 \
3.在const成员函数中,调用其他非const成员函数时非法的。
    type operator[](int index) const //
    {
        assert(index<dim && index > 0);
        return _coords[index];
    }

private:
type _coords[dim];
};

inline
template <class type ,int dim>
ostream&
operator<<(ostream &os,const Point<type,dim> &pt)
{
    os<<"(";
    for(int ix=0;ix<dim-1;ix++)
    os<<pt[ix]<<","
    os<<pt[dim-1];
    os<<")";
}




```
主要的布局损失是跟虚函数相关。

### c++对象模型
* 非静态数据直接分配在每一个类对象内
* 静态数据存储在各个类对象的外部
* 静态和非静态的成员函数存储在类桂香的外部
* 虚函数支持以下两个步骤 1. 每个类生成一个虚函数指针列表，2. 指向相关虚拟表的指针插入每一个类对象中。通过在每个类的构造，析构，拷贝赋值操作，去自动处理设置，重新设置，不设置。在虚拟表中（通常在表的第一个插槽中）也处理了与支持类型识别（RTTI）的每个类相关联的type_info对象。
C++对象模型的主要优势是它的空间和runtime运行效率。它的缺点是需要重新编译未修改的代码，该代码利用已对非静态数据存储器进行了添加，删除或修改的类的对象进行编译。
例如，两个表模型通过提供额外的间接访问从而提高了模型的灵活性，但它是以空间和运行时的效率为损失的。

```c++
class Point
{
public:
Point(float xval);
virtual ~Point();
float x() const;
static int PointCount();

protected:
   virtural ostream& print(ostream &os) const;
   float _x;
   static int _point_count;
};
```

#### 添加继承
单继承
```C++
class Library_materials {...};
class Book:public Library_materials {...};
class Rental_book:public Book {...};
```
多继承
```C++
class iostream:public istream,public ostream{...};
```
更重要的是，继承可以指定为虚继承
```c++
class istream:virtual public ios{...};
class ostream:virtual public ios{...};
```
在虚继承的情况下，无论该继承类在继承链中派生了多少次，都仅维护一次单个的base类。例如，iostream仅包含虚拟ios基类的一个实例。
##### 派生类如何对其内部的基类实例进行建模？
在一个简单的基类对象里，基类会在每一个派生类中分配一个插槽，每一个槽保存着基类的地址。
该方案的缺点主要是间接访问的空间和时间开销。好处是类对象的大小不受其相关基类大小的更改的影响。











