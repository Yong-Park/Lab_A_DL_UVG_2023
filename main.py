from postfix import *


#lenguaje
r = '(a|b)*abb'
# r = 'ab(a|b*)ab*ba'

post = Postfix(r)
post.infix_Transformation()