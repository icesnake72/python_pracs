myString = "abc def ghi"
print(myString[:3])
print(myString[8:])

print(myString[-1])
print(myString[-3:])
print(myString[-7:-4])

upr = myString.upper()
print(upr)
print(upr.lower())

print()
print("strip()")
myString = "  abc aaa ghi  "
print(myString.strip())
myString = "abc aaa ghi"
print(myString.strip('a'))
print(myString.strip('abc'))

print()
print("replace")
myString = "abc aaa ghi"
print(myString.replace('a', 'z'))
myString = "HelloHelloHelloHelloHello"
print(myString.replace('Hello', 'Welcome '))
print(myString.replace('Hello', 'Welcome ', 2))


print()
print("split")
myString = "Hello Hello Hello Hello Hello"
li_hellos = myString.split()
print(li_hellos)

li_hellos = myString.split('o')
print(li_hellos)

li_hellos = myString.split(maxsplit=2)
print(li_hellos)

10
