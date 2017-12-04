// auto_ptr example
#include <iostream>
#include <memory>
#include <vector>
class A{

public:
    A(){std::cout<<"A const"<<std::endl; a  =0;};
    A(const A& ra)
    {
std::cout<<"A copy"<<std::endl;
    }
    A& operator =(const A& ra)
    {
        std::cout<<"A ="<<std::endl;
    }

    int a;
};

A getA()
{
    A a;
    a.a = 1;
    int b = 1;
    std::cout<<"point a %x"<<&a<<&b<<std::endl;
    return a;
}

int main () {
    A a = getA();
     std::cout<<"point a %x"<<&a<<std::endl;
    A b = a;
     std::cout<<"point a %x"<<&b<<std::endl;
    std::cout <<a.a;
  std::auto_ptr<int> p1 (new int);
  *p1.get()=10;
  
//   std::auto_ptr<int> p2 (new int);
//   *p2.get()=10;
//   std::vector<std::auto_ptr<int> > vec;
//   vec.push_back(p1);

  std::auto_ptr<int> p2 (p1);

  std::cout << "p2 points to " << p1.get() << '\n';
  // (p1 is now null-pointer auto_ptr)

  return 0;
}

// A const
// point a %x0x61cc5c0x61cc2c
// point a %x0x61cc5c
// A copy
// point a %x0x61cc58
// 1p2 points to 0