import math
import tkinter as tk


def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr


def func(x, y):
    xPM = 0.5 - x
    yPM = 0.5 - y
    shapePM = (xPM ** 2 + yPM ** 2) ** 0.5 - 0.02

    xEye = 0.59 - x
    yEye = 0.30 - y
    shapeEye = (xEye ** 2 + yEye ** 2) ** 0.5 + 0.002

    upSide = yPM > 2 * xPM / 3 and x >= 0.5 and y >= 0.5
    downSide = yPM < -2 * xPM / 3 and x >= 0.5 >= y

    return (x > shapePM < 0.5 or y < shapePM > 0.5) and shapeEye > 0.06, 0, 0
    '''
    if x > 0.5 > y and 0.3 - shapeEye > 0.24:
        return 0, 0, 0
    elif upSide or downSide:
        return 0, 0, 0
    elif 0.5 - shapePM > 0.2 and 0.5 - shapePM > 0.2:
        return 1, 1, 0
    else:
        return 0, 0, 0
    '''
    

label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()
