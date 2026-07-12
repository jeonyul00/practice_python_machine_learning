# 변경이 안된대요 이뮤터블인가?
t1 = ()
print(type(t1))
t2 = (1, )
print(type(t2))
t3 = (1, 2, 3)
print(type(t3))
t4 = 1,2,3
print(type(t4))
t5 = (1,2,(12,34))
print(type(t5))

# 다 tuple임 미친건가
# 변경 x
# del t1[0] error
# t1[2] = 1 error

t23 = t2 + t3
print(t23)
t = t2 * 10
print(t)