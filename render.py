# Using libtcod to render things
import libtcodpy as libtcod

def render_init(width, height, title):
    libtcod.console_init_root(width, height, title, False)
    libtcod.console_set_default_foreground(0, libtcod.white)

def render_draw(objects):
    for obj in objects:
        libtcod.console_put_char(0, obj.x, obj.y, obj.symbol, 
                libtcod.BKGND_NONE)
    libtcod.console_flush()
    
def render_clear(objects):
    for obj in objects:
        libtcod.console_put_char(0, obj.x, obj.y, ' ',
                libtcod.BKGND_NONE)

# note:  probably don't need this function.
# we will see later and i'll remove it later.
def render_clear_obj(obj):
    libtcod.console_put_char(0, obj.x, obj.y, ' ',
            libtcod.BKGND_NONE)

def render_rect(x1, y1, x2, y2, char):
    for i in range(y1, y2):
        for j in range(x1, x2):
           libtcod.console_put_char(0, j, i, char,
                   libtcod.BKGND_NONE)

def render_hline(x1, x2, y, char):
    for i in range(x1, x2):
        libtcod.console_put_char(0, i, y, char,
                libtcod.BKGND_NONE)

def check_window_closed():
    if libtcod.console_is_window_closed():
        return True


