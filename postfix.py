class Postfix:
    
    def __init__(self,infix):
        self.infix = infix
        self.postfix = None

    def infix_Transformation(self):
        self.infix_array = []
        for value in range(len(self.infix)):
            self.infix_array.append(self.infix[value])
            if self.infix[value] not in '|':
                self.infix_array.append('.')

        for value in range(len(self.infix_array)):
            if self.infix_array[value] in '.':
                if value+1 < len(self.infix_array):
                    if self.infix_array[value+1] in '|)':
                        self.infix_array[value] = ''
        self.infix_array.pop(len(self.infix_array)-1)
                    
        print(self.infix_array)

        
        
        

