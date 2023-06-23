# Python 3 Object Oriented Programming
this notes has been created based on [Python 3 Object Oriented Programming](https://learning.oreilly.com/library/view/python-3-object/9781849511261/), thanks the author [Dusty Phillips](https://dusty.phillips.codes/)

## oops 

### Composition

```python
class Car:
    def __init__(self, engine):
        self.engine = engine

    def drive(self):
        self.engine.start()
        self.engine.run()
        self.engine.stop()

class Engine:
    def start(self):
        print("Engine started")

    def run(self):
        print("Engine running")

    def stop(self):
        print("Engine stopped")

```

### Inheritance

```python

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print("I am a", self.species)

class Dog(Animal):
    def wag_tail(self):
        print("Wagging tail")


```

### Aggregation

```python

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def print_address(self):
        print(self.address)

class Address:
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code


```

### Association

```python
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def place_order(self, order):
        self.orders.append(order)

class Order:
    def __init__(self, customer, product, quantity):
        self.customer = customer
        self.product = product
        self.quantity = quantity
```


### Polymorphism

```python
class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

def make_animal_sound(animal):
    animal.make_sound()

dog = Dog()
cat = Cat()

make_animal_sound(dog)
# Output: Woof!

make_animal_sound(cat)
# Output: Meow!

```

### multiple inheritance 

```python
class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class Bird(Animal):
    def make_sound(self):
        print("Tweet!")

class Hybrid(Dog, Cat, Bird):
    pass

hybrid = Hybrid()

hybrid.make_sound()

```


### interface 


### Multiple inheritance

#### the diamond problem

consider about use __mro__(method resolution order)


### Polymorphism

#### duck typing


## Exception

### raising an exception

```python

class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super().append(integer)


```

### handling exceptions

```python

def funny_division(anumber):
    try:
        return 100 / anumber
    except ZeroDivisionError:
        return "Silly wabbit, you can't divide by zero!"

print(funny_division(0))
print(funny_division(50.0))
print(funny_division("hello"))

```

![exception] (exception.jpg)


```python

item_type = 'widget'
inv = Inventory()
inv.lock(item_type)
try:
    num_left = inv.purchase(item_type)
except InvalidItemType:
    print("Sorry, we don't sell {}".format(item_type))
except OutOfStock:
    print("Sorry, that item is out of stock.")
else:
    print("Purchase complete. There are "
            "{} {}s left".format(num_left, item_type))
finally:
    inv.unlock()

```

this same code could be written with an if..elif..ekse structure, but i wouldn't be as easy to read or maintain. Using exceptions for flow control can make for some handy program designs


## python data strctures

### empty objects

### tuples and named tuples


### dictionaries


### Lists


### Sets


## python build-in functions

### len()

### reversed()

### enumerate()


### zip()

### sorted()


### sort()


## comprehensions

### list comprehensions

### dic and set comprehensions

### generator expressions


## arguments

### unpacking arguments

```python
def show_args(arg1, arg2, arg3="THREE"):
    print(arg1, arg2, arg3)

some_args = range(3)
more_args = {
        "arg1": "ONE",
        "arg2": "TWO"}

print("Unpacking a sequence:", end=" ")
show_args(*some_args)
print("Unpacking a dict:", end=" ")
show_args(**more_args)
```

``` bash
Unpacking a sequence: 0 1 2
Unpacking a dict: ONE TWO THREE
```
\* operator for list
\*\* operator for collection


## functions are objects

### use functions as attributes


## Python Design patterns

### structure pattern
#### decorator pattern

allows us to dynamically add functionality to classes without creating subclasses and affecting the behavior of other objects of the same class. by suing the decorator pattern, we can easily generate different permutations of functionality that we might want without creating an exponentially increasing number of sublcasses, making our code increasingly complex and bloated

1. enhancing the response of a component that is sending data to a second component
2. supporting multiple optional behaviors


function decorators 

```python
# function decorator that calls the function twice
def repeat_decorator(fn):
    def decorated_fn():
        fn()
        fn()
    # returns a function
    return decorated_fn
 
# using the decorator on hello_world function
@repeat_decorator
def hello_world():
    print ("Hello world!")
 
# call the function
hello_world()

```

hello_world = repeat_decorator(hello_world)



### behavior pattern

#### observer pattern


observer pattern is useful for state monitoring and event handling situations.

a single core object can be monitored by an unknown or array of observer objects.



#### strategy pattern

strategy pattern implements different solutions to a single problem each in a different object. the client code can then choose the most appropriate implementation dynamically at runtime

##### state pattern

it is similar to strategy pattern, the goal of the state pattern is to represent state-transition systems: systems where it is obvious that an object can be in a specific state, and that certain activities may drive it to a different state.

state vs strategy

state pattern looks very similar to strategy pattern, indeed the UML diagrams for the two are identical. 

but strategy is used to choose an algorithm at runtime; generally, only one of those algorithms is going to be chosen for a particular use case.
the state pattern, on the other hand is designed to allow switching between different states dynamically

#### singleton pattern

one of most controversial patterns, a pattern that should be avoided, not promoted.

#### template pattern

is used for removing duplicate code; 

#### adapter pattern
is designed to interact with existing code
for matching interfaces
#### facade pattern
is designed to provide a simple interface to a complex system of componenets

for simplifying complex systems

#### flyweight pattern

is a memory optimization pattern

#### command pattern
for isolating invokers
#### abstract factory pattern
is normally used when we have multiple possible implementations of a system that depend on some configuration or platform issue.

Common examples of the abstract factory pattern at work include code for operating system independent toolkits, database backends, and country-specific formatters or calculators

for separating implementation

#### composite pattern
allow complex tree-like structures to be buit from simple components

for tree-like structures


## Files and String

### string manipulation


```python
s = "hello world"
s.startswith('hi')
False
s.endswith('ld')
True
s.find('l')
2
s.index('m')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found


s = "hello world, how are you"
s2 = s.split(' ')
s2
['hello', 'world,', 'how', 'are', 'you']
'#'.join(s2)
'hello#world,#how#are#you'
s.replace(' ', '**')
'hello**world,**how**are**you'
s.partition(' ')
('hello', ' ', 'world, how are you')


```

### string formatting

```python

template = "Hello {}, you are currently {}."
print(template.format('Dusty', 'writing'))

>> Hello Dusty, you are currently writing.


template = "Hello {0}, you are {1}. Your name is {0}."
print(template.format('Dusty', 'writing'))

```

### escaping braces

```python

template = """
public class {0} {{
    public static void main(String[] args) {{
        System.out.println({1});
    }}
}}"""

print(template.format("MyClass", "print('hello world')"));


```


### keyword arguments


```python
template = """
From: <{from_email}>
To: <{to_email}>
Subject: {subject}

{message}"""
print(template.format(
    from_email = "a@example.com",
    to_email = "b@example.com",
    message = "Here's some mail for you. "
    " Hope you enjoy the message!",
    subject = "You have mail!"
    ))

```


### container lookups


```python
emails = ("a@example.com", "b@example.com")
message = {
        'subject': "You Have Mail!",
        'message': "Here's some mail for you!"
        }
template = """
From: <{0[0]}>
To: <{0[1]}>
Subject: {message[subject]}
{message[message]}"""
print(template.format(emails, message=message))

```


### object lookups


```python

class EMail:
    def __init__(self, from_addr, to_addr, subject, message):
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.subject = subject
        self.message = message

email = EMail("a@example.com", "b@example.com",
        "You Have Mail!",
         "Here's some mail for you!")

template = """
From: <{0.from_addr}>
To: <{0.to_addr}>
Subject: {0.subject}

{0.message}"""
print(template.format(email))

```

### storing objects

python pickle module


```python
import pickle

some_data = ["a list", "containing", 5,
        "values including another list",
        ["inner", "list"]]

with open("pickled_list", 'wb') as file:
    pickle.dump(some_data, file)

with open("pickled_list", 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
assert loaded_data == some_data

```


### summary

1. bytes vs str
2. mutable bytearrays
3. context managers and the "with" statement
4. serializing data with pickle and json


## Testing object-oriented programs


### TDD


1. The first is to ensure that tests really get written. and we'll know in the future if it is ever broken by a change we, or someone else has made
2. Secondly, writing tests first forces us to consider exactly how the code is going to be interacted with. It tells us what methods we need objects to have and how attributes will be accessed

### Unit testing

discover module 

### ingnoring broken tests

expextedFailure()
skip(reason)
skipIf(condition,reason)
skipUnless(condition,reason)

```python
import unittest
import sys

class SkipTests(unittest.TestCase):
    @unittest.expectedFailure
    def test_fails(self):
        self.assertEqual(False, True)

    @unittest.skip("Test is useless")
    def test_skip(self):
        self.assertEqual(False, True)

    @unittest.skipIf(sys.version_info.minor == 1,
            "broken on 3.1")
    def test_skipif(self):
        self.assertEqual(False, True)

    @unittest.skipUnless(sys.platform.startswith('linux'),
            "broken on linux")
    def test_skipunless(self):
        self.assertEqual(False, True)

if __name__ == "__main__":
    unittest.main()    

```


### pytest

pytest support setup and teardown methods in unittest

```python

def setup_module(module):
    print("setting up MODULE {0}".format(
        module.__name__))

def teardown_module(module):
    print("tearing down MODULE {0}".format(
        module.__name__))

def test_a_function():
    print("RUNNING TEST FUNCTION")

class BaseTest:
    def setup_class(cls):
        print("setting up CLASS {0}".format(
            cls.__name__))

    def teardown_class(cls):
        print("tearing down CLASS {0}\n".format(
            cls.__name__))

    def setup_method(self, method):
        print("setting up METHOD {0}".format(
            method.__name__))

    def teardown_method(self, method):
        print("tearing down  METHOD {0}".format(
            method.__name__))

class TestClass1(BaseTest):
    def test_method_1(self):
        print("RUNNING METHOD 1-1")

    def test_method_2(self):
        print("RUNNING METHOD 1-2")

class TestClass2(BaseTest):
    def test_method_1(self):
        print("RUNNING METHOD 2-1")

    def test_method_2(self):
        print("RUNNING METHOD 2-2")

```
pytest -k arguments can run single methods 


### code coverage

```bash

>> coverage run coverage_unittest.py

>> coverage report


The output is as follows:

Name                           Stmts   Exec  Cover
--------------------------------------------------
coverage_unittest                  7      7   100%
stats                             19      6    31%
--------------------------------------------------
TOTAL                             26     13    50%


coverage html

```

bear in mind that while 100% code coverage is a lofty goal that we should all strive for, but 100% is not enough!

## commonn Libraries

### user interfaces

1. pyQt

### XML
1. lxml



# fluent Python

## emulating numeric type

