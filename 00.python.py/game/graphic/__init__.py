"""graphic 패키지가 바깥에 공개하는 기능을 정하는 파일."""

# render.py 안의 함수를 graphic 패키지 바로 아래에 꺼내 놓는다.
# game.graphic.render.render_test() 대신 game.graphic.render_test()로 호출할 수 있다.
from .render import render_test

# from game.graphic import *에서 공개할 이름이다.
__all__ = ["render_test"]
