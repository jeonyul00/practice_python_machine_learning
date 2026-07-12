
# def solution(num):
#     return num * 10
# a = solution(1)
# print(a)

def solution2(*num): # num => type tuple
    return len(num)
print(solution2(1,2,3,4,5))

# 키워드 매개변수는 함수 호출 시 키워드=값 형태로 전달하는 매개변수를 받을 때 사용한다. 키워드 매개변수를 사용할 때는 매개변수 앞에 별 2개(**)를 붙인다.
def solution3(**what):
    return what['a'] * 3   # 문자열 키 'what'로 값(2)을 꺼냄

print(solution3(a= 1))   # 4
