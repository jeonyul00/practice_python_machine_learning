numArr = [1,2,3,4,5,6,7,8,9]
anyArr = ["a", 1,[3,4],{5,6}] # 미친 이게 되네
print(anyArr[2])
print(anyArr[3])
print(anyArr[2][1]) # 도랐누
print(anyArr[-1])

a = [1,2,3]
b = [4,5,6]
print(a + b * 2)
print((a + b) * 2)
numArr.append(10)
numArr.insert(len(numArr),11)
print(numArr)
numArr.remove(10)
print(numArr)
a.append(b)
print(a)
b.extend(a) # 이러면 무한 루프인가
print(b)



