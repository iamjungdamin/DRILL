# self, 생성자가 없음 -> 싱글톤처럼 사용
# 싱글톤: 객체를 하나만, 마치 전역변수처럼 바로 액세스 가능

class Star:
    # 클래스 변수
    type = 'Star'
    x = 100

    def change():
        # 지역 변수 (클래스 변수와 다름)
        x = 200
        print('x is ', x)


print('x IS ', Star.x)  # 100
Star.change()           # 200
print('x IS ', Star.x)  # 100

star = Star()
print('x IS ', star.x)  # 100, 클래스 변수는 객체 변수처럼 액세스 가능
star.change()           # Error
# => Star.change(star)  # 객체를 함수의 첫번째 파라미터로 넘겨줌
# 사실 파이썬의 모든 변수는 포인터

