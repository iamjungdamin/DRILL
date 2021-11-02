class Player:
    type = 'Plyaer'

    def __init__(self):
        self.x = 100

    def where(self):
        print(self.x)


player = Player()
player.where()

# 클래스 변수 사용
print(Player.type)

# 클래스 함수 호출
Player.where()          # Error
Player.where(player)    # player.where() 와 같음

# self 는 자기 자신을 가리키는 포인터고
# 함수 호출 시 객체를 클래스 함수의 첫번째 인자로 넘겨줌
