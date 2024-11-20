from graphics import*
import time
#function for carrot house scene
def carrothouse():
    image.undraw()
    bg2=Image(Point(500,350),"carrothouse.png")
    bg2.draw(win)
    print('carrot house interior')
    image.draw(win)
    time.sleep(0.0001)
    key=win.getKey()
      
       
#function for bakery scene 
def bakery():
    image.undraw()
    bg3=Image(Point(500,350),"bakerybg.png")
    bg3.draw(win)
    print('bakery interior')
    image.draw(win)
    time.sleep(0.0001)
#function for tree house scene 
def treehouse():
    image.undraw()
    bg4=Image(Point(500,350),"tree_scene.png")
    bg4.draw(win)
    print('tree interior')
    image.draw(win)
    time.sleep(0.0001)
    
#creates textbox for information function
def textbox():
        speed=10
        box.draw(win)
        box.setFill('white')
            
        text=Text(Point(500,250), 'use Up, Down, Left, and Right arrows to move!')   
        text.setSize(20)
        text.setFace("courier")
        text.draw(win)
            
        text2=Text(Point(500,300), 'to enter the a house, key E then click  house')
        text2.setSize(20)
        text2.setFace("courier")
        text2.draw(win)

        text3=Text(Point(500,350), 'to leave house key R')      
        text3.setSize(20)
        text3.setFace("courier")
        text3.draw(win)

        text4=Text(Point(500,400), 'to close program key C')         
        text4.setSize(20)
        text4.setFace("courier")
        text4.draw(win)
            
        text5=Text(Point(500,450), 'key any key to close this text and I to reopen')         
        text5.setSize(20)
        text5.setFace("courier")
        text5.draw(win)
        time.sleep(0.0001)

#text box closes with key with any key
        key=win.getKey()
        if key == key:
                text.undraw()
                text2.undraw()
                text3.undraw()
                text4.undraw()
                text5.undraw()
                box.undraw()
                
#main function for creation and call of scenes
def bunny():
#creates invisible button for carrot house scene 
    button=Rectangle(Point(800,500),Point(1000,700))
    button.draw(win)

    
#creates invisible button for bakery scene
    button2=Rectangle(Point(300,100),Point(500,300))
    button2.draw(win)
    
#creates invisible button for tree scene
    button3=Rectangle(Point(0,350),Point(200,700))
    button3.draw(win)
    
#draws original scene
    background=Image(Point(500,350),"newbg.png")
    background.draw(win)
    image.draw(win)
    
#creates textbox w/ instructions    
    textbox()

#allows for movement of bunny     
    while True:
        key=win.getKey()
        if key == 'Left':
            image.move(-20,0)
        elif key == 'Right':
            image.move(20,0)
        elif key == 'Up':
            image.move(0,-20)
        elif key == 'Down':
            image.move(0,20)
        time.sleep(0.0001)       
            
#allows for user to return to original scene with 'r'
        if key == 'r':
            image.undraw()
            background.draw(win)
            image.draw(win)
        
#reopen info box and text with 'i'
        if key == 'i':
            textbox()
            
#close program with key 'c'
        if key == 'c':
            win.close()
                    
#key e then click a house to switch scene
#gets click points
        if key == 'e':
            p=win.getMouse()
            p1=p.getX()
            p2=p.getY()
            
#checks to make sure click point in within bounds of button for carrot house entry
            if 800<=p1<=1000 and 500<=p2<=700:                                      
                background.undraw()                
                carrothouse()
                win.checkKey()
                if key == '-':
                    other()
            
                       
#checks to make sure click point in within bounds of button for bakery house entry
#draws bakery scene 
            elif 450<=p1<=700 and 100<=p2<=300:                
                background.undraw()
                bakery()                

#checks to make sure click point in within bounds of button for tree house entry
#draws tree scene
            elif 0<=p1<=200 and 350<=p2<=700:                
                background.undraw()
                treehouse()
                
#close program with key 'c'                
                key=win.checkKey()
                if key == 'c':
                    win.close()
            
        

update(10)
    
if __name__=="__main__":
    
    speed=10
    image=Image(Point(150,100), "newbun.png")
    win=GraphWin('bunny', 1000,700)
    box=Rectangle(Point(100,200),Point(900,500))
    key=win.getKey()
    bunny()
    textbox()
    carrothouse()
    bakery()
    treehouse()
    other()
