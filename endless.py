import render
import object
import game_io as io
import tilemap

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

objects = []
player = object.Object(1, 1, '@', object.OBJCLASS_PLAYER)
objects.append(player)

for i in range(4):
    monster = object.Object(4, 4+i, 'A', object.OBJCLASS_MONSTER)
    objects.append(monster)

render.render_init(SCREEN_WIDTH, SCREEN_HEIGHT, b'Endless Tower')

game_running = True

while game_running and not render.check_window_closed():
    render.render_draw(objects)
    render.render_clear(objects)
    game_running = io.wait_for_key(player)








