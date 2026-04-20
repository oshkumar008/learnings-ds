import time
from threading import Thread
from multiprocessing import Process

def main():
    hello_obj = Hello()
    hello_hi = Hi()
    hello_obj.start()
    time.sleep(0.2)
    print("Main thread is running") 
    hello_hi.start()
    func_hello = Thread(target=hello)
    func_hi = Thread(target=hi)
    func_hello.start()
    time.sleep(0.2)
    print("Main thread is running") 
    func_hi.start() 
    func_hello.join()
    func_hi.join()
    print("Main thread is running") 

    start_time = time.time()
    calculate_sum(1, 2000000)
    end = time.time()
    print("Time taken by single thread: ", end - start_time)


    start_time = time.time()
    t1 = Thread(target=calculate_sum, args=(1, 1000000))
    t2 = Thread(target=calculate_sum, args=(1000001, 2000000))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Main thread is running")
    end = time.time()
    print("Time taken by threads: ", end - start_time)

    start_time = time.time()

    t1 = Process(target=calculate_sum, args=(1, 1000000))
    t2 = Process(target=calculate_sum, args=(1000001, 2000000))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print("Time taken by processes: ", end - start_time)
    print("Main thread is running")

class Hello(Thread):
    def run(self):
        for a in range(5): 
            print("Hello", a+1)
            time.sleep(0.3)

class Hi(Thread):
    def run(self):
        for a in range(5): 
            print("Hi", a+1)
            time.sleep(0.2)
def hello():
    for a in range(5): 
        print("Function Hello", a+1)
        time.sleep(0.3)

def hi():
    for a in range(5): 
        print("Function Hi", a+1)
        time.sleep(0.2)

def calculate_sum(num1, num2):
    sum = 0
    for a in range(num1, num2+1):
        sum += a*a
    

if __name__ == "__main__":
    try:
        5/8
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else: 
        print("Division successful")
    finally:        print("This will always execute")

    main()

