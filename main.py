# This is a sample Python script.
import queue
from sys import platform, version_info

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(version_info[0], version_info[1], version_info[2], sep='.')


def queue_check(size):
    # From class queue, Queue is
    # created as an object Now L
    # is Queue of a maximum
    # capacity of 20
    L = queue.Queue(maxsize=size)

    # Data is inserted into Queue
    # using put() Data is inserted
    # at the end
    L.put(5)
    L.put(9)
    L.put(1)

    # get() takes data_gmt out from
    # the Queue from the head
    # of the Queue
    L.get()
    L.get()
    L.get()
    L.put([{2,3,4,5},44,45,0])
    L.put(27)
    print(L.get()[::-1])
    print(L.all_tasks_done)
    print(L.qsize())


class StackCheck:
    MAXSIZE = 4
    stack = [None] * MAXSIZE
    top = -1

    def __init__(self, max_size):
        self.MAXSIZE = max_size
        self.stack = [None] * max_size

    def isfull(s):
        if s.top == s.MAXSIZE - 1:
            return True
        else:
            return False

    def push(self, data):
        if not self.isfull():
            self.top = self.top + 1
            self.stack[self.top] = data
        else:
            print("Could not insert data_gmt, Stack is full.")
    def get_top(s):
        return s.top

class SuperClass1:
    def info(self):
        print("Super Class 1 method called")

class SuperClass2():
    def __init__(self,a):
        self.a = a
    def info(self):
        print("Super Class 2 method called"," -- #method overrriding")
    def __add__(self, a): #operator overlaoding in python
        return "Sum is " + str(self.a + a.a) + " -- #perator verloading"

class Derived(SuperClass2):
    '''super keyword to call parent class things'''
    def __init__(self, a):
        super().__init__(a) #super for set parent data_gmt

d1 = Derived(3)
d2 = Derived(6)
print(d1+d2) #Operator verloading
d1.info()
print(d1.__module__.__getattribute__('split'))

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
        cls.project_name = "ABC Project"
    def work(self):
        self.changeitsdata()
        print("# call class method from instance method to change class's attribute")
        requirement = self.gather_requirement(self.project_name)
        print("# call static method from instance method for do something as normal function")
        for task in requirement:
            pass

emp = Employee('Kelly', 12000)
emp.work()
print(emp.project_name)



class GFG3(GFG2):
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG3)')
        super().__init__()

    def sub_GFG(self, b):
        print('Printing from class GFG3:', b)
        super().sub_GFG(b + 1)
    # Press the green button in the gutter to run the script.



if __name__ == '__main__':
    # print_hi('Santosh')
    queue_check(6)
    x = StackCheck(7)
    # x.push(1)
    # x.push(1)
    # x.push(1)
    # x.push(1)
    # x.push(1)
    # print(x.stack)
    a = "dsasdas d"
    b = "dsasdas d"
    c = 155
    d = 257
    # print(a[1::-1])
    print(id(d) == id(257))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
    obj = GFG3()
    GFG3.sub_GFG(obj,3)
    print(x.get_top())
