import random
from googletrans import Translator

trans = Translator()
objTrans = trans.translate("I'm a boy", dest="ko")
print(objTrans.text)

print("Here is a tuple")
tp = ("china", "korea", "japan", "America", "England")
print(tp)
print(tp.count("korea"))  # 튜플안에 korea의 갯수
print(len(tp))  # 튜플내의 아이템들의 갯수

try:
  random.shuffle(tp)  # 허용되지 않는다!!!
except TypeError as te:
  # err = trans.translate(te.__str__, dest="ko")
  print("TypeError: {} ===> {}".format(te, "random.shuffle(tp)"))
  
try:
  tp[1] = "Republic of korea" # 허용되지 않는다!!!
except TypeError as te:    
  print("TypeError: {} ===> {}".format(te, "tp[1]"))


# list
print()
print("Here is a list")
li = ["china", "korea", "japan", "America", "England"]
print(li)

print("Append France")
li.append("France")
print(li)

print("Here is another list and join two lists")
li2 = ["India", "Mexico"]
print(li2)
# li.extend(li2)
li = li  + li2
print(li)

print("Ascending Sort ther list")
li.sort()
print(li)

print("Descending Sort ther list")
li.sort(reverse=True)
print(li)

print("Remove 'japan' from the list")
li.remove("japan")
print(li)

print("Remove last item in the list")
li.pop()
print(li)

print("Remove 2nd item in the list")
li.pop(1)
print(li)

print("Copy the list")
li2 = li.copy()
print(li2)

# index()메소드는 첫번째 나타나는 아이템의 인덱스만을 가져온다!!!
print("Get index of India")
print(li.index("India"))

print("Change korea to Rep. of Korea in the list")
li[0] = "Rep. of Korea"
print(li)


# set
# set은 순서가 없고, 아이템의 값을 변경을 할 수 없다. 추가, 삭제는 가능하다.
# set은 인덱스를 지원하지 않는다!!!
setCar = {"Genesis", "BMW", "Benz", "Audi"}
print(setCar)

# Set의 아이템 추가
setCar.add("Porsche")
print(setCar)

# Set의 아이템 삭제
setCar.remove("Genesis")
print(setCar)

# set은 중복 데이터를 허용하지 않는다.
setCar.add("BMW")
print(setCar)

setCar.add(1)
print(setCar)

if "Genesis" not in setCar:
  setCar.add("Genesis")
  print(setCar)
  
len(setCar)


  



