class Ladder:

    #Ladders' class
    
    def __init__(self, x, y, broken):
        #Ladders' positions
        self.__posx=x
        self.__posy=y
        #If ladders are broken or not
        self.__broken=broken

    @property
    def broken(self):
        return self.__broken
        
    @property
    def posx(self):
        return self.__posx   
    
    @property
    def posy(self):
        return self.__posy
