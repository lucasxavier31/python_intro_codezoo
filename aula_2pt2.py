import turtle

t = turtle.Pen()

turtle.bgcolor('black')
colors = ['yellow', 'blue', 'red', 'violet', 'orange', 'green']
t.shape('turtle')

for x in range(360):
    t.forward(x)
    t.pencolor(colors[x%6])
    t.left(59)
    t.left(90)

turtle.mainloop()

#lados = input("Você deseja vizualizar uma figura de quantos lados? ")
#t.down = 100
#x = int(lados)
#for i in range (0,x):
#    t.forward(100)
#    t.left(360/x)
