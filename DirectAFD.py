class DirectAfd:
    def __init__(self,postfix):
        self.postfix = postfix
        #agregar el # de ultimo para la cadena
        self.postfix.append('#')
        self.postfix.append('.')

        self.newPostfix = []
        self.nullable= []
        self.firstPos= []
        self.lastPos = []
        self.followPos = [] 
        self.q = []
        self.enumerate()
        self.startConstruct()
    
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

        print("node: ", self.newPostfix)
        print("nullable: ", self.nullable)
        print("firstpos: ", self.firstPos)
        print("lastpos: ", self.lastPos)
        
    def follopostConstruct(self):
        pass