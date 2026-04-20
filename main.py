# This is a sample Python script.
from sys import platform, version_info
from abc import ABC, abstractmethod
from venv import create
import time
from functools import wraps

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(version_info[0], version_info[1], version_info[2], sep='.')


class GFG1:
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG1)')

    def sub_GFG(self, b):
        print('Printing from class GFG1:', b)

    # class GFG2 inherits the GFG1


class GFG2(GFG1):
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG2)')
        super().__init__()

    def sub_GFG(self, b):
        print('Printing from class GFG2:', b)
        super().sub_GFG(b + 1)

    # class GFG3 inherits the GFG1 ang GFG2 both


class GFG3(GFG2):
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG3)')
        super().__init__()

    def sub_GFG(self, b):
        print('Printing from class GFG3:', b)
        super().sub_GFG(b + 1)
    # Press the green button in the gutter to run the script.



if __name__ == '__main__':
    obj = GFG3()
    GFG3.sub_GFG(obj,3)




class SuperClass1:
    def info(self):
        print("Super Class 1 method called")

class SuperClass2():
    def __init__(self,a):
        self.a = a  

    def __add__(self, a): #operator overlaoding in python
        return "Sum is " + str(self.a + a.a) + " -- #perator verloading"

class Derived(SuperClass1, SuperClass2):
    '''super keyword to call parent class things'''
    def __init__(self, a):
        super().__init__(a) #super for set parent data member in child class    

print(Derived.mro(), "method resolution order in multiple inheritance", end="\n\n")

print("object is always the final class in the chain, The object class provides default methods like:__init__()__str__()__repr__()__hash__()__eq__()", end="\n\n")  

print("But SuperClass1 does not have __init__, so Python continues searching in the MRO")

d1 = Derived(3)
d2 = Derived(6)
print(d1+d2) #Operator verloading
print(d2.a)
print(d1.__module__.__getattribute__('split'))


#static and class method
class Employee(object):
    name, salary, project_name = "santosh singh", 12222, "metswift"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @staticmethod
    def gather_requirement(project_name):
        if project_name == 'ABC Project':
            requirement = ['task_1', 'task_2', 'task_3']
        else:
            requirement = ['task_1']
        return requirement

    # instance method
    @classmethod
    def changeitsdata(cls):
        cls.project_name = "ABC Project1"

    def work(self):
        print("# call class method from instance method to change class's attribute")
        self.changeitsdata()
    
        print("# call static method from instance method for do something as normal function without any self or cls parameter", end="\n\n")
        requirement = self.gather_requirement(self.project_name)
        for task in requirement:
            pass

emp = Employee('Kelly', 12000)
emp.work()
print(emp.project_name)
print(Employee.gather_requirement("ABC"))



# Multiple Inheritance left to right method resolution order
class A:
    def show(self):
        print("A - method overriding in class A left to right method resolution order")

class B:
    def show(self):
        print("B - method overriding in class B left to right method resolution order", end="\n\n")

class C(A, B):
    pass

class D(B, A):
    pass

obj, obj1 = C(), D()
 
obj.show()
obj1.show()




#create a abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        print("Area of shape is calculated")
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius 
    
    def area(self,x=9):
        return 3.14 * self.radius * self.radius 


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    
circlearea1 = Circle(5)
rectanglearea1 = Rectangle(5, 10)
print(circlearea1.area(), rectanglearea1.area()) # this will give error as area is not implemented in shape class



# DECORATOR BASICS AND ADVANCED CONCEPTS

# 1. BASIC DECORATOR - Function wrapper
def simple_decorator(func):
    def wrapper():
        print("Something before function call")
        func()
        print("Something after function call")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

say_hello()

print("\n" + "="*50 + "\n")

# 2. DECORATOR WITH ARGUMENTS to wrapped function
def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@decorator_with_args
def add(a, b):
    return a + b

print(add(5, 3))
print("\n" + "="*50 + "\n")

# 3. DECORATOR WITH ITS OWN PARAMETERS
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"Execution {i+1}:")
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
print("\n" + "="*50 + "\n")

# 4. TIMER DECORATOR - measure execution time
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(1)
    print("Function executed")

slow_function()
print("\n" + "="*50 + "\n")

# 5. LOGGING DECORATOR
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"LOG: Function '{func.__name__}' called")
        print(f"LOG: Arguments: {args}, Keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"LOG: Function '{func.__name__}' returned {result}")
        return result
    return wrapper

@logging_decorator
def multiply(x, y):
    return x * y

multiply(4, 5)
print("\n" + "="*50 + "\n")

# 6. CHAINING MULTIPLE DECORATORS
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclamation_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!!!123"
    return wrapper

@exclamation_decorator
@uppercase_decorator
def get_message():
    return "hello world"

print(get_message())
print("\n" + "="*50 + "\n")

# 7. CLASS-BASED DECORATOR
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Function called {self.count} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    print("Hi!")

say_hi()
say_hi()
say_hi()
print("\n" + "="*50 + "\n")

# 8. DECORATOR PRESERVING FUNCTION METADATA (using functools.wraps)

def preserve_metadata(func):
    @wraps(func)  # Preserves original function's metadata
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@preserve_metadata
def documented_function():
    """This function has documentation"""
    return "Result"

print(f"Function name: {documented_function.__name__}")
print(f"Documentation: {documented_function.__doc__}")


