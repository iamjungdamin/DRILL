def check_collision(o1, o2):
    a1, a2, a3, a4 = o1.get_bb()
    b1, b2, b3, b4 = o2.get_bb()

    if a1 > b3 or a3 < b1:  # x축
        return False
    if a4 < b2 or a2 > b4:  # y축
        return False

    return True

