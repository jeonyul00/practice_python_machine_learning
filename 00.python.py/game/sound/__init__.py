"""sound 패키지가 바깥에 공개하는 기능을 정하는 파일."""

# echo.py 안의 함수를 sound 패키지 바로 아래에 꺼내 놓는다.
# game.sound.echo.echo_test() 대신 game.sound.echo_test()로 호출할 수 있다.
from .echo import echo_test

# from game.sound import *에서 공개할 이름이다.
__all__ = ["echo_test"]
