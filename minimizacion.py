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
        self.finalTransaction = []
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
        while(largo != len(self.P0)):
            largo = len(self.P0)
            
            #comenzar con la rotacion de equivalentes
            for x in self.P0:
                tabla = []
                print("x: ", x)
                if len(x) > 1:
                    for y in x:
                        for alfa in self.alfabeto:
                            conjuntos = []
                            conjuntos.append(y)
                            for transaction in self.afd:
                                if transaction[0] == y and transaction[1] == alfa:
                                    conjuntos.append(alfa)
                                    for w in range(len(self.P0)):
                                        if transaction[2] in self.P0[w]:
                                            conjuntos.append(w)
                                            if conjuntos not in tabla:
                                                tabla.append(conjuntos)
                    print("tabla: ", tabla)
                    
                    #juntarlos por sus similitudes
                    grupos = {}

                    for estado in tabla:
                        letra = estado[1]
                        valor = estado[2]
                        clave = f"{letra}_{valor}"
                        if clave in grupos:
                            grupos[clave].append(estado[0])
                        else:
                            grupos[clave] = [estado[0]]

                    resultado = list(grupos.values())
                    resultado.remove(x)
                    
                    self.P0.remove(x)
                    self.P0.extend(resultado)

                    print("Resultados: ", resultado)

                                                
                    print("P0: ", self.P0)
                    print("=====================")
                    
        #obtener los nuevos iniciales y finales
        for x in self.P0:
            if len(x) > 1:
                if self.final in x:
                    print("si esta el final")
                    self.final = [x[0]]
                elif self.inicio in x:
                    print("si esta el inicio")
                    self.inicio = [x[0]]
                    
        #obtener sus transaciones de cada uno
        for value in self.P0:
            for alfa in self.alfabeto:
                for transaction in self.afd:
                    if transaction[0] == value[0] and transaction[1] == alfa:
                        for inside in self.P0:
                            if transaction[2] in inside:
                                self.finalTransaction.append([transaction[0],transaction[1],inside[0]])
        
        print(self.inicio)
        print(self.final)       
        print(self.finalTransaction)
                        
                    
                    