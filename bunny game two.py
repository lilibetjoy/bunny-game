from graphics import*
import time

def bunny():
    
#builds window and first scene
    win=GraphWin('bunny', 1000,700)
#creates invisible button for carrot house scene 
    button=Rectangle(Point(800,500),Point(1000,700))
    button.draw(win)
#created invidible button for bakery scene
    button2=Rectangle(Point(300,100),Point(500,300))
    button2.draw(win)
#draws original scene
    background=Image(Point(500,350),"newbg.png")
    background.draw(win)
    image=Image(Point(150,100), "newbun.png")
    image.draw(win)
    speed = 100
    
#creates textbox w/ instructions    
    box=Rectangle(Point(100,200),Point(900,500))
    box.draw(win)
    box.setFill('white')
    
    text=Text(Point(500,250), 'use Up, Down, Left, and Right arrows to move!')
    text.draw(win)
    text.setSize(20)
    text.setFace("courier")
    
    text2=Text(Point(500,300), 'to enter the house, key Q then double click a house')
    text2.draw(win)
    text2.setSize(20)
    text2.setFace("courier")

    text4=Text(Point(500,350), 'to leave house key R')         
    text4.draw(win)
    text4.setSize(20)
    text4.setFace("courier")

    text5=Text(Point(500,400), 'to close program key C')         
    text5.draw(win)
    text5.setSize(20)
    text5.setFace("courier")
    
    text3=Text(Point(500,450), 'key E to close this text and I to reopen')         
    text3.draw(win)
    text3.setSize(20)
    text3.setFace("courier")

   
    
    
#allows for movement of bunny    
    while True:
        time.sleep(0.10)
        key=win.getKey()
        if key == 'Left':
            image.move(-20,0)
        elif key == 'Right':
            image.move(20,0)
        elif key == 'Up':
            image.move(0,-20)
        elif key == 'Down':
            image.move(0,20)
            
#allows for user to return to original scene with 'a'
        if key == 'r':
            image.undraw()
            background.draw(win)
            image.draw(win)
        if key == 'i':
            box.draw(win)
            text.draw(win)
            text2.draw(win)
            text3.draw(win)
            text4.draw(win)
            text5.draw(win)

            
#close program with key 'd'
        if key == 'c':
            win.close()
            
#closes directions box with key 'e'
        if key == 'e':
            box.undraw()
            text.undraw()
            text2.undraw()
            text3.undraw()
            text4.undraw()
            text5.undraw()
            
#click q then double click a house to switch scene
#gets click points
        if key == 'q':
            p=win.getMouse()
            p1=p.getX()
            p2=p.getY()
            p_=win.getMouse()
            p_1=p_.getX()
            p_2=p_.getY()
            
#checks to make sure click point in within bounds of button for carrot house entry
            if 800<=p1<=1000 and 500<=p2<=700:
#deconstructs original scene                       
                background.undraw()
                box.undraw()
                text.undraw()
                text2.undraw()
                text3.undraw()
                image.undraw()
                print('carrot house interior')
#draws carrot house scene 
                bg2=Image(Point(500,350),"carrothouse.png")
                bg2.draw(win)
                image.draw(win)
                
#checks for click bounds of bakery button
#draws bakery scene 
            elif 450<=p_1<=700 and 100<=p_2<=300:
                background.undraw()
                box.undraw()
                text.undraw()
                text2.undraw()
                text3.undraw()
                image.undraw()
                bg3=Image(Point(500,350),"bakerybg.png")
                bg3.draw(win)
                print('bakery interior')
                image.draw(win)     

#allows for movement in subsequent scenes 
                key=win.checkKey()
                if key == 'Left':
                    image.move(-20,0)               
                elif key == 'Right':
                    image.move(20,0)
                elif key == 'Up':
                    image.move(0,-20)
                elif key == 'Down':
                    image.move(0,20)
                    
#allows for user to return to original scene with 'a'
                if key == 'r':
                    image.undraw()
                    background.draw(win)
                    image.draw(win)
                    
#close program with key 'd'
                if key == 'c':
                    win.close()
            
        

        update()
    

bunny()

