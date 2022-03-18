class Prince:

    #Prince's class

    imagenx=38
    imageny=16
    
    def __init__(self, x, y):
        #Prince's position
        self.__posx=x
        self.__posy=y
        
    @property
    def posx(self):
        return self.__posx   
    
    @property
    def posy(self):
        return self.__posy
