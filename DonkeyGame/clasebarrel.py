import random

class Barrel:

    #Barrels' class

    imagenx=35
    imageny=106
    
    def __init__(self, x, y):
        #Barrels' positions
        self.__posx=x
        self.__posy=y
        #Direction of the barrel
        self.__direction=True
        

    @property
    def posx(self):
        return self.__posx   
    
    @property
    def posy(self):
        return self.__posy
    
    
    def movebarrel(self,ladders=[],platforms=[]):
        '''This function makes the barrels move on the platforms, fall down at the
            end of the platformsand go down the ladders'''

        for c in platforms:

            #Barrels move to the right
            if (self.__posx)<(c.posx+167) and (self.__posy+11)==(c.posy) and self.__direction:
                self.__posx+=1

            #Barrels move down at the right end of the platforms
            elif (self.__posx)>=(c.posx+167) and (self.__posy+11)==(c.posy) and self.__direction:
                    for _ in range(32):
                        self.__posy+=1
                    #Barrels change direction when they fall  
                    self.__direction=not self.__direction

            #Barrels move down at the left end of the platforms
            elif (self.__posx+11)<=(c.posx) and (self.__posy+11)==(c.posy) and not self.__direction:
                    for _ in range(32):
                        self.__posy+=1
                    self.__direction=not self.__direction

            #Barrels move to the left
            elif (self.__posx+11)>(c.posx) and (self.__posy+11)==(c.posy) and not self.__direction:
                self.__posx-=1

            
            for b in ladders:

                    #Barrels go down the ladders with a 25% chance
                    if (self.__posx)==(b.posx) and (self.__posy+11)==(b.posy):
                        pr=random.randint(1,4)

                        if pr==1:
                            #When they go down they change their direction
                            self.__direction=not self.__direction
                            for _ in range(32):
                                self.__posy+=1
