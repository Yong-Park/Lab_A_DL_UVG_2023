import graphviz
import os
os.environ["PATH"] += os.pathsep + 'D:/Program Files (x86)/Graphviz2.38/bin/'

class Thompson:
    
    def __init__(self):
        self.eps = "ε"
        self.q = []
        self.afn_control = []
        #este guardara absolutamente todos los estados y sus conexiones sin separarlos
        self.afn = []

        #en esta se guardaran las estados primarios y finales de cada cadena
        self.cadena_fl = []
        #en este se guardaran todas los estados que fueron creados todo por aparte en caso que no esten directamente relacionados
        self.cadena = []
        self.list = []
        #se encarga de crear los estados
        self.estados()
        
    #se encarga de crear 1000 estados a utilizar
    def estados(self):
        for i in range(1000):
            value = i
            self.q.append(value)
            
    def construccion_thompson(self, output):
        # print(output)
        #este se llenara con los chain, donde al final se ve si con ello se crea un una nueva cadena o solo se le realiza el extend.
        self.lista = []
        #utilizado solo para crear los movimientos de estados para luego limpiarlo despues de una ejecucion
        self.chain = []
        for l in output:
            self.list.append(l)
            # print("===========")
            # print("list: ", self.list)
            if self.list[len(self.list)-1] == "|":
                self.orFunction()
            elif self.list[len(self.list)-1] == "*":
                self.kleenFunction()
            elif self.list[len(self.list)-1] == ".":
                self.andFunction()
            elif self.list[len(self.list)-1] == "+":
                self.kleenPositiveFunction()
            else:
                self.createState()
            # print("afn: ", self.afn)
            # print("cadena: ", self.cadena)
            # print("first and last de cadena: ", self.cadena_fl)
        return [self.afn, self.cadena_fl]

    def createState(self):
        #creacion de los dos estados y su conexion
        self.chain.append(self.q[0])
        self.chain.append(self.list[len(self.list)-1])
        self.chain.append(self.q[1])
        self.lista.append(self.chain)
        self.afn.append(self.chain)
        self.chain = []
    
        self.cadena.append(self.lista)
        self.lista = []
            
        fl = []
        fl.append(self.q[0])    #first
        fl.append(self.q[1])    #last

        self.cadena_fl.append(fl)
        
        self.q.pop(0)
        self.q.pop(0)
        
        self.list.pop(len(self.list)-1)
    
    def andFunction(self):
        #en lista crear agregar como uno por medio de extend
        for sublista in self.cadena:
            self.lista.extend(sublista)
        #crear la conexion entre las dos 
        self.chain.append(self.cadena_fl[len(self.cadena_fl)-2][1]) #utilizar el nodo final del primero
        self.chain.append(self.eps)
        self.chain.append(self.cadena_fl[len(self.cadena_fl)-1][0]) #utilizar el nodo primario del segundo
        self.lista.append(self.chain)
        self.afn.append(self.chain)
        self.chain = []

        self.cadena.append(self.lista) #agregar la nueva que esta unificada por medio de exten
        self.lista = []

        #eliminar los dos anteriores al nuevo agregado
        self.cadena.pop(len(self.cadena)-2)
        self.cadena.pop(len(self.cadena)-2)

        #obtener sus nuevos inciales y finales
        fl = []
        fl.append(self.cadena_fl[len(self.cadena_fl)-2][0]) 
        fl.append(self.cadena_fl[len(self.cadena_fl)-1][1])
        #agregarlo
        self.cadena_fl.append(fl)
        #eliminar los dos anteriores del nuevo agregaedo
        self.cadena_fl.pop(len(self.cadena_fl)-2)
        self.cadena_fl.pop(len(self.cadena_fl)-2)

        self.list.pop(len(self.list)-1)


    def orFunction(self):
        #en lista crear agregar como uno por medio de extend
        for sublista in self.cadena:
            self.lista.extend(sublista)
            
        #creacion de los dos estados y su conexion
        self.chain.append(self.q[0])
        self.chain.append(self.eps)
        self.chain.append(self.cadena_fl[len(self.cadena_fl)-2][0])
        self.lista.append(self.chain)
        self.afn.append(self.chain)
        self.chain = []
        
        self.chain.append(self.q[0])
        self.chain.append(self.eps)
        self.chain.append(self.cadena_fl[len(self.cadena_fl)-1][0])
        self.lista.append(self.chain)
        self.afn.append(self.chain)
        self.chain = []
        
        self.chain.append(self.cadena_fl[len(self.cadena_fl)-2][1])
        self.chain.append(self.eps)
        self.chain.append(self.q[1])
        self.lista.append(self.chain)
        self.afn.append(self.chain)
        self.chain = []
        
        self.chain.append(self.cadena_fl[len(self.cadena_fl)-1][1])
        self.chain.append(self.eps)
        self.chain.append(self.q[1])
        self.lista.append(self.chain)
        self.afn.append(self.chain)
        self.chain = []
        
        self.cadena.append(self.lista) #agregar la nueva que esta unificada por medio de exten
        self.lista = []
        
        #eliminar los dos anteriores al nuevo agregado
        self.cadena.pop(len(self.cadena)-2)
        self.cadena.pop(len(self.cadena)-2)
        
        #obtener sus nuevos inciales y finales
        fl = []
        fl.append(self.q[0]) 
        fl.append(self.q[1])
        #agregarlo
        self.cadena_fl.append(fl)
        #eliminar los dos anteriores del nuevo agregaedo
        self.cadena_fl.pop(len(self.cadena_fl)-2)
        self.cadena_fl.pop(len(self.cadena_fl)-2)
        
        self.q.pop(0)
        self.q.pop(0)
        
        self.list.pop(len(self.list)-1)
            
    def kleenFunction(self):
        #creacion de los dos estados y su conexion
        self.chain.append(self.q[0])
        self.chain.append(self.eps)
        self.chain.append(self.cadena_fl[len(self.cadena_fl)-1][0])
        self.lista.append(self.chain)
        self.afn.append(self.chain)
        self.chain = []

        self.chain.append(self.cadena_fl[len(self.cadena_fl)-1][1])
        self.chain.append(self.eps)
        self.chain.append(self.q[1])
        self.lista.append(self.chain)
        self.afn.append(self.chain)
        self.chain = []

        self.chain.append(self.q[0])
        self.chain.append(self.eps)
        self.chain.append(self.q[1])
        self.lista.append(self.chain)
        self.afn.append(self.chain)
        self.chain = []

        self.chain.append(self.cadena_fl[len(self.cadena_fl)-1][1])
        self.chain.append(self.eps)
        self.chain.append(self.cadena_fl[len(self.cadena_fl)-1][0])
        self.lista.append(self.chain)
        self.afn.append(self.chain)
        self.chain = []

        #agregar las nuevas a la cadena anterior del *
        self.cadena[len(self.cadena)-1].extend(self.lista)
        self.lista = []

        fl = []
        fl.append(self.q[0])
        fl.append(self.q[1])
        #agregar las nuevos inicial y final
        self.cadena_fl.append(fl)

        #eliminar el anterior del nuevo agregaedo
        self.cadena_fl.pop(len(self.cadena_fl)-2)

        self.q.pop(0)
        self.q.pop(0)

        self.list.pop(len(self.list)-1)

    def kleenPositiveFunction(self):
        #creacion de los dos estados y su conexion
        self.chain.append(self.q[0])
        self.chain.append(self.eps)
        self.chain.append(self.cadena_fl[len(self.cadena_fl)-1][0])
        self.lista.append(self.chain)
        self.afn.append(self.chain)
        self.chain = []

        self.chain.append(self.cadena_fl[len(self.cadena_fl)-1][1])
        self.chain.append(self.eps)
        self.chain.append(self.q[1])
        self.lista.append(self.chain)
        self.afn.append(self.chain)
        self.chain = []

        self.chain.append(self.cadena_fl[len(self.cadena_fl)-1][1])
        self.chain.append(self.eps)
        self.chain.append(self.cadena_fl[len(self.cadena_fl)-1][0])
        self.lista.append(self.chain)
        self.afn.append(self.chain)
        self.chain = []

        #agregar las nuevas a la cadena anterior del +
        self.cadena[len(self.cadena)-1].extend(self.lista)
        self.lista = []

        fl = []
        fl.append(self.q[0])
        fl.append(self.q[1])
        #agregar las nuevos inicial y final
        self.cadena_fl.append(fl)

        #eliminar el anterior del nuevo agregaedo
        self.cadena_fl.pop(len(self.cadena_fl)-2)

        self.q.pop(0)
        self.q.pop(0)

        self.list.pop(len(self.list)-1)

    #mostar el grafo del afn creado
    def afnGraph(self,afn,sfPoint):
        inicio = sfPoint[0][0]
        final = sfPoint[0][1]
        q_list = []
        q = []
        for i in range(1000):
            value = i
            q.append(value)
        
        #guardar los valores de q utilizados
        for l in afn:
            for q_search in q:
                if q_search in l:
                    if q_search not in q_list:
                        q_list.append(q_search)
                        
        f = graphviz.Digraph(comment = "afn")
        inicio_listo = True
        
        for name in q_list:
            if name == final:
                f.node(str(name), shape="doublecircle",fillcolor="#ee3b3b",style="filled")
            elif name == inicio:
                f.node(str(name),fillcolor="#7fff00",style="filled")
            else:
                f.node(str(name))
        f.node("", shape="plaintext")
        for l in afn:
            if inicio in l:
                if(inicio_listo):
                    f.edge("",str(l[0]),label = "")
                    inicio_listo = False
            f.edge(str(l[0]),str(l[2]),label = str(l[1]))
            
        f.render("afn", view = True)


    