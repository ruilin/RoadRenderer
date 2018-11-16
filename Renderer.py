#!/usr/bin/python
# -*- coding:UTF-8 -*-

from Tkinter import *
from DataMapper import Mapper
from PIL import Image, ImageDraw
import aggdraw

DATA = [
    [115.157989,
     -30.601056],
    [115.158096,
     -30.600876],
    [115.158195,
     -30.60075],
    [115.158264,
     -30.600548],
    [115.158554,
     -30.600325],
    [115.158653,
     -30.600295],
    [115.158775,
     -30.600329],
    [115.158843,
     -30.600411],
    [115.158882,
     -30.60052],
    [115.158874,
     -30.60088]
]

DATA = [
    [
        109.514923,
        18.228886
    ],
    [
        109.514862,
        18.228931
    ],
    [
        109.514793,
        18.228981
    ],
    [
        109.514641,
        18.229074
    ],
    [
        109.514320,
        18.229239
    ],
    [
        109.514290,
        18.229273
    ],
    [
        109.514259,
        18.229322
    ],
    [
        109.514244,
        18.229368
    ],
    [
        109.514244,
        18.229412
    ],
    [
        109.514244,
        18.229855
    ],
    [
        109.514236,
        18.230101
    ],
    [
        109.514229,
        18.230204
    ],
    [
        109.514214,
        18.230324
    ],
    [
        109.514175,
        18.230553
    ],
    [
        109.514076,
        18.231087
    ],
    [
        109.514000,
        18.231405
    ],
    [
        109.513962,
        18.231562
    ],
    [
        109.513908,
        18.231724
    ],
    [
        109.513824,
        18.231924
    ],
    [
        109.513741,
        18.232138
    ],
    [
        109.513695,
        18.232302
    ],
    [
        109.513672,
        18.232405
    ],
    [
        109.513664,
        18.232498
    ],
    [
        109.513657,
        18.232662
    ],
    [
        109.513649,
        18.232836
    ],
    [
        109.513657,
        18.232988
    ],
    [
        109.513672,
        18.233181
    ],
    [
        109.513733,
        18.233576
    ]
    ]

canvasW = 500
canvasH = 500

mapping = Mapper(canvasW, canvasH)
result = mapping.mapping(DATA)

# 画在窗口
# window = Tk()
# window.title("Road Renderer")
# canvas = Canvas(window, width=canvasW, height=canvasH, bg="white")
# canvas.create_line(result, width=20, fill="black", tags="line")
# canvas.pack()
# window.mainloop()

# 保存图像
# points = []
# for i in range(len(result)):
#     points.append(tuple(result[i]))
#
# im = Image.new("RGB", (canvasW, canvasH), "#ffffff")
# dr = ImageDraw.Draw(im)
# dr.line(points, fill="black", width=20)
# im.save("temp.png")



# 曲线
im = Image.new("RGB", (canvasW, canvasH), "#ffffff")
draw = aggdraw.Draw(im)
pen = aggdraw.Pen("black", 20)
path = aggdraw.Path()

path.moveto(result[0][0], result[0][1])
for i in range(len(result) - 1):
    path.curveto(result[i][0],
                 result[i][1],

                 (result[i][0] + result[i + 1][0]) / 2,
                 (result[i][1] + result[i + 1][1]) / 2,

                 result[i + 1][0],
                 result[i + 1][1])

draw.path(path, pen)
draw.flush()

draw2 = ImageDraw.Draw(im)
center = (result[0][0], result[0][1])
rad = 10
draw2.chord((center[0] - rad, center[1] - rad,
            center[0] + rad, center[1] + rad),
          0, 360,
          fill=(255, 0, 0))


im.save("temp.png")


# img = Image.new("RGB", (200, 200), "white")
# canvas = aggdraw.Draw(img)
#
# pen = aggdraw.Pen("black")
# path = aggdraw.Path()
# path.moveto(0, 0)
# path.curveto(0, 60, 40, 100, 100, 100)
# canvas.path(path, path, pen)
# canvas.flush()
# img.save("curve.png", "PNG")
# img.show()