import random
from encodings import undefined

print("hello world")

numA = 10
numB = 2

print(numA +  numB)
print(numA -  numB)
print(numA *  numB)
print(numA / numB) # 나누기
print(numA // numB) # 몫
print(numA ** numB) # 제곱
print(numA % numB) # 나머지

print(type(numA / numB)) # float
print(type(numA // numB)) # int
print(type(""))
print(type(''))
print(type(''''''))

strA = 'hello'
strB = 'swift'
strC = '0123456789'

print(strA + strB)
print(strA * 10)
print(len(strA))

print(strC[0])
print(strC[0 - 2]) # -2 -> 뒤에서 2번째
print(strC[2-1]) # 2-1 === 1
print(strC[2 - 1]) # 2-1 === 1

# 이상 : 미만 : 간격
# 문자형는 이뮤터블
print(strC[0:1])
print(strC[0:-1:2])
print(strC[0::])
print(strC[::1])
print(strC[:len(strC):])
print(strC[:])
print("=" * 50)
print("%d 뭐 언어가 이 따위냐 %s" % (18,"?"))
print("%s 뭐 언어가 이 따위냐 %s" % (18,"?"))
# s : 문자
# d : 정수
print("=" * 50)
print("%10s" % "뭐 이딴")
print(len("%10s" % "뭐 이딴"))
print("%12s" % "뭐 이딴")
print(len("%12s" % "뭐 이딴"))
print("%-10s" % "뭐 이딴")
print(len("%-10s" % "뭐 이딴"))
print("이런것도 있네? {0} {1}".format(1, "어이없어."))

print("%.2f" % 3.141592)

name = 'jeon'
age = 30
a = f'{name} is {age+100} years old'
print(a)
py = 3.141592
print(f'{py:0.2f}') # 소수점 n자리까지 표시

stringA = 'abcdefg'
print(stringA.count('g')) # g의 개수
print(stringA.index('g')) # 없으면 error
print(stringA.find('5')) # 없으면 -1
print(','.join(stringA))

print(stringA.upper())
spaceSTR = "   a   "
print(spaceSTR.strip())
print(spaceSTR.lstrip())
print(spaceSTR.rstrip())
print(spaceSTR.replace(" ", "_"))
print(stringA.split("c"))
print(stringA.split("d"))