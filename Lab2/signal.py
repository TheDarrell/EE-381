import numpy as np

#Probability of error transmission
def signal1(N, p0, e0, e1):
    success = 0
    for x in range (0,N):
        m = np.random.rand()
        if m <= p0:
            s = 0
        else:
            s = 1
        t = np.random.rand()
        if s == 0:
            if t <= e0:
                r = 1
            else:
                r = 0
        else:
            if t <= e1:
                r = 0
            else:
                r = 1
        if r == s:
            success += 1
    print("1.")
    print("Amount of Failure:", N-success)
    print("Probability of Failure:", (N-success)/N)
    print("")
    
signal1(100000, .4, .02, .03)

#P(r = 1|s = 1)
def signal2(N, e0, e1):
    success = 0
    for x in range (0,N):
        s = 1
        t = np.random.rand()
        if s == 0:
            if t <= e0:
                r = 1
            else:
                r = 0
        else:
            if t <= e1:
                r = 0
            else:
                r = 1
        if r == s:
            success += 1
    print("2.")
    print("Amount of Success:", success)
    print("Probability of Success:", success/N)
    print("")
    
signal2(100000, .02, .03)

#P(s = 1|r = 1)
def signal3(N, p0, e0, e1):
   success = 0
   count = N
   for x in range (0,N):
        m = np.random.rand()
        if m <= p0:
            s = 0
        else:
            s = 1
        t = np.random.rand()
        if s == 0:
            if t <= e0:
                r = 1
            else:
                r = 0
        else:
            if t <= e1:
                r = 0
            else:
                r = 1
        if r == 1:
            if s == 1:
                success += 1
        else:
            count -= 1
   print("3.")
   print("Amount of Success:", success)
   print("Amount of trials that r = 1: ", count)
   print("Probability of Success:", success/count)
   print("")
    
signal3(100000, .4, .02, .03)

#Probability of error with enhanced transmission
def signal4(N, p0, e0, e1):
    success = 0
    for x in range (0,N):
        m = np.random.rand()
        if m <= p0:
            s = 0
        else:
            s = 1
        r = [None]*3
        for y in range (0,3):
            t = np.random.rand()
            if s == 0:
                if t <= e0:
                    r[y] = 1
                else:
                    r[y] = 0
            else:
                if t <= e1:
                    r[y] = 0
                else:
                    r[y] = 1
        if sum(r) <= 1:
            d = 0
        else:
            d = 1
        if s == d:
            success += 1
    print("4.")
    print("Amount of Failure:", N-success)
    print("Probability of Failure:", (N-success)/N)
    print("")
    
signal4(100000, .4, .02, .03)