background = None
mario = None
enemies = []
itemBlocks = []
brickBlocks = []
floorBlocks = []
items = []
pipes = []
flag = None
castle = None

boundingBox = False
game_time = 100
gaming = True
cur_stage = 1
wait_time = 0


def init_game():
    global background, mario, enemies, itemBlocks, brickBlocks, floorBlocks, items, pipes, flag, castle
    global game_time, gaming, wait_time

    background = None
    mario = None
    enemies = []
    itemBlocks = []
    brickBlocks = []
    floorBlocks = []
    items = []
    pipes = []
    flag = None
    castle = None

    game_time = 100
    gaming = True
    wait_time = 0

