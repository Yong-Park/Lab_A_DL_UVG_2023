from graphviz import Digraph

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def build_tree_from_postfix(self, postfix):
        stack = []
        for symbol in postfix:
            if str(symbol) not in "|*•+?":
                if type(symbol) == int:
                    symbol = str(symbol)
                # if "\\" in symbol:
                #     symbol = symbol[1:]
                node = Node(symbol)
                stack.append(node)
            elif symbol == '|':
                node = Node(symbol)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
            elif symbol == '*':
                node = Node(symbol)
                node.left = stack.pop()
                stack.append(node)
            elif symbol == '+':
                node = Node(symbol)
                node.left = stack.pop()
                stack.append(node)
            elif symbol == '?':
                node = Node(symbol)
                node.left = stack.pop()
                stack.append(node)
            elif symbol == '•':
                node = Node(symbol)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
        self.root = stack.pop()

    # Lectura Left Most
    def left_most(self):
        if self.root is None:
            return []
        stack = [self.root]
        result = []
        while len(stack) > 0:
            node = stack.pop(0)
            result.append(node.data)
            if node.left is not None:
                stack.insert(0, node.left)
            if node.right is not None:
                stack.insert(0, node.right)
        return list(reversed(result))

    def generate_dot(self, node, dot):
        if node is not None:
            dot.node(str(id(node)), node.data)
            if node.left is not None:
                dot.edge(str(id(node)), str(id(node.left)))
                self.generate_dot(node.left, dot)
            if node.right is not None:
                dot.edge(str(id(node)), str(id(node.right)))
                self.generate_dot(node.right, dot)

    def print_tree(self, node=None, level=0):
        dot = Digraph()
        self.generate_dot(self.root, dot)
        dot.render('tree.gv', view=True)