#prime number
# n=int(input("enter the number: "))
# count=0
# for i in range(1,n+1):
#     if (n%i==0):
#         count+=1
# if count == 2:
#     print(n,"is a prime number")
#     print(True)
# else:
#     print(n,"is not a prime number")
#     print(False)
#Brute force approach 
# n=int(input("enter the number: "))
# count=0
# for i in range(1,(n//2)+1):
#     if (n%i==0):
#         count+=1
# if count == 1:
#     print(n,"is a prime number")
#     print(True)
# else:
#     print(n,"is not a prime number")
#     print(False)
#O(squareroot(n)) like dsa 
# n=int(input("enter the number: "))
# count=0
# for i in range(1,int(n**0.5)+1):
#     if (n%i==0):
#         count+=1
# if count == 1:
#     print(n,"is a prime number")
#     print(True)
# else:
#     print(n,"is not a prime number")
#     print(False)
# n number of primes
# n = int(input("Enter the number:"))
# for n in range(1, n+1):
#     count=0
#     for i in range(1,int(n**0.5)+1):
#         if n%i==0:
#             count+=1
#     if count==1:
#         print(n)
# how many times the code  excuted  
# primecount=0
# n=int(input("Enter the number: "))
# for n in range(1,n+1):
#     count=0
#     for i in range(1,int(n**0.5)+1):
#         if n%i==0:
#             count+=1
#     if count==1:
#         primecount+=1
# print(primecount)

#task
#1)find next prime 16->17
#2) Find the nearest prime 14-> 13, 17 O/P = 13 


# 1)find next prime
# n=int(input("Enter a number: "))
# next_num=n+1
# while True:
#     count=0
#     for i in range(1,int(next_num**0.5)+1):
#         if next_num%i==0:
#             count+=1
#     if count==1:
#         print(next_num)
#         break
#     next_num += 1

# 2) Find the nearest primes 14->13 and 17 O/P= 13
# n=int(input("Enter a number: "))
# prev_num=n-1
# next_num=n+1
# while True:
#     count=0
#     for i in range(1,int(prev_num**0.5)+1):
#         if prev_num%i==0:
#             count+=1
#     if count == 1:
#         print(prev_num)
#         break
#     prev_num-=1









    
    




