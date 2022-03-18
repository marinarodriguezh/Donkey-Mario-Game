import random
import pyxel
import clasemario
import claseprince
import claseplatform
import clasedonkey
import clasebarrel
import claseladder

class Game:

    def __init__(self):

        WIDTH = 256
        HEIGHT = 192
        CAPTION = "DONKEY KONG"

        self.objDonkey=clasedonkey.Donkey(0,32)
        self.objPrince=claseprince.Prince(120,16)
        self.objMario=clasemario.Mario(20,177)
        self.platforms=[claseplatform.Platform(80,160),claseplatform.Platform(30,128),claseplatform.Platform(60,96),claseplatform.Platform(0,64),claseplatform.Platform(0,192)]#claseplatform.Platform(167,192)]
        self.ladders=[claseladder.Ladder(90,160,False),claseladder.Ladder(160,128,False),claseladder.Ladder(70,96,False),claseladder.Ladder(140,64,False),claseladder.Ladder(100,32,False)]
        self.ladderb=claseladder.Ladder(120,96,True)
        self.ladders.append(self.ladderb)
        self.barriles=[]

        #Screen
        pyxel.init(WIDTH, HEIGHT, caption=CAPTION)

        # Loading the pyxres file
        pyxel.load("assets/my_resource.pyxres")
           
        #Start the game 
        pyxel.run(self.update, self.draw)
    
    def update(self):
        '''This function is executed frame. It checks if you are pressing a key and it creates the barrels. '''

        #Quit game if you press key Q
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        else:
            #Go riht pressing key Right
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.objMario.newmove("right",platforms=self.platforms)

            #Go left pressing key Left
            elif pyxel.btn(pyxel.KEY_LEFT):
                self.objMario.newmove("left",platforms=self.platforms)                    

            #Jump pressing key Space
            for i in self.platforms:                
                if pyxel.btnp(pyxel.KEY_SPACE) and self.objMario.posy+15==i.posy:
                    self.objMario.when=pyxel.frame_count
                    self.objMario.jump()
            if (self.objMario.jumping and pyxel.frame_count-self.objMario.when==5):
                    self.objMario.desjump()
            
            for b in self.barriles:
                #Getting points when jumping a barrel
                if pyxel.btnp(pyxel.KEY_SPACE) and (self.objMario.posy+20==b.posy and ((self.objMario.posx+6) in range(b.posx-11,b.posx+22))):
                    self.objMario.scoreMario()
                #Dying when touching a barrel
                elif (self.objMario.posx+8==b.posx and self.objMario.posy+4==b.posy):
                    self.objMario.death()

            #Go up in a ladder pressing key Up
            if pyxel.btn(pyxel.KEY_UP):
                self.objMario.newmove("up",self.ladders,self.platforms)
                
            #Go down in a ladder pressing key Down
            elif pyxel.btn(pyxel.KEY_DOWN):
                self.objMario.newmove("down",self.ladders,self.platforms)

            #Create barrels
            if random.randint(0,300)<175 and pyxel.frame_count%40==0  and len(self.barriles)<10:        
                self.barriles.append(clasebarrel.Barrel(60,53))
            for i in self.barriles:
                i.movebarrel(self.ladders,self.platforms)
                if i.posy==181 and i.posx==167:
                    self.barriles.remove(i)                  


    def draw(self):
            ''' This function draws graphics from the image bank'''

            #Draw a new screen when mario reaches the prince
            if self.objMario.posy==17:
                pyxel.cls(0)
                pyxel.text(115,80 , "YOU WON!", pyxel.frame_count %16)
                pyxel.blt(145,105,0,self.objPrince.imagenx,self.objPrince.imageny,16,16,colkey=0)
                pyxel.blt(105,105, 0,5, 32, -12, 15, colkey=0)
                pyxel.blt(125,95,0,191,180,16,14,colkey=0)

            #Draw a new screen when mario doesn't have any more lives           
            elif self.objMario.lives==0:
                pyxel.cls(0)
                pyxel.text(105,80 , "GAME OVER", pyxel.frame_count %16)
                pyxel.blt(115,95,0,214,180,16,14,colkey=0)

            #Draw game screen
            else:
                pyxel.cls(0)
                pyxel.text(198, 0, "Score: %i"%(self.objMario.score), pyxel.frame_count %16)
                pyxel.text(198, 20, "Lives: %i"%(self.objMario.lives),pyxel.frame_count %16 )
                
                #Draw princess
                pyxel.blt(self.objPrince.posx,self.objPrince.posy,0,self.objPrince.imagenx,self.objPrince.imageny,16,16,colkey=0)

                #Draw donkey
                pyxel.blt(self.objDonkey.posx,self.objDonkey.posy,0,self.objDonkey.imagenx,self.objDonkey.imageny,45,32,colkey=0)

                #Draw barrels
                for i in self.barriles:
                    pyxel.blt(i.posx,i.posy, 0,i.imagenx,i.imageny, 12, 12, colkey=0)

                #Draw platforms
                for p in self.platforms:
                    pyxel.blt(p.posx,p.posy,0,p.imagenx,p.imageny,167,16,colkey=0)

                #Draw platform at the top
                pyxel.blt(70,32,0,88,0,101,16,colkey=0)

                #Draw ladders
                for r in range (0,5):
                    pyxel.blt(self.ladders[r].posx,self.ladders[r].posy,0,224,72,6,32,colkey=0)

                #Draw broken ladder
                pyxel.blt(self.ladderb.posx,self.ladderb.posy,0,232,72,6,32,colkey=0)
               
                #Draw barrel next to donkey
                pyxel.blt(40,48,0,12,104,16,16,colkey=0)
                

                #Draw mario looking to the left
                if pyxel.btn(pyxel.KEY_LEFT) and self.objMario.inLadder==False:
                    pyxel.blt(self.objMario.posx,self.objMario.posy,0,5,32,12,15,colkey=0)

                #Draw mario going up the ladders
                elif self.objMario.inLadder==True:
                    pyxel.blt(self.objMario.posx,self.objMario.posy,0,78,32,12,15,colkey=0)

                #Draw mario going to the right and when he isn't moving
                else:
                    pyxel.blt(self.objMario.posx,self.objMario.posy, 0,5, 32, -12, 15, colkey=0)
            

################ main program ##################
Game()   


