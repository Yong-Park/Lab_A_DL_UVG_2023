import string
import graphviz
import os
os.environ["PATH"] += os.pathsep + 'D:/Program Files (x86)/Graphviz2.38/bin/'

class DirectAfd:
    def __init__(self,postfix):
        self.postfix = postfix
        #agregar el # de ultimo para la cadena
        self.postfix.append('#')
        self.postfix.append('.')
        # Nueva lista vacía que se utiliza para ordenar correspondientemente cuando se obtienen los valores
        self.nueva_lista = []

        self.deletable_firstPos = []
        self.deletable_lastPos = []
        self.deletable_nullable = []

        self.newPostfix = []
        self.nullable= []
        self.firstPos= []
        self.lastPos = []
        self.followPos = [] 
        self.q = []
        self.enumerate()
        self.startConstruct()
        self.follopostConstruct()
    
    #en este se enumeraran los estados correspondientes
    def enumerate(self):
        #generar un listado de numeros de 1 - 1000
        for i in range(1,1000):
            value = i
            self.q.append(value)
        
        #si los valores son distintos a *|.?+ darles un valor numerico
        for x in self.postfix:
            if x not in '*|.?+ε':
                self.newPostfix.append(self.q.pop(0))
            else:
                self.newPostfix.append(x)
        # print("old postfix: ",self.postfix)
        # print("nuevo postfix: ",self.newPostfix)

    #se comenzara a armar lo necesario para obtner los conjuntos y asi en los que eston van a viajar
    def startConstruct(self):
        for node in self.newPostfix:
            if str(node) in '*|.?+ε':
                if node == '*':
                    self.nullable.append(True)
                    self.firstPos.append(self.firstPos[len(self.firstPos)-1])
                    self.lastPos.append(self.firstPos[len(self.firstPos)-1])
                elif node == '|':
                    #revisar si es nullable
                    c1 = self.nullable[len(self.nullable)-2]
                    c2 = self.nullable[len(self.nullable)-1]
                    if c1 == True or c2 == True:
                        self.nullable.append(True)
                    else:
                        self.nullable.append(False)
                    #agregar el firstpos
                    first = []
                    first.extend(self.firstPos[len(self.firstPos)-2])
                    first.extend(self.firstPos[len(self.firstPos)-1])
                    self.firstPos.append(first)
                    #agregar el lastpos
                    last = []
                    last.extend(self.lastPos[len(self.lastPos)-2])
                    last.extend(self.lastPos[len(self.lastPos)-1])
                    self.lastPos.append(last)
                elif node == '.':
                    #revisar si es nullable
                    c1 = self.nullable[len(self.nullable)-2]
                    c2 = self.nullable[len(self.nullable)-1]
                    if c1 == True and c2 == True:
                        self.nullable.append(True)
                    else:
                        self.nullable.append(False)
                    #agregar el firstpos
                    if c1 == True:
                        first = []
                        first.extend(self.firstPos[len(self.firstPos)-2])
                        first.extend(self.firstPos[len(self.firstPos)-1])
                        self.firstPos.append(first)
                    else:
                        first = []
                        first.extend(self.firstPos[len(self.firstPos)-2])
                        self.firstPos.append(first)
                    #agregar el lastpos
                    if c2 == True:
                        last = []
                        last.extend(self.lastPos[len(self.lastPos)-2])
                        last.extend(self.lastPos[len(self.lastPos)-1])
                        self.lastPos.append(last)
                    else:
                        last = []
                        last.extend(self.lastPos[len(self.lastPos)-1])
                        self.lastPos.append(last)
                elif node == '?':
                    self.nullable.append(True)
                    self.firstPos.append(self.firstPos[len(self.firstPos)-1])
                    self.lastPos.append(self.lastPos[len(self.lastPos)-1])
                elif node == '+':
                    #revisar si es nullabel
                    c1 = self.nullable[len(self.nullable)-1]
                    if c1 == True:
                        self.nullable.append(True)
                    else:
                        self.nullable.append(False)
                    #insertar el firstpos y lastpos
                    self.firstPos.append(self.firstPos[len(self.firstPos)-1])
                    self.lastPos.append(self.lastPos[len(self.lastPos)-1])
                elif node == 'ε':
                    self.nullable.append(True)
                    self.firstPos.append('∅')
                    self.lastPos.append('∅')
            else:
                self.nullable.append(False)
                self.firstPos.append([node])
                self.lastPos.append([node])

                self.deletable_nullable.append(False)
                self.deletable_firstPos.append([node])
                self.deletable_lastPos.append([node])

        print("node: ", self.newPostfix)
        print("nullable: ", self.nullable)
        print("firstpos: ", self.firstPos)
        print("lastpos: ", self.lastPos)
        
    def follopostConstruct(self):
        #guardar todos los valores para el followpost
        for val in range(len(self.newPostfix)):
            if str(self.newPostfix[val]) not in "*?.+|":
                self.followPos.append([self.newPostfix[val]])
                
        for val in range(len(self.newPostfix)):
            isnodes = []
            addnodes = []
            
            if self.newPostfix[val] == "*":
                isnodes.extend(self.lastPos[val])
                addnodes.extend(self.firstPos[val])
                
                for nod in range(len(self.followPos)):
                    if self.followPos[nod][0] in isnodes:
                        if len(self.followPos[nod]) > 1:
                            for x in addnodes:
                                if x not in self.followPos[nod][1]:
                                    self.followPos[nod][1].extend(addnodes)
                        else:
                            self.followPos[nod].append(addnodes)
                            
            elif self.newPostfix[val] == "+":
                isnodes.extend(self.lastPos[val])
                addnodes.extend(self.firstPos[val])
                
                for nod in range(len(self.followPos)):
                    if self.followPos[nod][0] in isnodes:
                        if len(self.followPos[nod]) > 1:
                            for x in addnodes:
                                if x not in self.followPos[nod][1]:
                                    self.followPos[nod][1].extend(addnodes)
                        else:
                            self.followPos[nod].append(addnodes)
            
            elif self.newPostfix[val] == ".":
                c1 = val - 2
                c2 = val - 1
                isnodes.extend(self.lastPos[c1])
                addnodes.extend(self.firstPos[c2])
                
                for nod in range(len(self.followPos)):
                    if self.followPos[nod][0] in isnodes:
                        if len(self.followPos[nod]) > 1:
                            for x in addnodes:
                                if x not in self.followPos[nod][1]:
                                    self.followPos[nod][1].extend(addnodes)
                        else:
                            self.followPos[nod].append(addnodes)
                            
                            
        #agregar el ultimo un signo ∅ ya que es el # 
        self.followPos[len(self.followPos)-1].append(["∅"])
        
        print("followpos: ",self.followPos)
        
    def Dstate(self):
        #nodo inicial
        # print(self.followPos)
        sNode = self.followPos[0][1]
        #nodo final
        final = self.followPos[len(self.followPos)-1][0]
        #aqui tendra todos los nodos de los cuales viajara
        P0 = []
        P0.append(sNode)
        #obtener las variables que utiliza
        variables = []
        for x in self.postfix:
            if x not in "|.*+?#":
                if x not in variables:
                    variables.append(x)
        # print("variables: ", variables)
        
        tabla = []
        for x in P0:                #[1,2,3]
            # print("x: ", x)
            conjuntos = []
            conjuntos.append(x)
            for alfa in variables:  #a, b
                # print("alfa: ",alfa)
                movement = []
                movement.append(alfa)
                con = []
                for y in x:         #1,2,3
                    # print("y: ", y)
                    for l in range(len(self.postfix)):
                        if self.newPostfix[l] == y and self.postfix[l] == alfa:
                            for w in self.followPos:
                                if w[0] == y:
                                    for z in w[1]:
                                        if z not in con:
                                            con.append(z)
                con.sort
                if con not in P0:
                    P0.append(con)
                movement.append(con)
                # print("movement: ",movement)
                conjuntos.append(movement)
                # print("conjuntos: ", conjuntos)
                if conjuntos not in tabla:
                    tabla.append(conjuntos)
        # print("tabla: ", tabla)

        for sublist in tabla:
            new_sublist1 = [sublist[0], sublist[1][0], sublist[1][1]]
            new_sublist2 = [sublist[0], sublist[2][0], sublist[2][1]]
            self.nueva_lista.append(new_sublist1)
            self.nueva_lista.append(new_sublist2)

        # Impresión de la nueva lista
        # print(self.nueva_lista
        
        #convertir la nueva lista en A,B,C ...
        q = list(string.ascii_uppercase)
        #obtener todos los nodos
        node = []
        alfanode = []
        for x in self.nueva_lista:
            if x[0] not in node:
                node.append(x[0])
                alfanode.append(q.pop(0))
        # print("node: ",node)
        # print("alfanode: ",alfanode)
        
        #comenzar a reemplazarlo por alfabetos
        for x in self.nueva_lista:
            for y in range(len(node)):
                if x[0] == node[y]:
                    x[0] = alfanode[y]
                if x[2] == node[y]:
                    x[2] = alfanode[y]
        # print("nueva lista actualizada: ", self.nueva_lista)
        
        start = []
        end = []
        #obtener los nuevos iniciales y finales
        
        for ele in range(len(node)):
            if node[ele] == sNode:
                start.extend(alfanode[ele])
            elif final in node[ele]:
                end.extend(alfanode[ele])
        #se guardan los nuevos iniciales y finales correspondientes
        # print(start)
        # print(end)
        
        sfPoint=[]
        sfPoint.append(start)
        sfPoint.append(end)  
            
        
        return [self.nueva_lista,sfPoint]
    
    def DirectGraph(self,directAFD,sfPoint):
        # print(sfPoint)
        inicio = sfPoint[0]
        final = sfPoint[1]
        q_list = []
        q = list(string.ascii_uppercase)
        # print(directAFD)

        #guardar los valores de q utilizados
        for l in directAFD:
            for q_search in q:
                if q_search in l:
                    if q_search not in q_list:
                        q_list.append(q_search)

        f = graphviz.Digraph(comment = "afd Directo")
        inicio_listo = True
        
        for name in q_list:
            if name in final:
                f.node(str(name), shape="doublecircle",fillcolor="#ee3b3b",style="filled")
            elif name in inicio:
                f.node(str(name),fillcolor="#7fff00",style="filled")
            else:
                f.node(str(name))
        f.node("", shape="plaintext")
        for l in directAFD:
            for val in inicio:
                if val in l and l[0] == val:
                    if(inicio_listo):
                        f.edge("",str(l[0]),label = "")
                        inicio_listo = False
            f.edge(str(l[0]),str(l[2]),label = str(l[1]))
            
        f.render("afd Directo", view = True)
        
                
                
                