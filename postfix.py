import re
import sys
class Postfix:
    def __init__(self,infix):
        self.infix = infix
        self.postfix = None
        self.stack =[]
        self.output = []

    def infix_Transformation(self):
        #conversion de simbolos especiales antes
        # self.infix = re.sub("\.*?\?", lambda m: m.group().replace("?", "|ε"), self.infix)

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
                    
            elif self.infix_array[value] in '*+?':
                if self.infix_array[value-1] in ".":
                    self.infix_array[value-1] =" "
                    
            
        self.infix_array.pop(len(self.infix_array)-1)
        
        self.data = ''.join([c for c in self.infix_array if c != ' '])
        # print(self.data)
        #revisar si esta correctamente el regex
        # print("_____________")
        for l in range(len(self.data)):
            # print(self.data[l])
            if l-1 >= 0 :
                if l+1 < len(self.data):
                    if self.data[l] in '+*?':
                        if self.data[l-1] not in '.|(' and self.data[l+1] not in '(':
                            pass
                            # print(self.data[l] in '+*')
                            # print(self.data[l-1] not in '+*.|(')
                            # print(self.data[l+1] not in '*+(')
                        else:
                            # print("anterior ",self.data[l-1])
                            # print("seguido ",self.data[l+1])
                            print("system error")
                            sys.exit()
                    elif self.data[l] in '.|':
                        if self.data[l-1] not in '.|(' and self.data[l+1] not in '.*+)|':
                            pass
                            # print(self.data[l] in '.|')
                            # print(self.data[l-1] not in '+*.|(')
                            # print(self.data[l+1] not in '.*+)|')
                        else:
                            # print("anterior ",self.data[l-1])
                            # print("seguido ",self.data[l+1])
                            print("system error")
                            sys.exit()
                else:
                    if self.data[l] in '.|':
                        print("system error")
                        sys.exit()
            else:
                if self.data[l] in '+*.|':
                    print("system error")
                    sys.exit()
        #     print("_____________")
        # print("_____________")
        #si todo esta bien regresa todo sin problema
        return self.data

    def transform_postfix(self,c):
        print(c)
        for l in c:
            # print("====================")
            # print(l)
            # print("s: " + str(stack))
            # print("o: " + str(output))
            if l in "|()*.+?":
                self.stack.append(l)
                # print("before stack: ", self.stack)
                proceso = True
                while(proceso):
                    element = self.stack[len(self.stack)-1]
                    if element == ")":
                        a = len(self.stack)-2
                        while(self.stack[a] != "("):
                            self.output.append(self.stack[a])
                            self.stack[a]=""
                            a = a-1
                        self.stack[a] = ""
                        self.stack[self.stack.index(")")] = ""
                        while "" in self.stack:
                            self.stack.remove("")
                        proceso = False
                        
                    elif element == "?":
                        if len(self.stack) > 1:
                            if self.stack[len(self.stack)-2] == "*":
                                self.output.append(self.stack[len(self.stack)-1])
                                self.stack.pop(len(self.stack)-1)
                            elif self.stack[len(self.stack)-2] == "+":
                                self.output.append(self.stack[len(self.stack)-1])
                                self.stack.pop(len(self.stack)-1)
                            elif self.stack[len(self.stack)-2] == "?":
                                self.output.append(self.stack[len(self.stack)-1])
                                self.stack.pop(len(self.stack)-1)
                            else:
                                proceso = False
                        else:
                            proceso = False
                            
                    elif element == "*":
                        if len(self.stack) > 1:
                            if self.stack[len(self.stack)-2] == "*":
                                self.output.append(self.stack[len(self.stack)-1])
                                self.stack.pop(len(self.stack)-1)
                            elif self.stack[len(self.stack)-2] == "+":
                                self.output.append(self.stack[len(self.stack)-1])
                                self.stack.pop(len(self.stack)-1)
                            elif self.stack[len(self.stack)-2] == "?":
                                self.output.append(self.stack[len(self.stack)-1])
                                self.stack.pop(len(self.stack)-1)
                            else:
                                proceso = False
                        else:
                            proceso = False
                                
                    elif element =="+":
                        if len(self.stack) > 1:
                            if self.stack[len(self.stack)-2] == "+":
                                self.output.append(self.stack[len(self.stack)-1])
                                self.stack.pop(len(self.stack)-1) 
                            elif self.stack[len(self.stack)-2] == "*":
                                self.output.append(self.stack[len(self.stack)-1])
                                self.stack.pop(len(self.stack)-1)
                            elif self.stack[len(self.stack)-2] == "?":
                                self.output.append(self.stack[len(self.stack)-1])
                                self.stack.pop(len(self.stack)-1)
                            else:
                                proceso = False
                        else:
                            proceso = False
                                
                    elif element == ".":
                        if len(self.stack) > 1:
                            if self.stack[len(self.stack)-2] == "*":
                                self.output.append(self.stack[len(self.stack)-2])
                                self.stack.pop(len(self.stack)-2)
                            elif self.stack[len(self.stack)-2] == "+":
                                self.output.append(self.stack[len(self.stack)-2])
                                self.stack.pop(len(self.stack)-2)
                            elif self.stack[len(self.stack)-2] == "?":
                                self.output.append(self.stack[len(self.stack)-2])
                                self.stack.pop(len(self.stack)-2)
                            elif self.stack[len(self.stack)-2] == ".":
                                self.output.append(self.stack[len(self.stack)-1])
                                self.stack.pop(len(self.stack)-1)
                            else:
                                proceso = False
                        else:
                            proceso = False
                                
                    elif element == "|":
                        if len(self.stack) > 1:
                            if self.stack[len(self.stack)-2] == "*":
                                self.output.append(self.stack[len(self.stack)-2])
                                self.stack.pop(len(self.stack)-2)
                            elif self.stack[len(self.stack)-2] == "+":
                                self.output.append(self.stack[len(self.stack)-2])
                                self.stack.pop(len(self.stack)-2)
                            elif self.stack[len(self.stack)-2] == "?":
                                self.output.append(self.stack[len(self.stack)-2])
                                self.stack.pop(len(self.stack)-2)
                            elif self.stack[len(self.stack)-2] == ".":
                                self.output.append(self.stack[len(self.stack)-2])
                                self.stack.pop(len(self.stack)-2)
                            elif self.stack[len(self.stack)-2] == "|":
                                self.output.append(self.stack[len(self.stack)-1])
                                self.stack.pop(len(self.stack)-1)
                            else:
                                proceso = False
                        else:
                            proceso = False
                    else:
                        proceso = False
                
                # if l == ")":
                #     a = len(self.stack)-2
                #     while(self.stack[a] != "("):
                #         self.output.append(self.stack[a])
                #         self.stack[a]=""
                #         a = a-1
                #     self.stack[a] = ""
                #     self.stack[self.stack.index(")")] = ""
                #     while "" in self.stack:
                #         self.stack.remove("")
                # elif l =="*":
                #     if len(self.stack) > 1:
                #         if self.stack[len(self.stack)-2] == "*":
                #             self.output.append(self.stack[len(self.stack)-1])
                #             self.stack.pop(len(self.stack)-1)
                        
                # elif l =="+":
                #     if len(self.stack) > 1:
                #         if self.stack[len(self.stack)-2] == "+":
                #             self.output.append(self.stack[len(self.stack)-1])
                #             self.stack.pop(len(self.stack)-1) 
                #         elif self.stack[len(self.stack)-2] == "*":
                #             self.output.append(self.stack[len(self.stack)-2])
                #             self.stack.pop(len(self.stack)-2)  
                # elif l == ".":
                #     if len(self.stack) > 1:
                #         if self.stack[len(self.stack)-2] == "*":
                #             self.output.append(self.stack[len(self.stack)-2])
                #             self.stack.pop(len(self.stack)-2)
                #         elif self.stack[len(self.stack)-2] == "+":
                #             self.output.append(self.stack[len(self.stack)-2])
                #             self.stack.pop(len(self.stack)-2)
                #         elif self.stack[len(self.stack)-2] == ".":
                #             self.output.append(self.stack[len(self.stack)-1])
                #             self.stack.pop(len(self.stack)-1)
                # elif l == "|":
                #     if len(self.stack) > 1:
                #         if self.stack[len(self.stack)-2] == "*":
                #             self.output.append(self.stack[len(self.stack)-2])
                #             self.stack.pop(len(self.stack)-2)
                #         elif self.stack[len(self.stack)-2] == "+":
                #             self.output.append(self.stack[len(self.stack)-2])
                #             self.stack.pop(len(self.stack)-2)
                #         elif self.stack[len(self.stack)-2] == ".":
                #             self.output.append(self.stack[len(self.stack)-2])
                #             self.stack.pop(len(self.stack)-2)
                #         elif self.stack[len(self.stack)-2] == "|":
                #             self.output.append(self.stack[len(self.stack)-1])
                #             self.stack.pop(len(self.stack)-1)
            else:
                self.output.append(l)
            # print("stack: ", self.stack)
            # print("output: ", self.output)
            # print("__________")
        while(len(self.stack) > 0):
            self.output.append(self.stack[len(self.stack)-1])
            self.stack.pop(len(self.stack)-1)

        # print("output: " + str(self.output))
        # print("stack: " + str(self.stack))
        
        #convertir el postfix a afd
        return self.output