"""점프 투 파이썬 05-3 '패키지' 실행 예제.

실행 방법(프로젝트 최상위 폴더에서):
    python3 00.python.py/12.package.py
"""

print("=" * 60)
print("0. 먼저 구조부터 보기")
print("""
game/                       <- 패키지(폴더)
    __init__.py             <- 패키지의 입구
    sound/                  <- 하위 패키지
        __init__.py
        echo.py             <- 모듈(파일)
    graphic/                <- 하위 패키지
        __init__.py
        render.py           <- 모듈(파일)

기억할 것: 모듈은 .py 파일 하나, 패키지는 모듈을 담은 폴더입니다.
""")


print("=" * 60)
print("1. 모듈 전체를 가져오기")
import game.sound.echo

# 전체 경로를 모두 적어서 호출한다.
game.sound.echo.echo_test("첫 번째 방법")


print("=" * 60)
print("2. 패키지에서 모듈을 가져오기")
from game.sound import echo

# echo라는 짧은 이름으로 모듈을 사용한다.
echo.echo_test("두 번째 방법")


print("=" * 60)
print("3. 모듈에서 함수만 가져오기")
from game.sound.echo import echo_test

# 함수 이름만 바로 호출한다.
echo_test("세 번째 방법")


print("=" * 60)
print("4. __init__.py가 패키지의 입구 역할을 하는 모습")
import game

print("game.VERSION:", game.VERSION)
game.print_version_info()

# game/__init__.py가 render_test를 미리 가져왔기 때문에
# game.graphic.render.render_test() 대신 짧게 호출할 수 있다.
game.render_test()


print("=" * 60)
print("5. import는 같은 실행 중에는 한 번만 초기화한다")
print("game을 다시 import해도 초기화 문구가 또 나오지 않습니다.")
import game  # 이미 불러온 패키지라 __init__.py를 다시 실행하지 않는다.


print("=" * 60)
print("핵심 정리")
print("1) .py 파일 하나 = 모듈")
print("2) 관련 모듈을 담은 폴더 = 패키지")
print("3) __init__.py = 패키지를 처음 불러올 때 실행되는 입구")
print("4) .은 현재 패키지, ..은 부모 패키지를 뜻함")
