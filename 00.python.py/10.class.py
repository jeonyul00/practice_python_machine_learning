# =============================================================
#  점프 투 파이썬 "05-1 클래스"  (https://wikidocs.net/28)
#  이 책에서 가장 크고 중요한 챕터. 천천히 위에서부터 읽으세요.
#  클래스 = "과자 틀",  객체 = 그 틀로 찍어낸 "과자"
# =============================================================


# =============================================================
# 1. 클래스가 "왜" 필요한가?  (함수만으로는 불편한 상황)
# =============================================================

# 계산기: 이전 결과에 계속 더하는 기능을 함수로 만들면?
result = 0
def add(num):
    global result          # 함수 밖 변수를 쓰려고 global 사용
    result += num
    return result

print("[1] 함수 방식 계산기1 :", add(3), add(4))   # 3, 7 (누적됨)

# 그런데 "계산기가 2대" 필요하면? 변수도 함수도 따로 만들어야 한다...
result1 = 0
result2 = 0
def add1(num):
    global result1
    result1 += num
    return result1
def add2(num):
    global result2
    result2 += num
    return result2
print("[1] 계산기 2대 만들려니 함수를 또 복사... 3대,10대면?? => 불편!")
print("=" * 55)


# =============================================================
# 2. 클래스로 해결!  계산기를 몇 대든 쉽게 찍어낸다
#    - class 로 "틀"을 한 번만 정의하면
#    - Calculator() 로 원하는 만큼 객체(계산기)를 만들 수 있다
# =============================================================
class Calculator:
    def __init__(self):        # 객체가 생길 때 자동 실행 (생성자)
        self.result = 0        # 이 계산기만의 결과값
    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()            # 계산기 1대
cal2 = Calculator()            # 계산기 2대 (서로 독립!)
print("[2] cal1 :", cal1.add(3), cal1.add(4))   # 3, 7
print("[2] cal2 :", cal2.add(3), cal2.add(7))   # 3, 10 (cal1 과 안 섞임)
print("=" * 55)


# =============================================================
# 3. 클래스와 객체의 관계 (과자 틀 비유)
#    - Cookie 라는 틀(클래스)로 과자(객체) 여러 개를 찍는다
# =============================================================
class Cookie:
    pass                       # 아직 내용 없는 빈 클래스

a = Cookie()                   # a 는 Cookie 로 만든 "객체"
b = Cookie()                   # b 도 별개의 객체
print("[3] a 는 Cookie 의 인스턴스:", isinstance(a, Cookie))   # True
print("=" * 55)


# =============================================================
# 4. 사칙연산 클래스 만들기 (핵심! self 이해하기)
# =============================================================
class FourCal:
    # setdata : 객체에 숫자 2개를 저장하는 메서드
    #   self 는 "이 메서드를 호출한 객체 자신" 이 자동으로 들어옴.
    #   a.setdata(4, 2)  ==  FourCal.setdata(a, 4, 2)  (self=a)
    def setdata(self, first, second):
        self.first = first     # 객체 a 안에 first 저장
        self.second = second   # 객체 a 안에 second 저장

    def add(self):             # 더하기
        return self.first + self.second
    def mul(self):             # 곱하기
        return self.first * self.second
    def sub(self):             # 빼기
        return self.first - self.second
    def div(self):             # 나누기
        return self.first / self.second

a = FourCal()
a.setdata(4, 2)                # a.first=4, a.second=2
print("[4] a.first, a.second :", a.first, a.second)   # 4 2
print("[4] add/sub/mul/div   :", a.add(), a.sub(), a.mul(), a.div())  # 6 2 8 2.0

# 객체는 서로 독립적이다
b = FourCal()
b.setdata(3, 8)
print("[4] b.add() (a와 별개):", b.add())   # 11
print("=" * 55)


# =============================================================
# 5. 생성자(__init__) : 객체 만들 때 초깃값을 자동으로 넣기
#    - setdata 를 깜빡하고 add() 하면 에러가 남 (first 가 없어서).
#    - __init__ 은 객체가 "생성되는 순간" 자동으로 호출된다.
# =============================================================
class FourCal2:
    def __init__(self, first, second):   # 생성자
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second
    def div(self):
        return self.first / self.second

a = FourCal2(4, 2)             # 만들 때 바로 값 전달 => 자동으로 __init__ 실행
print("[5] 생성자로 바로 세팅 :", a.first, a.second, "/ add =", a.add())  # 4 2 / add = 6
print("=" * 55)


# =============================================================
# 6. 상속(Inheritance) : 기존 클래스를 물려받아 기능 추가
#    class 자식클래스(부모클래스):
# =============================================================
class MoreFourCal(FourCal2):   # FourCal2 의 모든 기능을 물려받음
    def pow(self):             # 거듭제곱 기능만 새로 추가
        return self.first ** self.second

a = MoreFourCal(4, 2)
print("[6] 물려받은 add() :", a.add())   # 6  (부모 기능 그대로 사용)
print("[6] 새로 추가 pow() :", a.pow())  # 16 (4의 2제곱)
print("=" * 55)


# =============================================================
# 7. 메서드 오버라이딩(Overriding) : 물려받은 메서드를 "덮어쓰기"
#    - 원래 div 는 0으로 나누면 에러 → 안전하게 고쳐 쓴다
# =============================================================
class SafeFourCal(FourCal2):
    def div(self):             # 부모의 div 를 같은 이름으로 다시 정의
        if self.second == 0:   # 0으로 나누려 하면
            return 0           # 에러 대신 0 반환
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)
print("[7] 0으로 나눠도 안전 :", a.div())   # 0 (에러 안 남)
print("=" * 55)


# =============================================================
# 8. 클래스 변수 : 그 클래스로 만든 "모든 객체가 공유" 하는 변수
#    (객체마다 따로인 self.xxx 와 다르다)
# =============================================================
class Family:
    lastname = "김"            # 클래스 변수 (모두 공유)

a = Family()
b = Family()
print("[8] 처음 성씨 :", a.lastname, b.lastname)   # 김 김

Family.lastname = "박"         # 클래스 변수를 바꾸면
print("[8] 바꾼 후   :", a.lastname, b.lastname)   # 박 박 (모든 객체에 반영)
