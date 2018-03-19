#Made by C272. http://c272.ga

foundPrime = 0
#Prime array.
while True:
    try:
        file = open("primes.txt", "r")
    except FileNotFoundError:
        file = open("primes.txt", "w")
        file.write("2"+"\n")
        file.flush()
        primes = ["2"]
        break
    else:
        primesUnformat = file.readlines()
        primes = []
        for i in primesUnformat:
            primes.append(i.replace("\n", ""))
        file.close()
        break
    
#Starting number.
x = 3
while True:
    isPrime = 1
    for i in primes:
        if int(i)<int(x):
            if x%int(i)==0:
                isPrime = 0
    if isPrime==0:
        arbit = "true"
    else:
        print(str(x)+" is prime.")
        foundPrime=1
        if str(x) not in primes:
            file = open("primes.txt", "a")
            file.write(str(x)+"\n")
            file.close()
        if str(x) not in primes:
            primes.append(str(x))
    #Next number.
    x+=1
