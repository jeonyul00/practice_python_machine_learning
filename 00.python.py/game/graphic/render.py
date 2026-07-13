"""화면을 그리는 기능을 담당하는 모듈."""

# sound 패키지가 공개한 echo_test를 가져온다.
# .. 은 부모인 game을 뜻하므로 ..sound는 game.sound이다.
from ..sound import echo_test


def render_test():
    print("화면을 그립니다.")
    echo_test("렌더링 완료")
