from postfix import *
from Tree import *
from thompson_v2 import *
from subset import *
from simulation import *
from minimizacion import *

#lenguaje
# r = '(a|b)*abb'
# r = '(a|)*abb'
# r = 'ab(a|b*)ab*ba'
# r = 'ab(abba|bbb*)aab*baba|a'
# r = "a*"
# r = "(ab)*"
# r = "(a|b)a*"
# r = "(a|b)*(a|b)"
# r ="(b|b)*abb(a|b)*"
# r = "(ab)?"
r = "0?(1?)?0*0"
# r = "(ab+)?"
# r ='(aa)?'
# r = 'a+(a?|b)*b'
# r = '*a'
# r = 'a+(a?|)*b'

#comenzar para convertirlo 
post = Postfix(r)
#conversion a su nuevo infix
new_infix = post.infix_Transformation()
#obtencion de su postfix
postfix = post.transform_postfix(new_infix)
# print(postfix)
# Construccion del arbol del postfix
tree = Tree()
tree.build_tree_from_postfix(postfix)
# obtener la lectura desde el left most utilizando el arbol construido
result = tree.left_most()
#comenzar con la construccion de thompson
afn = Thompson()
#construir el afn
afn_construido = afn.construccion_thompson(result)
#mostrar el grafico del afn
afn.afnGraph(afn_construido[0],afn_construido[1])

#comenzar la utilizacion de subset alimentarlo con el afn, y los inicales y finales y tambien el postfix
subset = Subset(afn_construido[0],afn_construido[1],postfix)
#comenzar la construccion por medio de subset
afd = subset.afnConstruction()
#construir el grafo del afn
subset.afdGraph(afd[0],afd[1])

#realizar la minimizacion del afd
minimizacion = Minimizacion(afd[0],afd[1])

# #comenzar con la simulacion para afn y afd
# simulation = Simulation()


