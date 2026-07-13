"""game 패키지의 입구.

이 파일은 ``import game``을 처음 실행할 때 한 번 실행된다.
자주 쓰는 기능을 여기서 꺼내 놓으면 사용자가 더 짧게 호출할 수 있다.
"""

from .graphic.render import render_test

VERSION = "1.0"


def print_version_info():
    print(f"game 패키지 버전: {VERSION}")


print("[game/__init__.py] game 패키지를 처음 불러왔습니다.")

