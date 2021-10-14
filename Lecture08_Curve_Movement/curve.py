import turtle
import random


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_line(p1, p2):
    draw_big_point(p1)
    draw_big_point(p2)

    x1, y1 = p1
    x2, y2 = p2

    for i in range(0, 200+1, 2):
        t = i / 100
        # 원래 t의 범위는 0에서 1인데, t의 범위를 조정하면 선분의 길이를 마음대로 조정 가능
        # 0에서 2로 조정하면 2배가 되고 0에서 -1로 조정하면 반대방향이 되고 -무한대에서 무한대로 조정하면 직선이 됨
        x = (1-t)*x1 + t*x2
        y = (1-t)*y1 + t*y2

        draw_point((x, y))
    draw_point(p2)


def blend_lines(p2, p3, p4, p1):
    draw_big_point(p2)
    draw_big_point(p3)
    draw_big_point(p4)
    draw_big_point(p1)

    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4

    for i in range(0, 100+1, 2):
        t = i / 100

        # left line, p2와 p3 섞기
        lx = (1-t)*x2 + t*x3
        ly = (1-t)*y2 + t*y3
        # right line, p4와 p1 섞기
        rx = (1-t)*x4 + t*x1
        ry = (1-t)*y4 + t*y1

        draw_point((lx, ly))
        draw_point((rx, ry))

        # 선분을 섞는다 = 각각의 좌표들을 섞는다
        x = (1-t)*lx + t*rx
        y = (1-t)*ly + t*ry
        # t가 0일때 왼쪽 라인의 시작점 p2와 오른쪽 라인의 시작점 p4를 섞어서 곡선의 시작점 p2가 됨
        # t가 1일때 왼쪽 라인의 도착점 p3와 오른쪽 라인의 도착점 p1을 섞어서 곡선의 도착점 p1이 됨

        draw_point((x, y))  # 2차곡선


def draw_curve_3_points(p1, p2, p3):
    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)

    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    for i in range(0, 100+1, 2):
        t = i / 100
        x = (2*t**2 - 3*t + 1) * x1 + (-4*t**2 + 4*t) * x2 + (2*t**2 - t) * x3
        y = (2*t**2 - 3*t + 1) * y1 + (-4*t**2 + 4*t) * y2 + (2*t**2 - t) * y3

        draw_point((x, y))  # 세점을 지나는 2차곡선
    draw_point(p3)


def draw_curve_4_points(p1, p2, p3, p4):
    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)
    draw_big_point(p4)

    # draw p1-p2
    # p1, p2, p3로부터 앞의 50% 계산 (t: 0~0.5)
    for i in range(0, 50, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
        y = (2*t**2-3*t+1)*p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]
        draw_point((x, y))
    draw_point(p2)

    # draw p2-p3
    # p1, p2, p3, p4로부터 계산 (t: 0~1)
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        draw_point((x, y))
    draw_point(p3)

    # draw p3-p4
    # p2, p3, p4 로부터 뒤의 50% 계산 (t: 0.5~1)
    for i in range(50, 100, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*p2[0]+(-4*t**2+4*t)*p3[0]+(2*t**2-t)*p4[0]
        y = (2*t**2-3*t+1)*p2[1]+(-4*t**2+4*t)*p3[1]+(2*t**2-t)*p4[1]
        draw_point((x, y))
    draw_point(p4)


prepare_turtle_canvas()


# 1. 점과 점을 섞으면 선분
p1 = x1, y1 = random.randint(-300, -200), random.randint(100, 200)
p2 = x2, y2 = random.randint(-50, -20), random.randint(10, 50)
# draw_line(p1, p2)

# 2. 선분과 선분을 섞으면 2차곡선
p1 = x1, y1 = random.randint(100, 300), random.randint(100, 400)
p2 = x2, y2 = random.randint(-300, -100), random.randint(100, 300)
p3 = x3, y3 = random.randint(-300, -200), random.randint(-400, -50)
p4 = x4, y4 = random.randint(100, 400), random.randint(-300, -100)
# blend_lines(p2, p3, p4, p1)
# 이 경우 p2-p3 선분의 중점과 p4-p1 선분의 중점을 이은 선분의 한 점을 지남

# 3. 카디널 스플라인 = 세 점 (p1, p2, p3) 을 지나는 2차곡선
# p1-p2 선분을 2배 (0~2) 하고 p3-p2 선분을 2배 (-1~1) 한 후
# 두 선분을 이으면 두 선분의 중점이 만나는 점 p2를 지남
# 깔끔하게 정리하면 세 점을 2t^2 - 3t + 1 : -4t^2 + 4t : 2t^2 - t 비율로 섞는것
# draw_curve_3_points((-350, -100), (-50, 200), (150, -100))

# 4-1. 네 점 (p1, p2, p3, p4) 을 지나는 2차곡선
# draw_curve_3_points((-350, -100), (-50, 200), (150, -100))
# draw_curve_3_points((-50, 200), (150, -100), (350, 300))
# 세 점을 지나는 2차곡선을 두번 호출하면 연결 부분이 꺾여서 부자연스러움

# 4-2. 2차곡선과 2차곡선을 섞으면 3차곡선
# 네 점을 일정 비율로 섞는 것, 단 p2-p3 사이에서만 정의됨
draw_curve_4_points((-350, -100), (-50, 200), (150, -100), (350, 300))

# 5. 5개의 점을 지나는 곡선은?
# 똑같은 방법으로 가능하지만 제곱이 너무 많아짐
# 최적화를 위해서는 최대한 곱하기와 나누기를 줄여야함


turtle.done()
