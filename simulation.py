class Simulation:
    
    def afnSimulation(self,afn,sfPoints,cadena):
        point = sfPoints[0][0]
        end = sfPoints[0][1]
        caminos = []
        eps = 'ε'
        alfabeto = []
        
        #obtener el alfabeto
        for x in afn:
            if x[1] not in alfabeto and x[1] != "ε":
                alfabeto.append(x[1])
        alfabeto.sort()
        # print("alfabeto: ", alfabeto)
        
        # print("start :", point)
        # print("end: ",end)
        
        caminos.append([point])
        # print("caminos: ", caminos)
        # print(afn)
        # print("===================")
        
        for c in cadena:
            i = 0
            # print(c)
            # print("len caminos :",len(caminos))
            # print("i: ", i)
            while i  != len(caminos):
                
                
                #obtener todos los nodos que llega con epsilon
                i = len(caminos)
                # print("new i: ", i)
                for camino in caminos:
                    for p in camino:
                        for x in afn:
                            if p == x[0] and x[1] == eps:
                                if x[2] not in camino:
                                    camino.append(x[2])
                           
            # print("caminos epsilon: ", caminos)
            #buscar los que llegan a un lado y agregarlos como uno nuevo
            largo = len(caminos)
            camino_borrable = []
            for camino in caminos:
                for p in camino:
                    for x in afn:
                        if p == x[0] and x[1] == c:
                            camino_borrable.append([x[2]])
            caminos.extend(camino_borrable)
            #eliminiar las de epsilon
            for i in range(largo):
                caminos.pop(0)
                        
            # print("caminos valor: ", caminos)
            # print("==================")
        
        
        #realizar un ultimo movimiento del epsilon si en dado caso tiene 
        i = 0
        while i  < len(caminos):
            #obtener todos los nodos que llega con epsilon
            i = len(caminos)
            for camino in caminos:
                for p in camino:
                    for x in afn:
                        if p == x[0] and x[1] == eps:
                            if x[2] not in camino:
                                camino.append(x[2])
        # print("camino final: ", caminos)
        #revisar si llego
        for x in caminos:
            if end in x:
                return True
            
        return False
        
  
    def afdSimulation(self,afd,sfPoints,cadena):
        point = sfPoints[0]
        end = sfPoints[1]
        caminos = []
        alfabeto = []
        
        caminos.extend(point)
        # print("caminos: ",caminos)
        #obtener el alfabeto
        for x in afd:
            # print(x)
            if x[1] not in alfabeto and x[1] != "ε":
                alfabeto.append(x[1])
        alfabeto.sort()
        # print("alfabeto: ", alfabeto)
        # print("afd: ", afd)
        # print("start: ",point)
        # print("end: ",end)
        for c in cadena:
            camino_borrable = []
            for p in caminos:
                for x in afd:
                    if p == x[0] and x[1] == c:
                        # print("p: ",p)
                        # print("afd: ",x)
                        camino_borrable.append(x[2])
                    if c == "ε":
                        camino_borrable.append(x[0])


            caminos = camino_borrable
            # print("caminos: ",caminos)

        #revisar si llego
        for i in end:
            if i in caminos:
                return True
        return False
                
    
    