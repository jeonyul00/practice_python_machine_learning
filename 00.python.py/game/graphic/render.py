"""화면을 그리는 기능을 담당하는 모듈."""

# render.py의 위치는 game/graphic이다.
# .. 은 부모인 game을 뜻하므로 game/sound/echo.py를 가리킨다.
from ..sound.echo import echo_test


def render_test():
    print("화면을 그립니다.")
    echo_test("렌더링 완료")

