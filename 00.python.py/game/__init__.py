"""game 패키지가 사용자에게 공개할 기능을 한곳에 모으는 파일."""

# 두 하위 패키지가 공개한 함수를 똑같은 방식으로 가져온다.
from .sound import echo_test
from .graphic import render_test

# from game import *에서 공개할 이름을 명시한다.
__all__ = ["echo_test", "render_test"]

VERSION = "1.0"


def print_version_info():
    print(f"game 패키지 버전: {VERSION}")


print("[game/__init__.py] game 패키지를 처음 불러왔습니다.")
