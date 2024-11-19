from graphics import*
import time
def bunny():
            
#builds window 
    win=GraphWin('bunny', 1000,700)
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
    image=Image(Point(150,100), "newbun.png")
    image.draw(win)
    
    
    
#creates textbox w/ instructions    
    box=Rectangle(Point(100,200),Point(900,500))
    box.draw(win)
    box.setFill('white')
    
    text=Text(Point(500,250), 'use Up, Down, Left, and Right arrows to move!')
    
    text.setSize(20)
    text.setFace("courier")
    text.draw(win)
    
    text2=Text(Point(500,300), 'to enter the house, key E then triple click a house')
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
    
    text5=Text(Point(500,450), 'key O to close this text and I to reopen')         
    text5.setSize(20)
    text5.setFace("courier")
    text5.draw(win)
    
    
    while True:
        #allows for movement of bunny    
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
        
#closes directions box with key 'o'
        if key == 'o':
            box.undraw()
            text.undraw()
            text2.undraw()
            text3.undraw()
            text4.undraw()
            text5.undraw()
        
            
#allows for user to return to original scene with 'r'
        if key == 'r':
            image.undraw()
            background.draw(win)
            image.draw(win)
        
#reopen info box and text with 'i'
        if key == 'i':
            box.draw(win)
            text.draw(win)
            text2.draw(win)
            text3.draw(win)
            text4.draw(win)
            text5.draw(win)

            
#close program with key 'c'
        if key == 'c':
            win.close()
                    
#click e then triple click a house to switch scene
#gets click points
        if key == 'e':
            p=win.getMouse()
            p1=p.getX()
            p2=p.getY()
            p_=win.getMouse()
            p_1=p_.getX()
            p_2=p_.getY()
            poo=win.getMouse()
            poo1=poo.getX()
            poo2=poo.getY()
            
#checks to make sure click point in within bounds of button for carrot house entry
            if 800<=p1<=1000 and 500<=p2<=700:
                
#deconstructs original scene                       
                background.undraw()
                box.undraw()
                text.undraw()
                text2.undraw()
                text3.undraw()
                text4.undraw()
                text5.undraw()
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

            elif 0<=poo1<=200 and 350<=poo2<=700:
                
                background.undraw()
                box.undraw()
                text.undraw()
                text2.undraw()
                text3.undraw()
                image.undraw()
                bg4=Image(Point(500,350),"tree_scene.png")
                bg4.draw(win)
                print('tree interior')
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
    
if __name__=="__main__":
    bunny()
