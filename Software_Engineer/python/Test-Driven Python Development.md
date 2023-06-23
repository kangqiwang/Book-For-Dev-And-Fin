# Test-Driven Python Development

this notes has been created based on [Test-Driven Python Development](https://learning.oreilly.com/library/view/test-driven-python-development/9781783987924/), thanks the author [Dusty Phillips](https://www.playfulpython.com/)

## unit testing

testing a single unit of code, isolated from other code that it might be integrated with.

## integration test
 involves exercising more than one unit of the system. the goal is to check whether these units have been integrated correctly. A typical integration test might be to go to a web page,fill in a form, and check whether the right message is displayed on the scr

## mock method and 

assert_called(*args, **kwargs) 断言mock至少被调用一次
assert_called_once(*args, **kwargs) 断言mock调用仅一次
assert_called_with(*args, **kwargs) 断言mock以某种参数至少调用一次
assert_called_once_with(*args, **kwargs) 断言mock以某种参数调用仅一次
assert_any_called(*args, **kwargs) 断言mock以某种参数曾经被调用过，区别与上面的assert_called_with()与assert_called_once_with()必须是最近的那次调用符合断言
assert_has_calls(calls, any_order=False) 断言mock被按照的特定一组调用的方式调用过。如果any_order是False，那么必须满足calls中的调用，而且必须是连续的，如果any_order是True，那么就只需要执行了calls中的调用就可以了
assert_not_called() 断言没有被调用
reset_mock(*args, return_value=False, side_effect=False) 重置mock对象的所有调用
attach_mock() 将mock附加在mock对象的属性上
called mock是否被调用的值
call_count 调用次数
return_value 设置mock的返回值
side_effect 可以设置为特定的方法，迭代器或者一个异常。设置为None可以取消side_effect的影响
call_args 最后调用的参数
__class__ 指定mock的类型，支持isinstance()判断

MagicMock 是Mock类的子类，与Mock相比，默认实现了大部分的魔术方法
NonCallableMock 是不可调用的Mock类，适合模拟模拟不可调用的类对象
NonCallableMagicMock 是不可调用的MagicMock类


## PDB debugging
Some common pdb commands
Most of the time, we will use the following commands:

s: This executes one line of code (going inside a function call if required)
n: This executes code until you reach the next line in the current function
r: This executes code until the current function returns
q: This quits the debugger
b: This sets a breakpoint on a particular line of a file
cl: This clears breakpoints
c: This continues execution until a breakpoint is encountered or until the end of execution


