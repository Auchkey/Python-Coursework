from graphics import *

#LEVEL 0

def main():
    win, selectedColours, patchWorkSize = getInputs()
    colourList = patchDraw(win, selectedColours)
    reColour(win, selectedColours, colourList, patchWorkSize)


#LEVEL 1

def getInputs(): #calls functions which get colour and window size inputs from user, then creates the window.
    size = getPatchSize()
    selectedColours = getColours()
    win = GraphWin("Patchwork", size*100, size*100) #size of window is inputted size * 100 (pixels), as each patch is 100x100 pixels.
    win.setBackground("white")
    return win, selectedColours, size


#LEVEL 2

def getPatchSize(): # Get valid patchwork size from user.
    while True:
        size = eval(input("Please enter the size of the patchwork (valid sizes are 5, 7 and 9): \n"))
        if size % 2 != 0 and size > 4 and size < 10: # If an odd number between 5 and 9.
            break
        print ("That's not a valid size (5, 7 or 9)!\n")
    return size


def getColours(): #get valid colours for patchwork from user.
    validInputs = ["red","green","blue","orange","brown","pink"]
    print("Choose three colours out of the following: red, green, blue, orange, brown or pink. \n")
    Colour1, Colour2, Colour3 = "","","" # Starts empty to trigger following code.
    while Colour1.lower() not in validInputs or Colour2.lower() not in validInputs or Colour3.lower() not in validInputs: # Check if values are not within the list. .lower() in case user inputs using uppercase.
        Colour1 = input("Enter colour 1: ")
        Colour2 = input("Enter colour 2: ")
        Colour3 = input("Enter colour 3: ")
        if Colour1.lower() not in validInputs or Colour2.lower() not in validInputs or Colour3.lower() not in validInputs: # If any of the inputs are still invalid...
            print("One or more values you entered were invalid! Please enter any of the following: red, green, blue, orange, brown or pink. \n") #... then error message returned and user prompt to try again.
            Colour1 = input("Enter colour 1: ")
            Colour2 = input("Enter colour 2: ")
            Colour3 = input("Enter colour 3: ")
    selectedColours = [Colour1, Colour2, Colour3]
    return selectedColours     


#LEVEL 1

def patchDraw(win, colours): # Draws out the patchwork using the given inputs defined by the user.
    yCheck = (win.getHeight()/2) # Gets ycoord of midpoint of patch.
    colourList = [] # List for all colours per patch used when generating patchwork.
    for x in range(0,win.getWidth(),100):
        for y in range(0,win.getHeight(),100): 
            if x == 0 or x+100 == win.getWidth(): # Check if first column or last column in patchwork.
                patternColour = colours[0]
            elif y < yCheck-50: # Check if y is less than top of the midpoint-squares.
                patternColour = colours[1]
            elif y >= yCheck+50: # Check if y is greater than or equal to bottom of the midpoint-squares
                patternColour = colours[2]
            else:
                patternColour = colours[0]
            colourList.append(patternColour)
            lengthOfList = len(colourList)
            if lengthOfList % 2 == 0: # If even:
                pattern1Draw(win, x, y, patternColour)
            else: # If odd:
                pattern2Draw(win, x, y, patternColour)
    return colourList


#LEVEL 2

def pattern1Draw(window, xCoord, yCoord, patternColour): # Pattern of 25 squares alternating between coloured and white. Four circles inside each oppositely coloured to square.
    colourCount = 0 
    for y in range (yCoord,yCoord+100,20):
        for x in range (xCoord,xCoord+100,20):
            boxDraw(window, x, y, patternColour, colourCount)
            circleDraw(window, x, y, patternColour, colourCount)
            colourCount = colourCount+1 # For keeping track of which colour to use for squares and circles.


#LEVEL 3

def boxDraw(window, x, y, currentColour, colourCount):
    box = Rectangle(Point(x,y), Point(x+20,y+20))
    if colourCount % 2 != 0: # If odd:
        currentColour = "white" # Don't use user defined colour.
    box.setFill(currentColour)
    box.setOutline(currentColour)
    box.draw(window)


def circleDraw(window, x, y, currentColour, colourCount):
    circVals = [[5, 5], [5, 15], [15, 5], [15, 15]] # Multi-dimensional array containing relative coords of circles to draw.
    smallCircles = [] # Reset to empty array when function is called for drawing next four circles.
    for c in range(4): # To create four small circles.
        smallCircle = Circle(Point(x+circVals[c][0],y+circVals[c][1]), 5) # Looks at 1st and 2nd values of index c in array.
        smallCircles.append(smallCircle)
    if colourCount % 2 == 0: # If even:
        currentColour = "white" # Don't use user defined colour.
    for i in range(4): # Does the following to all four circles:
        smallCircles[i].setFill(currentColour)
        smallCircles[i].setOutline(currentColour)
        smallCircles[i].draw(window)


#LEVEL 2

def pattern2Draw(window, xCoord, yCoord, patternColour): # Pattern made up of 25 boxes with the text 'hi!' inside each box.
    for x in range(xCoord,xCoord+100,20):
        for y in range(yCoord,yCoord+100,20):
            # Boxes part:
            box = Rectangle(Point(x,y), Point(x+20,y+20)) # Boxes 20x20 pixels, total of 5 per row/column.
            box.setOutline(patternColour)
            box.draw(window)
            # hi! part:
            hi = Text(Point(x+10, y+10), "hi!") # Text placed in centre of each box.
            hi.setSize(6)
            hi.setOutline(patternColour)
            hi.draw(window)
            


#LEVEL 1

def reColour(win, selectedColours, colourList, patchWorkSize): # Recolours patches which are clicked.
    while True: # Loops until window is closed.
        pointOnWindow = win.getMouse()
        distanceFromLeft = pointOnWindow.getX() % 100 # Calcs how far from left side of patch the user click was
        distanceFromTop = pointOnWindow.getY() % 100 # As above, for distance from top of patch.
        xPointToDrawFrom = pointOnWindow.getX() - distanceFromLeft # Gives x Coord of where to recolour current patch.
        yPointToDrawFrom = pointOnWindow.getY() - distanceFromTop # As above for y Coord.
        colourToUse = int(((xPointToDrawFrom/100)*patchWorkSize) + (yPointToDrawFrom/100)) # Gets index of current selected patch.
        currentColour = selectedColours.index(colourList[colourToUse]) # Matches current colour of patch to the colour in selectedColours, returning its index.
        nextColour = (currentColour + 1) % len(selectedColours) # Determines next colour to use in selectedColours list.
        colourList[colourToUse] = selectedColours[nextColour] # Sets the current colour of patch to the next one.
        if colourToUse % 2 != 0: # If an odd number, recolour first pattern.
            pattern1Draw(win, xPointToDrawFrom, yPointToDrawFrom, colourList[colourToUse])        
        else: # Otherwise, recolour second pattern.
            pattern2Draw(win, xPointToDrawFrom, yPointToDrawFrom, colourList[colourToUse])
        

#Stuff to do when program is initially executed:

print("Now running patchwork program...\n")
main()
