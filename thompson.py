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
            value = "q"+str(i)
            self.q.append(value)
            
    def construccion_thompson(self, output):
        print(output)
        #este se llenara con los chain, donde al final se ve si con ello se crea un una nueva cadena o solo se le realiza el extend.
        self.lista = []
        #utilizado solo para crear los movimientos de estados para luego limpiarlo despues de una ejecucion
        self.chain = []
        for l in output:
            self.list.append(l)
            print("===========")
            print("list: ", self.list)
            print("afn: ", self.afn)
            print("cadena: ", self.cadena)
            # print("lista que debe de estar vacia: ", self.lista)
            print("first and las de cadena: ", self.cadena_fl)
            if self.list[len(self.list)-1] == "|":
                self.orFunction()
            elif self.list[len(self.list)-1] == "*":
                self.kleenFunction()
            elif self.list[len(self.list)-1] == ".":
                self.andFunction()
        return [self.afn, self.cadena_fl]
    
    def andFunction(self):
        #significa que este conecta dos arrays que estan en la cadena por separado, entonces estos se unificaran con un extend y una variable mas que es el que los conecta. y se actualizaria el final y inicial. 
        if len(self.list)==1:
            pass
        #significa que tiene una variable que esta se conecta con el ultimo elemento que esta en la cadena, este se realizara un extend porque forma parte de ella. y se actualizara solo el final
        elif len(self.list)==2:
            self.chain.append(self.cadena_fl[len(self.cadena_fl)-1][1])
            self.chain.append(self.list[len(self.list)-2])
            self.chain.append(self.q[0])
            self.lista.append(self.chain)
            self.afn.append(self.chain)
            self.chain = []
            
            self.cadena[len(self.cadena)-1].extend(self.lista)
            self.lista = []
            
            last = self.q[0]
            
            self.cadena_fl[len(self.cadena_fl)-1][1] = last
            
            self.q.pop(0)
            
            self.list.pop(len(self.list)-1)
            self.list.pop(len(self.list)-1)
            
        #significa que este tiene las dos variabels antes del . por lo cual se debe de agregar a cadena como uno nuevo junto con su inical y final
        elif len(self.list)==3:
            self.chain.append(self.q[0])
            self.chain.append(self.list[len(self.list)-3])
            self.chain.append(self.q[1])
            self.lista.append(self.chain)
            self.afn.append(self.chain)
            self.chain = []
            
            self.chain.append(self.q[1])
            self.chain.append(self.list[len(self.list)-2])
            self.chain.append(self.q[2])
            self.lista.append(self.chain)
            self.afn.append(self.chain)
            self.chain = []
            
            self.cadena.append(self.lista)
            self.lista = []
            
            fl = []
            fl.append(self.q[0])
            fl.append(self.q[2])
            
            self.cadena_fl.append(fl)
        
            self.q.pop(0)
            self.q.pop(0)
            self.q.pop(0)
            
            self.list.pop(len(self.list)-1)
            self.list.pop(len(self.list)-1)
            self.list.pop(len(self.list)-1)
            
    def orFunction(self):
        #este ocurre cuando estan las dos variables, por lo cual entonces se agrega este como una nueva en cadena y tambien nuevos incial y final
        if len(self.list) == 3:
            self.chain.append(self.q[0])
            self.chain.append(self.eps)
            self.chain.append(self.q[1])
            self.lista.append(self.chain)
            self.afn.append(self.chain)
            self.chain = []
            
            self.chain.append(self.q[1])
            self.chain.append(self.list[len(self.list)-2])
            self.chain.append(self.q[2])
            self.lista.append(self.chain)
            self.afn.append(self.chain)
            self.chain = []
            
            self.chain.append(self.q[2])
            self.chain.append(self.eps)
            self.chain.append(self.q[3])
            self.lista.append(self.chain)
            self.afn.append(self.chain)
            self.chain = []
            
            self.chain.append(self.q[0])
            self.chain.append(self.eps)
            self.chain.append(self.q[4])
            self.lista.append(self.chain)
            self.afn.append(self.chain)
            self.chain = []
            
            self.chain.append(self.q[4])
            self.chain.append(self.list[len(self.list)-3])
            self.chain.append(self.q[5])
            self.lista.append(self.chain)
            self.afn.append(self.chain)
            self.chain = []
            
            self.chain.append(self.q[5])
            self.chain.append(self.eps)
            self.chain.append(self.q[3])
            self.lista.append(self.chain)
            self.afn.append(self.chain)
            self.chain = []

            self.cadena.append(self.lista)
            self.lista = []
            
            first = self.q[0]
            last = self.q[3]
            
            fl = []
            fl.append(first)
            fl.append(last)
            
            self.cadena_fl.append(fl)
            
            self.q.pop(0)
            self.q.pop(0)
            self.q.pop(0)
            self.q.pop(0)
            self.q.pop(0)
            self.q.pop(0)
            
            self.list.pop(len(self.list)-1)
            self.list.pop(len(self.list)-1)
            self.list.pop(len(self.list)-1)
        #este ocurre cuando hay solo una variable, lo cual significa que se conecta esta variable con el ultimo que esta en el cadena, en este se realizara un extend ya que llegara a formar parte de este nuevo
        # y tambien se crearan nuevos iniciales y finales
        elif len(self.list) == 2:
            pass
        #este ocurre cuando no tiene variabels, significando que utilizara dos arrys de cadena, estos se realizaran extend y se agregaran los que corresponden, ademas que tambien llegara a tener nuevos iniciales y finales
        elif len(self.list) == 1:
            pass
            
    def kleenFunction(self):
        if len(self.cadena) > 0 and len(self.list) == 1:
            self.chain.append(self.q[0])
            self.chain.append(self.eps)
            self.chain.append(self.cadena_fl[len(self.cadena_fl)-1][0])
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
            
            self.chain.append(self.cadena_fl[len(self.cadena_fl)-1][1])
            self.chain.append(self.eps)
            self.chain.append(self.q[1])
            self.lista.append(self.chain)
            self.afn.append(self.chain)
            self.chain = []
            
            self.cadena[len(self.cadena)-1].extend(self.lista)
            self.lista = []
            
            first = self.q[0]
            last = self.q[1]
            
            fl = []
            fl.append(first)
            fl.append(last)
                    
            self.cadena_fl[len(self.cadena_fl)-1]=(fl)
            
            self.q.pop(0)
            self.q.pop(0)
            
            self.list.pop(len(self.list)-1)
        else:
            self.chain.append(self.q[0])
            self.chain.append(self.eps)
            self.chain.append(self.q[1])
            self.lista.append(self.chain)
            self.afn.append(self.chain)
            self.chain = []
            
            self.chain.append(self.q[1])
            self.chain.append(self.list[len(self.list)-2])
            self.chain.append(self.q[2])
            self.lista.append(self.chain)
            self.afn.append(self.chain)
            self.chain = []
            
            self.chain.append(self.q[2])
            self.chain.append(self.eps)
            self.chain.append(self.q[3])
            self.lista.append(self.chain)
            self.afn.append(self.chain)
            self.chain = []
            
            self.chain.append(self.q[2])
            self.chain.append(self.eps)
            self.chain.append(self.q[1])
            self.lista.append(self.chain)
            self.afn.append(self.chain)
            self.chain = []
            
            self.chain.append(self.q[0])
            self.chain.append(self.eps)
            self.chain.append(self.q[3])
            self.lista.append(self.chain)
            self.afn.append(self.chain)
            self.chain = []
            
            self.cadena.append(self.lista)
            self.lista = []
            
            first = self.q[0]
            last = self.q[3]
            
            fl = []
            fl.append(first)
            fl.append(last)
                    
            self.cadena_fl.append(fl)
            
            self.q.pop(0)
            self.q.pop(0)
            self.q.pop(0)
            self.q.pop(0)
            
            self.list.pop(len(self.list)-1)
            self.list.pop(len(self.list)-1)