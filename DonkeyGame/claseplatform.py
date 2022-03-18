class Platform:

    #Platforms' class

    imagenx=88
    imageny=0
    
    def __init__(self, x, y):
        #Platforms' positions
        self.__posx=x
        self.__posy=y
        
    @property
    def posx(self):
        return self.__posx   
    
    @property
    def posy(self):
        return self.__posy
