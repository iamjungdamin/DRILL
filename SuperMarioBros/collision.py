import server
import game_world


def check_collision(o1, o2, index1=0, index2=0):
    a1, a2, a3, a4 = o1.get_bb(index1)
    b1, b2, b3, b4 = o2.get_bb(index2)

    if a1 > b3 or a3 < b1:  # x축
        return False
    if a4 < b2 or a2 > b4:  # y축
        return False

    return True


def collide_update():
    # mario and enemy
    for enemy in server.enemies:
        if check_collision(server.mario, enemy) and enemy.state == 0:
            if server.mario.yPos > enemy.yPos:
                enemy.state = 1
                server.mario.jump()
            else:
                if server.mario.trans >= 0 and not server.mario.invincibility:
                    server.mario.trans -= 1
                    if server.mario.trans < 0:
                        print('Game Over')
                        pass
                    server.mario.invincibility = True
                    break

    # mario and block
    for block in server.floorBlocks:
        if check_collision(server.mario, block):
            server.mario.fall_speed = 0
            server.mario.yPos = block.yPos + 20 + 16

    for block in server.itemBlocks:
        if check_collision(server.mario, block):
            server.mario.fall_speed = 0
            server.mario.yPos = block.yPos + 15 + 16
        if check_collision(server.mario, block, 0, 1):
            # self.fall_speed = 0
            server.mario.yPos = block.yPos - 15 - 16
            block.frame = 3

    for block in server.brickBlocks:
        if check_collision(server.mario, block):
            server.mario.fall_speed = 0
            server.mario.yPos = block.yPos + 15 + 16
        if check_collision(server.mario, block, 0, 1):
            server.brickBlocks.remove(block)
            game_world.remove_object(block)
            server.mario.fall_speed = 0
            server.mario.yPos = block.yPos - 15 - 16

