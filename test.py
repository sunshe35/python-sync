import turtle as t

_list = []

def coordinate(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color('black')
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    print(str(x), str(y))
    _list.append((x,y))
    print(_list)
#    lx = lx.append(t.xcor)
#    ly = ly.append(t.ycor)


#主代码

t.Screen().bgcolor('white')
t.onscreenclick(coordinate)

t.mainloop()