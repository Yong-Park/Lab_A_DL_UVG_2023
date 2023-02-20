import re
class Postfix:
    def __init__(self,infix):
        self.infix = infix
        self.postfix = None
        self.stack =[]
        self.output = []

    def infix_Transformation(self):
        #conversion de simbolos especiales antes
        self.infix = re.sub("\.*?\?", lambda m: m.group().replace("?", "|ε"), self.infix)

        self.infix_array = []
        for value in range(len(self.infix)):
            self.infix_array.append(self.infix[value])
            self.infix_array.append('.')
                
        for value in range(len(self.infix_array)):
            if self.infix_array[value] in '|':
                if self.infix_array[value-1] in ".":
                    self.infix_array[value-1] = " "
                if self.infix_array[value+1] in ".":
                    self.infix_array[value+1] =" "
                    
            elif self.infix_array[value] in '(':
                if self.infix_array[value+1] in ".":
                    self.infix_array[value+1] =" "
                    
            elif self.infix_array[value] in ')':
                if self.infix_array[value-1] in ".":
                    self.infix_array[value-1] =" "
                    
            elif self.infix_array[value] in '*':
                if self.infix_array[value-1] in ".":
                    self.infix_array[value-1] =" "
                    
            
        self.infix_array.pop(len(self.infix_array)-1)
        
        self.data = ''.join([c for c in self.infix_array if c != ' '])
        return self.data

    def transform_postfix(self,c):
        print(c)
        for l in c:
            # print("====================")
            # print(l)
            # print("s: " + str(stack))
            # print("o: " + str(output))
            if l in "|()*.":
                self.stack.append(l)

                if l == ")":
                    a = len(self.stack)-2
                    while(self.stack[a] != "("):
                        self.output.append(self.stack[a])
                        self.stack[a]=""
                        a = a-1
                    self.stack[a] = ""
                    self.stack[self.stack.index(")")] = ""
                    while "" in self.stack:
                        self.stack.remove("")
                elif l == ".":
                    try:
                        if len(self.stack) > 1:
                            # print("====================")
                            # print("verdadero")
                            # print("s: " + str(stack))
                            # print("====================")
                            if self.stack[len(self.stack)-2] == "*":
                                self.output.append(self.stack[len(self.stack)-2])
                                self.stack.pop(len(self.stack)-2)
                            elif self.stack[len(self.stack)-2] == ".":
                                self.output.append(self.stack[len(self.stack)-1])
                                self.stack.pop(len(self.stack)-1)
                    except:
                        pass
                elif l == "|":
                    try:
                        if len(self.stack) > 1:
                            if self.stack[len(self.stack)-2] == "*":
                                self.output.append(self.stack[len(self.stack)-2])
                                self.stack.pop(len(self.stack)-2)
                            elif self.stack[len(self.stack)-2] == ".":
                                self.output.append(self.stack[len(self.stack)-2])
                                self.stack.pop(len(self.stack)-2)
                            elif self.stack[len(self.stack)-2] == "|":
                                self.output.append(self.stack[len(self.stack)-1])
                                self.stack.pop(self.stack[len(self.stack)-1])
                    except:
                        pass
                elif l =="*":
                    try:
                        if len(self.stack) > 1:
                            if self.stack[len(self.stack)-2] == "*":
                                self.output.append(self.stack[len(self.stack)-1])
                                self.stack.pop(self.stack[len(self.stack)-1])
                    except:
                        pass
                            
            else:
                self.output.append(l)
        while(len(self.stack) > 0):
            self.output.append(self.stack[len(self.stack)-1])
            self.stack.pop(len(self.stack)-1)

        # print("output: " + str(output))
        # print("stack: " + str(stack))
        
        #convertir el postfix a afd
        return self.output