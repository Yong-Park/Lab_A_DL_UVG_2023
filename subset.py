class Subset():
    
    def __init__(self,afn,slPoint,r):
        self.afn = afn
        self.start = slPoint[0][0]
        self.finish= slPoint[0][1]
        self.elements = r
        self.lenguaje = []
        self.obtainElement()
    
    def obtainElement(self):
        for l in self.elements:
            if l not in ".*|": 
                if l not in self.lenguaje:
                    self.lenguaje.append(l)
                    
        print(self.lenguaje)
    
    def eClosure(self):
        pass
    
    def move(self):
        pass