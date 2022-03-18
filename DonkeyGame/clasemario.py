class Mario:
    
    #Mario's class
  
    def __init__(self, x, y, when=0, jumping=False, score=0, lives=3):
        #Mario's position
        self.__posx=x
        self.__posy=y
        #If Mario is in a ladder
        self.__inLadder=False
        #If Mario is jumping
        self.__jumping=jumping
        #Used to jump
        self.__when=when
        #Stores Mario's score
        self.__score=score
        #Mario's lives
        self.__lives=lives

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self):
        return self.__score

    @property
    def lives(self):
        return self.__lives

    @lives.setter
    def lives(self):
        return self.__lives
    @property
    def posx(self):
        return self.__posx   
    
    @property
    def posy(self):
        return self.__posy

    @property
    def when(self):
        return self.__when
    
    @when.setter
    def when(self, value):
        self.__when=value

    @property
    def jumping(self):
        return self.__jumping
    
    @jumping.setter
    def jumping(self, value):
        self.__jumping=value 

    @property
    def inLadder(self):
        return self.__inLadder
    


    def newmove(self,d,ladders=[],platforms=[]):
        '''This function makes mario move'''

        #Mario moves to the left when he isn't in a ladder
        if d == 'left' and self.__inLadder==False and self.__posx>0:
            self.__posx-=2

            #Mario falls down at the left end of the platforms
            for c in range(len(platforms)-1):
                if (self.__posx+11)<(platforms[c].posx) and (self.__posy+15)==(platforms[c].posy):
                    for _ in range(32):
                        self.__posy+=1

        #Mario moves to the right when he isn't in a ladder
        elif d == 'right' and self.__inLadder==False and self.__posx<244:
            self.__posx+=2

            #Mario falls down at the right end of the platforms
            for c in range (len(platforms)-1):
                if (self.__posx)>(platforms[c].posx+165) and (self.__posy+15)==(platforms[c].posy):
                    for _ in range(32):
                       self.__posy+=1

        #Mario goes up the ladders            
        elif d == 'up':
            for k in ladders:
                if (self.__posx + 6) in range(k.posx,k.posx+6) and (self.__posy) in range(k.posy-14,k.posy+18) and k.broken==False:
                    self.__posy-=1
                    self.__inLadder=True 
                elif (self.__posx + 6) in range(k.posx,k.posx+6) and (self.__posy) in range(k.posy-15,k.posy): 
                    self.__inLadder=False

        #Mario goes down the ladders
        elif d == 'down':
            for k in ladders:
                if (self.__posx + 6) in range(k.posx,k.posx+6) and (self.__posy) in range(k.posy-16,k.posy+17) and k.broken==False:
                    self.__posy+=1
                    self.__inLadder=True
                elif (self.__posx + 6) in range(k.posx,k.posx+6) and (self.__posy) in range(k.posy+17,k.posy+32): #and k.broken==False:     
                    self.__inLadder=False
                    
    def jump(self):
        '''This function makes Mario jump'''
        self.__posy-=16
        self.__jumping=True

    def desjump(self):
        '''This function makes Mario fall down again after jumping'''
        self.__posy+=16
        self.__jumping=False

    def scoreMario(self):
        '''This function adds 100 points to the score everytime Mario jumps a barrel'''
        self.__score+=100
    

    def death(self):
        '''This function takes one life from Mario everytime he touches a barrel'''
        self.__lives-=1
        self.__score=0
        #Everytime Mario dies he appears in this position
        self.__posx=20
        self.__posy=177
        
