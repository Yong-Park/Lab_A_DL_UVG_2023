import string
import graphviz
import os
os.environ["PATH"] += os.pathsep + 'D:/Program Files (x86)/Graphviz2.38/bin/'

class Minimizacion():
    def __init__(self,afd,sfpoint):
        self.afd = afd
        self.inicio = sfpoint[0]
        self.final = sfpoint[1]
        self.empty = sfpoint[2]
        self.P0 = []
        self.aceptacion = []
        self.noAceptacion = []
        self.alfabeto = []
        self.finalTransaction = []
        self.obtainValues()
        
    def obtainValues(self):
        #guardar las cadenas segun son terminales o no
        for element in self.afd:
            if element[0] in self.final:
                if element[0] not in self.aceptacion:
                    self.aceptacion.append(element[0])
            else:
                if element[0] not in self.noAceptacion and element[0] not in self.empty:
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
                    
        # print(self.P0)
        
    def startFunction(self):
        largo = 0
        while(largo != len(self.P0)):
            largo = len(self.P0)
            #comenzar con la rotacion de equivalentes
            for x in self.P0:
                tabla = []
                # print("x: ", x)
                if len(x) > 1:
                    for y in x:
                        conjuntos = []
                        conjuntos.append(y)
                        for alfa in self.alfabeto:
                            movement = []
                            for transaction in self.afd:
                                if transaction[0] == y and transaction[1] == alfa:
                                    movement.append(alfa)
                                    for w in range(len(self.P0)):
                                        if transaction[2] in self.P0[w]:
                                            movement.append(w)
                                            conjuntos.append(movement)
                        if conjuntos not in tabla:
                            tabla.append(conjuntos)
                    # print("tabla: ", tabla)
                    
                    #juntarlos por sus similitudes
                    groups = {}
                    # print("_________Similitudes_______")
                    # Recorremos la lista y agrupamos los elementos según la condición especificada
                    for item in tabla:
                        # print("item: ", item)
                        key = tuple(sorted([str(subitem[0])+str(subitem[1]) for subitem in item[1:]]))
                        
                        # print("key: ", key)
                        if key in groups:
                            groups[key].append(item[0])
                        else:
                            groups[key] = [item[0]]
                        # print("groups: ", groups)
                        # print("__")

                    # Convertimos el diccionario en una lista de listas
                    result = [group for group in groups.values()]
                    
                    self.P0.remove(x)
                    self.P0.extend(result)

        #             print("Resultados: ", result)

                                                
        #             print("P0: ", self.P0)
        #             print("=====================")
        # print("final: ", self.final)
        # print("inicio: ", self.inicio)
        start = []
        end = []
        #obtener los nuevos iniciales y finales
        for item in self.P0:
            if any(x in self.final for x in item):
                end.append(item[0])
            elif any(x in self.inicio for x in item):
                start.append(item[0])
        #se guardan los nuevos iniciales y finales correspondientes
        self.inicio = start
        self.final = end

        # print(self.inicio)
        # print(self.final)
                    
        #obtener sus transaciones de cada uno
        for value in self.P0:
            for alfa in self.alfabeto:
                for transaction in self.afd:
                    if transaction[0] == value[0] and transaction[1] == alfa:
                        for inside in self.P0:
                            if transaction[2] in inside:
                                self.finalTransaction.append([transaction[0],transaction[1],inside[0]])
        
        # print(self.inicio)
        # print(self.final)
        sfPoint=[]
        sfPoint.append(self.inicio)
        sfPoint.append(self.final)    
        # print(self.finalTransaction)
        return [self.finalTransaction,sfPoint]

    def minimizacionGraph(self,afdMinimizado,sfPoint):
        # print(sfPoint)
        inicio = sfPoint[0]
        final = sfPoint[1]
        q_list = []
        q = list(string.ascii_uppercase)
        # print(afdMinimizado)

        #guardar los valores de q utilizados
        for l in afdMinimizado:
            for q_search in q:
                if q_search in l:
                    if q_search not in q_list:
                        q_list.append(q_search)

        f = graphviz.Digraph(comment = "afd Minimizado")
        inicio_listo = True
        
        for name in q_list:
            if name in final:
                f.node(str(name), shape="doublecircle",fillcolor="#ee3b3b",style="filled")
            elif name in inicio:
                f.node(str(name),fillcolor="#7fff00",style="filled")
            else:
                f.node(str(name))
        f.node("", shape="plaintext")
        for l in afdMinimizado:
            for val in inicio:
                if val in l and l[0] == val:
                    if(inicio_listo):
                        f.edge("",str(l[0]),label = "")
                        inicio_listo = False
            f.edge(str(l[0]),str(l[2]),label = str(l[1]))
            
        f.render("afd Minimizado", view = True)

                        
                    
                    