import math
import threading
import time

fn = (10005)**(0.5)
fd = 4270934400

f = fn/fd

def run(maxN):
    global sum
    n = maxN - 1000

    n1 = math.factorial(6*n)
    n2 = (13591409 + 545140134*n)

    d1 = math.factorial(3*n)
    d2 = math.factorial(n)**3
    d3 = (-640320)**(3*n)

    while n < maxN:
        n1 = math.factorial(6*n)
        n2 = (13591409 + 545140134*n)

        d1 = math.factorial(3*n)
        d2 = math.factorial(n)**3
        d3 = (-640320)**(3*n)

        sum = sum + (n1 * n2)/(d1 * d2 * d3)

        n = n + 1


if __name__=="__main__":

    sum = 0

    thread0 = threading.Thread(target=run, args=[1000])
    thread1 = threading.Thread(target=run, args=[2000])

    thread2 = threading.Thread(target=run, args=[3000])
    #thread3 = threading.Thread(target=run, args=[4000])

    #thread4 = threading.Thread(target=run, args=[5000])
    #thread5 = threading.Thread(target=run, args=[6000])

    #thread6 = threading.Thread(target=run, args=[7000])
    #thread7 = threading.Thread(target=run, args=[8000])

    #thread8 = threading.Thread(target=run, args=[9000])
    #thread9 = threading.Thread(target=run, args=[10000])

    start = time.time()

    thread0.start()
    thread1.start()
    thread2.start()

    thread0.join()
    thread1.join()
    thread2.join()

    attempt = 1/(f * sum)

print(attempt)
end = time.time()
print(end - start)
#final = 1/(f * (run(1000) + run(2000)))
#print(final)
