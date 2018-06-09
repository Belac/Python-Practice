from turtle import *
bgcolor("#f7efe1")

class Shape():
    colourFill = ""
    colourLine = ""
    Area = 0
    def newShape (self,Fill,Line):
        self.colourFill = Fill
        self.colourLine = Line

def drawCircle(colourFill,colourLine,diameter):
    fillcolor(colourFill)
    pencolor(colourLine)
    circle(diameter)

drawCircle("#b7b29f","#f7efe1",100)
