import turtle

class Artist:

    def __init__(self, t):
        self.t = t

    def move(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def square(self, size=100):
        for i in range(4):
            self.t.forward(100)
            self.t.right(90)

    def star(self, size = 100):
        for i in range(5):
            self.t.forward(30)
            self.t.right(144)
            self.t.forward(30)
            self.t.left(72)
        
        

def main():
        canvas = turtle.Screen()
        canvas.bgcolor("light green")
        canvas.title("Turtle Example")

        t = turtle.Turtle()
        t.shape("turtle")
        t.speed(1)
        t.color("green")
        t.pencolor("black")

        art = Artist(t)
        
        t.forward(100)
        t.left(120)
        t.forward(100)
        t.left(120)
        t.forward(100)

        t.right(60)
        t.penup()
        t.goto(-20, -20)
        t.pendown()

        art.square()

        t.penup()
        t.left(130)
        t.forward(80)
        t.pendown()
        t.circle(20)
        t.penup()
        t.left(190)
        t.forward(50)
        t.pendown()
    
        for i in range(360):
            t.speed(0)
            t.left(1)
            t.forward(1)

        t.speed(1)
        t.penup()
        t.right(50)
        t.forward(200)
        t.pendown()
        t.speed(2)
        
        art.star()

        t.speed(1)

        t.penup()
        t.right(10)
        t.forward(60)
        t.pendown()

        for i in range(9):
            t.forward(30)
            t.left(40)

        t.penup()
        t.speed(1)
        t.right(60)
        t.forward(60)
        t.speed(1)
        for i in range(4):
            t.forward(1)
            t.backward(1)
        t.speed(3)
        t.right(500)


if __name__ == "__main__":
    main()
