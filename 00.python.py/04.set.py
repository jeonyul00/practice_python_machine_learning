# 중복을 허용하지 않고 순서가 없는 데이터의 모임으로, 교집합, 합집합, 차집합 등의 집합 연산을 쉽게 처리할 수 있다.

s1 = set([1,2,3])
print(s1)
print("=" * 100)
# 중괄호({})를 사용해서 집합 자료형을 직접 만들 수도 있다.
s2 = {1, 2, 3}
print(s2)
# 리스트나 튜플은 순서가 있기(ordered) 때문에 인덱싱으로 요솟값을 얻을 수 있지만
# 집합 자료형은 순서가 없기(unordered) 때문에 인덱싱으로 요솟값을 얻을 수 없다.
notAOeder = {"1","2","3","4","5"}
print(notAOeder)
print("=" * 100)
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1)
print(s2)
print(s1 & s2)
print(s1.intersection(s2))
print(s1 | s2)
print(s1.union(s2))
print(s1 - s2)
print(s1.difference(s2))
s1.add(4)
s1.update([4, 5, 6])
print("=" * 100)
print(s1)
s1.remove(2)
print(s1)

# discard
# remove와 비슷하지만, 존재하지 않는 값을 제거하려 해도 오류가 발생하지 않는다.
s1.discard(2)
print(s1)
s1.clear()