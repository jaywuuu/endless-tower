# uses libtcod to handle input
import libtcodpy as libtcod
import game

def wait_for_key(player):
    key_pressed = libtcod.console_wait_for_keypress(True)
    process_key(key_pressed.vk, player)

    # check if exit key pressed
    if key_pressed.vk == libtcod.KEY_ESCAPE:
        return False

    return True

def process_key(key, player):
    if key == libtcod.KEY_UP:
        process_move(0, -1, player) 
    elif key == libtcod.KEY_DOWN:
        process_move(0, 1, player)
    elif key == libtcod.KEY_LEFT:
        process_move(-1, 0, player)
    elif key == libtcod.KEY_RIGHT:
        process_move(1, 0, palyer)
