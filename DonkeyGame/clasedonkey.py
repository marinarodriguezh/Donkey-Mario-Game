class Donkey:

    #Donkey's class
    
    imagenx=5
    imageny=56
    
    def __init__(self, x, y):
        #Donkey's position 
        self.__posx=x
        self.__posy=y
        
    @property
    def posx(self):
        return self.__posx   
    
    @property
    def posy(self):
        return self.__posy
