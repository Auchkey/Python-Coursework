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
        size = eval(input("Please enter the size of the patchwork (valid sizes are 5, 7 and 9)."))
        if size % 2 != 0 and size > 4 and size < 10: # If an odd number between 5 and 9.
            break
        print ("That's not a valid size (5, 7 or 9)!", end='\n\n') #double new line to make repeated requests for valid input more visually user friendly.
    return size


def getColours(): #get valid colours for patchwork from user.
    validInputs = ["red","green","blue","orange","brown","pink"]
    print("Choose three colours out of the following: red, green, blue, orange, brown or pink", end='\n\n')
    Colour1, Colour2, Colour3 = "","","" # All 3 values start off empty. They need to be assigned values before the while loop so it can apply its checks.
    while Colour1.lower() not in validInputs or Colour2.lower() not in validInputs or Colour3.lower() not in validInputs: # Check if values are not within the list. .lower() in case user inputs using uppercase.
        Colour1 = input("Enter colour 1: ")
        Colour2 = input("Enter colour 2: ")
        Colour3 = input("Enter colour 3: ")
        
        if Colour1.lower() not in validInputs or Colour2.lower() not in validInputs or Colour3.lower() not in validInputs: # If any of the inputs are still invalid...
            print("One or more values you entered were invalid! Please enter any of the following: red, green, blue, orange, brown or pink", end='\n\n') #... then error message returned and user prompt to try again.
            Colour1 = input("Enter colour 1: ")
            Colour2 = input("Enter colour 2: ")
            Colour3 = input("Enter colour 3: ")
            
    selectedColours = [Colour1, Colour2, Colour3]
    return selectedColours     


#LEVEL 1

def patchDraw(win, colours): # Draws out the patchwork using the given inputs defined by the user.
    yCheck = (win.getHeight()/2) # Gets ycoord of the midpoint of the patch.
    colourList = [] # List for all colours per patch used when generating patchwork.
    patternCount = 0  # Used later to check which pattern to use in current box to be drawn, depending on if its an even or odd number.
    
    for x in range(0,win.getWidth(),100):
        for y in range(0,win.getHeight(),100): 
            if x == 0 or x+100 == win.getWidth(): # Check if first column or last column in patchwork. If so, use 1st colour.5
                patternColour = colours[0]
                
            elif y < yCheck-50: # Check if y is less than the top of the midpoint-squares. If so, use 2nd colour.
                patternColour = colours[1]
                
            elif y >= yCheck+50: # Check if y is greater than or equal to the bottom of the midpoint-squares If so, use 3rd colour.
                patternColour = colours[2]
                
            else: # ...Otherwise, use the 1st colour.
                patternColour = colours[0]
                
            if patternCount % 2 != 0: # Patchwork alternates between patterns 1 and 2. If patternCount is odd, draws patch 1...
                pattern1Draw(win, x, y, patternColour)
                
            else: # ...Otherwise, is even and draws patch 2.
                pattern2Draw(win, x, y, patternColour)
                
            colourList.append(patternColour) # Every colour that was used for a patch is added to the list.
            patternCount = patternCount+1 # Keeps track of how many patterns have been drawn so far, +1 for each patch. 
            #---do something similar to recolour to remove this? (i.e. look at index of colourList?)---
    return colourList


#LEVEL 2

def pattern1Draw(window, xCoord, yCoord, patternColour): # Pattern made up of 25 squares of alternating colours, with four oppositely coloured circles inside each square.
    colourCount = 0 # Used later to keep track of which colour to use for each box and four circles design in the patch, depending on if this value is odd or even.
    for y in range (yCoord,yCoord+100,20):
        for x in range (xCoord,xCoord+100,20):
            boxDraw(window, x, y, patternColour, colourCount)
            circleDraw(window, x, y, patternColour, colourCount)
            colourCount = colourCount+1 # Once a box (and its four circles) are drawn, counter increases by 1.


#LEVEL 3

def boxDraw(window, x, y, currentColour, colourCount):
    box = Rectangle(Point(x,y), Point(x+20,y+20))
    if colourCount % 2 != 0: # If an odd number, box surrounding the circles must be white. Otherwise, is whatever colour is being passed to this function.
        currentColour = "white"
        
    box.setFill(currentColour)
    box.setOutline("")
    box.draw(window)


def circleDraw(window, x, y, currentColour, colourCount):
    smallCircle1 = Circle(Point(x+5,y+5), 5)
    smallCircle2 = Circle(Point(x+5,y+15), 5) #may need to make this better, loop with array? [1[5,5],2[5,15],3[15,5],4[15,15]]???
    smallCircle3 = Circle(Point(x+15,y+5), 5)
    smallCircle4 = Circle(Point(x+15,y+15), 5)
    smallCircles = [smallCircle1,smallCircle2,smallCircle3,smallCircle4]
    if colourCount % 2 == 0: # If an even number, circles inside the box must be white. Otherwise, they are whatever colour is being passed to this function.
        currentColour = "white" 
    for i in range(4): # Does the following to all four circles:
        smallCircles[i].setFill(currentColour)
        smallCircles[i].setOutline("")
        smallCircles[i].draw(window)


#LEVEL 2

def pattern2Draw(window, xCoord, yCoord, patternColour): # Pattern made up of 25 boxes with the word 'hi!' inside each box.
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

def reColour(win, selectedColours, colourList, patchWorkSize): # Recolours patches which are clicked on to the next colour in the list of available colours.
    while True: # Loops until window is closed...
        pointOnWindow = win.getMouse() #... as this will pass an error and terminal the program when the window is closed
        distanceFromLeft = pointOnWindow.getX() % 100 # Calculates how far from the left side (i.e. the x axis) of the patch the user click was in pixels, as patches are 100x100 pixels.

        distanceFromTop = pointOnWindow.getY() % 100 # Same as previous comment, but for the distance from the top of the patch (i.e. the y axis).
        xPointToDrawFrom = pointOnWindow.getX() - distanceFromLeft # Takes away the distance from the left side of the patch from the x coordinate of the point clicked, giving the start of the x coordinate of the patch.
        yPointToDrawFrom = pointOnWindow.getY() - distanceFromTop # Same as pervious comment, but calculates the start of the y coordinate of the patch instead by taking away the distance from top of the patch from the y coordinate of the point clicked.
        colourToUse = int(((xPointToDrawFrom/100)*patchWorkSize) + (yPointToDrawFrom/100)) # All drawn patches in the window are indexed based on their position. This calculates the index of the selected patch based on its coordinates. This can then be used to determine the current colour of the patch.
        currentColour = selectedColours.index(colourList[colourToUse]) # Matches the current colour of the patch in colourList to its value in the selectedColours list and stores the index for it.
        nextColour = (currentColour + 1) % len(selectedColours) # Gets the index for the next colour in the selectedColours list for the current colour of the patch. Mods by the length of the list so that the list can loop back to the start if the current index is the last value in the list.
        colourList[colourToUse] = selectedColours[nextColour] # Sets the current colour of the patch to the next avaliable colour in selectedColours.

        if colourToUse % 2 != 0: # If an odd number, drawn the first pattern.
            pattern1Draw(win, xPointToDrawFrom, yPointToDrawFrom, colourList[colourToUse])
            
        else: # Otherwise, draw the second pattern.
            pattern2Draw(win, xPointToDrawFrom, yPointToDrawFrom, colourList[colourToUse])
        

#Stuff to do when program is initially executed:

print("Now running patchwork program...", end='\n\n')
main()