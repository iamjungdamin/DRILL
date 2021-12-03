import pickle

# data = [1,2,3,4]
#
# with open('data.pickle', 'wb') as f:    # 바이너리 파일
#     pickle.dump(data, f)
#
# with open('data.pickle', 'rb') as f:
#     read_data = pickle.load(f)
#
# print(type(read_data))
# print(read_data)


class npc:
    def __init__(self, name, x, y):
        self.name, self.x, self.y = name, x, y


yuri = npc('yuri', 100, 200)

with open('yuri.pickle', 'wb') as f:
    pickle.dump(yuri, f)

with open('yuri.pickle', 'rb') as f:
    read_yuri = pickle.load(f)

print(read_yuri)
print(read_yuri.name, read_yuri.x, read_yuri.y)

# 피클로 안되는 것들: 클래스 변수, 순수 파이썬이 아닌 외부 라이브러리 데이터
# Boy 클래스의 이미지, 폰트 등은 저장못함 -> x, y, dir, 현재 상태 정도만 선택적으로 저장하면 됨


# dict -> update 방식
# 클래스 내부 변수를 딕셔너리 형태로 저장 가능 (obj.__dict__)
yuri.__dict__.update( {'name': 'jisu', 'x':1000, 'y':999} )
print(yuri.name, yuri.x, yuri.y)
