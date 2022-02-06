# resolution
WIDTH = 848
HEIGHT = 480

# positions on the frame in order to aim
CENTER_X = int(848 / 2)
CENTER_BASKET = int(848 / 2)
CENTER_Y = int(480 / 2) + 150

CENTER_OFFSET_X = 20
CENTER_OFFSET_Y = 25
CENTER_OFFSET_BASKET = 20

CENTER_RANGE_X = range(CENTER_X - CENTER_OFFSET_X, CENTER_X + CENTER_OFFSET_X, 1)
CENTER_RANGE_Y = range(CENTER_Y - CENTER_OFFSET_Y, CENTER_Y + CENTER_OFFSET_Y, 1)
CENTER_RANGE_BASKET = range(CENTER_BASKET - CENTER_OFFSET_BASKET, CENTER_BASKET + CENTER_OFFSET_BASKET, 1)
