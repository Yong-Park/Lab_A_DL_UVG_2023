import string

class Minimizacion():
    def __init__(self,afd,sfpoint):
        self.afd = afd
        self.inicio = sfpoint[0]
        self.final = sfpoint[1]
        self.P0 = []
        self.aceptacion = []
        self.noAceptacion = []
        self.alfabeto = []
        self.equivalents = []
        self.extra = []
        self.obtainValues()
        self.startFunction()
        
        
    def obtainValues(self):
        #guardar las cadenas segun son terminales o no
        for element in self.afd:
            if element[0] in self.final:
                if element[0] not in self.aceptacion:
                    self.aceptacion.append(element[0])
            else:
                if element[0] not in self.noAceptacion:
                    self.noAceptacion.append(element[0])
                    
        # print(self.noAceptacion)
        # print(self.aceptacion)
        
        #estos son los 0-equivalentes
        self.P0.append(self.noAceptacion)
        self.P0.append(self.aceptacion)
        
        #obtener los alfabetos
        for element in self.afd:
            if element[1] != "ε":
                if element[1] not in self.alfabeto:
                    self.alfabeto.append(element[1])
                    
        print(self.P0)
        
    def startFunction(self):
        contador = 1
        largo = 0
        tabla = []
        while(largo != len(self.P0)):
            largo = len(self.P0)
            
            #comenzar con la rotacion de equivalentes
            for x in self.P0:
                if len(x) > 1:
                    for y in x:
                        for alfa in self.alfabeto:
                            conjuntos = []
                            conjuntos.append(y)
                            for transaction in self.afd:
                                if transaction[0] == y and transaction[1] == alfa:
                                    conjuntos.append(alfa)
                                    for w in self.P0:
                                        if transaction[2] in w:
                                            conjuntos.append(w)
                                            if conjuntos not in tabla:
                                                tabla.append(conjuntos)
        print(tabla)
                        
                    
                    