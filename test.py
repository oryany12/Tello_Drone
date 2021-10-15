import time

t1 = time.time()
print(t1)
while True:
    t2 = time.time()
    if t2-t1 >1:
        print(t2)
        print(t2-t1)
        break