from postfix import *
from Tree import *
from thompson_v2 import *

#lenguaje
r = '(a|b)*abb'
# r = '(a|)*abb'
# r = 'ab(a|b*)ab*ba'
# r = 'ab(abba|bbb*)aab*baba|a'
# r = "a*"
# r = "(ab)*"
# r = "(a|b)a*"
# r = "(a|b)*(a|b)"
# r ="(b|b)*abb(a|b)*"

#comenzar para convertirlo 
post = Postfix(r)
#conversion a su nuevo infix
new_infix = post.infix_Transformation()
#obtencion de su postfix
postfix = post.transform_postfix(new_infix)
# Construccion del arbol del postfix
tree = Tree()
tree.build_tree_from_postfix(postfix)
# obtener la lectura desde el left most utilizando el arbol construido
result = tree.left_most()
#comenzar con la construccion de thompson
afn = Thompson()
afn_construido = afn.construccion_thompson(result)

print(afn_construido[0])
print(afn_construido[1])

afn.afnGraph(afn_construido[0],afn_construido[1][0][0],afn_construido[1][0][1])
