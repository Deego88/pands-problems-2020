#Ricky Deegan
#check if a number is prime (can only be divided by itself evenly)
#the primes are 2, 3, 5, 7, 11, 13, ....
#try to figure of if a number is prime of not. e.g 347

p = 347 
m = 2
isprime = True

while m < p: 
    if p % m ==0:
       # print(m,"divides", p, "and therefore", p, "is not prime")
       isprime = False
       break
    m = m + 1

if isprime:
    print (p, "is a prime number.")
else:
    print (p, "is not prime.")
