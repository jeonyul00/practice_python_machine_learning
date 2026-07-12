# key value
# 요즘 사용하는 대부분의 언어도 이러한 대응 관계를 나타내는 자료형을 가지고 있는데 이를 딕셔너리라고 하고, '연관 배열(associative array)'또는 '해시(hash)'라고도 한다.

a = { "name": "jeonyul" , "age":30, "etc": [1,2,3]}
print(a)
print(a["name"])
a["name"] = "전율"
print(a)
a['어떠한 값'] = "어떠한 키"
print(a)
del[a['etc']]
print(a)

# 딕셔너리에서 Key는 고유한 값이므로 중복되는 Key 값을 설정하면 하나를 제외한 나머지 것들이 모두 무시된다.
a = {1:'a', 1:'b'}
print(a)
# 또 한 가지 주의할 점은 Key에 리스트는 쓸 수 없다는 것이다.

#
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.keys())

# keys, values, items 함수는 리스트가 아닌 dict_keys, dict_values, dict_items 객체를 반환한다. 이 객체들은 for 문 등 반복 구문에서 리스트처럼 사용할 수 있다
for k in a.keys():
    print(a[k])
print("-"*100)
for value in a.values():
    print(value)
print("-"*100)
for a,b in a.items():
    print(a,b)

print("-"*100)


c = {"a": "a", "b":"b"}
c.clear()
print(c)

a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
a.get('nokey') # None
# a['nokey'] # error

print("-"*100)
print('name' in a)
