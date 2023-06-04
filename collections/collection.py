import random, math, time, threading

# by = bytes()
# by = "still allows embedded 'single' quotes"
# print(by)
# print(by.count('single'))



 
# def getTotal(low, high, owner):
#   own = owner
#   total = 0
#   for i in range(low, high):
#     total += i
#     print("{} : total = {}".format(own, total))
#     time.sleep(0.01)
 
# t = threading.Thread(target=getTotal, args=(1, 100, "sub_thread"))
# t.start()
 
# # print("Main Thread")
# getTotal(1,100, "main_thread")

# ta = [0 for 0 in range(1000)]
# 타율이 0.275 이면 

# 1에서부터 100까지 소수 구하기
def isPrimeNumber(num):
  for i in range(2, int(math.sqrt(num-1))+1):
    nam = num % i
    if nam == 0:
      return False
  
  return True


def getPrimeNumberInRage(num, owner):
  li = []
  for i in range(2, num):
    if isPrimeNumber(i):
      li.append(i)
      
  print("{} : {}".format(owner, li))
  #return li
  
n = 0
def printCount():
  global n
  n = n + 1
  print( n )
      
t = threading.Thread(target=getPrimeNumberInRage, args=(100, "sub-thread"))
t.start()

getPrimeNumberInRage(100, "main-thread")


tm = threading.Timer(3, printCount)
tm.start()

# while True:
#   if n >= 30:
#     threading.Timer.cancel(tm)
#     break