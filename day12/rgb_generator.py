from random import randint

def rgb_color_gen():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rtrn_seq = f'rgb({r}, {g}, {b})'
    return rtrn_seq
print(rgb_color_gen())