from graphics import *
from Button import *

def main():
    
    win = GraphWin("Character Creator", 800, 600)
    win.setBackground("light steel blue")
    
    ##########################################

    F = Oval(Point(200, 100), Point(500, 500))

    BigEye1 = Circle(Point(290, 250), 35)
    BigEye2 = Circle(Point(410, 250), 35)

    SmallEye1 = Circle(Point(290, 245), 25)
    SmallEye2 = Circle(Point(410, 245), 25)

    RoundNose = Oval(Point(300, 300), Point(400, 320))
    SharpNose = Polygon(Point(310, 350), Point(350, 280), Point(390, 350))

    NeutralMouth = Line(Point(290, 380), Point(410, 380))
    SmileMouth = Rectangle(Point(275, 400), Point(425, 380))

    #######################################################################################
    
    smallEyes = Button(win, Point(650, 100), Point(750, 175), "light yellow", "Small Eyes")
    bigEyes = Button(win, Point(650, 200), Point(750, 275), "light yellow", "Big Eyes")
    
    roundNose = Button(win, Point(520, 100), Point(620, 175), "light yellow", "Round Nose")
    sharpNose = Button(win, Point(520, 200), Point(620, 275), "light yellow", "Sharp Nose")

    neutralMouth = Button(win, Point(520, 300), Point(620, 375), "light yellow", "Neutral Mouth")
    smileMouth = Button(win, Point(520, 400), Point(620, 475), "light yellow", "Smile Mouth")
    
    Face = Button(win, Point(650, 300), Point(750, 375), "gold", "Face")
    Q = QuitButton(win, Point(650, 400), Point(750, 475), "dark red", "Click to END.")

    #######################################################################################

    while True:
        m = win.getMouse()

        if Face.isClicked(m):
            F.setFill("beige")
            F.undraw()
            F.draw(win)

        if bigEyes.isClicked(m):
            BigEye1.setFill("white")
            BigEye2.setFill("white")
            BigEye1.undraw()
            BigEye2.undraw()
            SmallEye1.undraw()
            SmallEye2.undraw()
            BigEye1.draw(win)
            BigEye2.draw(win)

        if smallEyes.isClicked(m):
            SmallEye1.setFill("white")
            SmallEye2.setFill("white")
            SmallEye1.undraw()
            SmallEye2.undraw()
            BigEye1.undraw()
            BigEye2.undraw()
            SmallEye1.draw(win)
            SmallEye2.draw(win)

        if roundNose.isClicked(m):
            RoundNose.setFill("pink")
            RoundNose.undraw()
            SharpNose.undraw()
            RoundNose.draw(win)

        if sharpNose.isClicked(m):
            SharpNose.setFill("pink")
            SharpNose.undraw()
            RoundNose.undraw()
            SharpNose.draw(win)

        if neutralMouth.isClicked(m):
            NeutralMouth.undraw()
            SmileMouth.undraw()
            NeutralMouth.draw(win)

        if smileMouth.isClicked(m):
            SmileMouth.setFill("white")
            SmileMouth.undraw()
            NeutralMouth.undraw()
            SmileMouth.draw(win)

        if Q.isClicked(m):
            break
        
    win.close()


if __name__ == "__main__":
    main()
