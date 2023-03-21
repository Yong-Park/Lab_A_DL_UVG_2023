import string
import graphviz
import os
os.environ["PATH"] += os.pathsep + 'D:/Program Files (x86)/Graphviz2.38/bin/'
class Subset():
    
    def __init__(self,afn,slPoint,r):
        self.eps = "ε"
        self.afn = afn
        self.start = slPoint[0][0]
        self.finish= slPoint[0][1]
        self.elements = r
        self.lenguaje = []
        self.alfabeto = list(string.ascii_uppercase)
        self.obtainElement()
        
        #en este se guardaran todos los nuevos elementos que se crean 
        self.newElement = []
        #este se agregara igual que el newElement pero al final este tiene que estar vacio
        self.stackElement = []
        #en este se guarda el stack del alfabeto
        self.stackAlfabet = []
        # en este se guardara todos las transacciones tipo A -> B si a y asi
        self.transaction = []
        
        #estos son los iniciales y finales a enviar
        self.sfAlfabet = []
    
    def obtainElement(self):
        # print("elements: ", self.elements)
        for l in self.elements:
            if l not in "•*|+?ε": 
                if l not in self.lenguaje:
                    self.lenguaje.append(l)
        # print("lenguaje: ", self.lenguaje)
        
    def afnConstruction(self):
        #este es la primera construccion que se realiza
        newArray = []
        # print(self.afn)
        #revisar todos los que este self.start puede visitar utilizando el epsilon
        #pero primero agregar estos elementos como parte de un array nuevo
        newArray.append(self.start)
            
        # print("el array que recibio para realizar la busqueda de eclousure: ", newArray)
        #agregar todos aquellos que puede visitar por epsilon
        for elem in newArray:
            for node in self.afn:
                if node[0] in newArray and node[1] == self.eps:
                    if node[2] not in newArray:
                        newArray.append(node[2])
        #ordenarlos y luego si no existe en la tabla agregarlo            
        newArray = sorted(newArray)
        if newArray not in self.newElement:
            self.newElement.append(newArray)
            self.stackElement.append(newArray)
            self.stackAlfabet.append(self.alfabeto.pop(0))
        #se realizara el movieminto y eclousure siempre y cuando el elemento no este vacio
        # print("newElement: ",self.newElement )
        # print("stackElement: ", self.stackElement)
        # print("stackAlfabet: ", self.stackAlfabet)
        self.cicle()
        
        #regresar la transaccion y sus iniciales y finales
        return [self.transaction,self.sfAlfabet]
        
    def cicle(self):
        while self.stackElement:
            stack = self.stackElement.pop(0)
            self.move(stack)
        # print("_____Transactions____________")
        # print(self.transaction)
        #encontrar sus nodos iniciales y finales
        start = []
        end = []
        empty = []
        # print("new element: ", self.newElement)
        # print("alfabet: ", self.stackAlfabet)
        for node in self.newElement:
            if self.start in node:
                indice = self.newElement.index(node)
                start.append(self.stackAlfabet[indice])
            if self.finish in node:
                indice = self.newElement.index(node)
                end.append(self.stackAlfabet[indice])
            if len(node) == 0:
                indice = self.newElement.index(node)
                empty.append(self.stackAlfabet[indice])
        # print("start: ", start)
        # print("end: ", end)
        # print("empy: ",empty)
        #agregar los que son inicial y final
        self.sfAlfabet.append(start)
        self.sfAlfabet.append(end)
        self.sfAlfabet.append(empty)

    def move(self,array):
        # print("Elementos eclosure: ", array)
        for tran in self.lenguaje:  #a,b
            temporalArray = []
            # print(tran)
            for start in array:
                for node in self.afn:
                    if node[0] == start and node[1] == tran:
                        if node[2] not in temporalArray:
                            temporalArray.append(node[2])
            #enviar este para encontrar su eclousure y de este ver si existe o no
            temporalArray = sorted(temporalArray)
            # print("los move encontrados: ", temporalArray)
            #obtener el indice para obtener su alfabeto concreto
            indice = self.newElement.index(array)
            if len(temporalArray) != 0:
                self.transaction.append([self.stackAlfabet[indice],tran,self.eClosure(temporalArray)])
        #     print("Transaction: ",self.transaction)
        #     print("todos los elementos que existe: ", self.newElement)
        # print("_____________________")

    def eClosure(self,array):
        #este es la primera construccion que se realiza
        newArray = []
        # print(self.afn)
        #revisar todos los que este self.start puede visitar utilizando el epsilon
        #pero primero agregar estos elementos como parte de un array nuevo
        if type(array) == type([]):
            newArray.extend(array)
        else:
            newArray.append(array)
            
        # print("el array que recibio para realizar la busqueda de eclousure: ", newArray)
        #agregar todos aquellos que puede visitar por epsilon
        for elem in newArray:
            for node in self.afn:
                if node[0] in newArray and node[1] == self.eps:
                    if node[2] not in newArray:
                        newArray.append(node[2])
        #ordenarlos y luego si no existe en la tabla agregarlo            
        newArray = sorted(newArray)
        # print("Array: ", newArray)
        if newArray not in self.newElement:
            self.newElement.append(newArray)
            self.stackElement.append(newArray)
            self.stackAlfabet.append(self.alfabeto.pop(0))
        
        #obtener el indice para obtener su alfabeto concreto
        indice = self.newElement.index(newArray)
        return self.stackAlfabet[indice]
    
    def afdGraph(self,afd,sfPoint):
        inicio = sfPoint[0]
        final = sfPoint[1]
        q_list = []
        q = list(string.ascii_uppercase)
        
        #guardar los valores de q utilizados
        for l in afd:
            for q_search in q:
                if q_search in l:
                    if q_search not in q_list:
                        q_list.append(q_search)
                        
        f = graphviz.Digraph(comment = "afd")
        inicio_listo = True
        
        for name in q_list:
            if name in final:
                f.node(str(name), shape="doublecircle",fillcolor="#ee3b3b",style="filled")
            elif name in inicio:
                f.node(str(name),fillcolor="#7fff00",style="filled")
            else:
                f.node(str(name))
        f.node("", shape="plaintext")
        for l in afd:
            for val in inicio:
                if val in l:
                    if(inicio_listo):
                        f.edge("",str(l[0]),label = "")
                        inicio_listo = False
            f.edge(str(l[0]),str(l[2]),label = str(l[1]))
            
        f.render("afd", view = True)