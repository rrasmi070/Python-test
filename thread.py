import threading

class Hi(threading.Thread):
    def run(self):
        for i in range(100):
            print(i)

class Hello(threading.Thread):
    def run(self):
        for i in range(100):
            print(i)
t1 =Hi()
t2 = Hello()

t1.start()
t2.start()
