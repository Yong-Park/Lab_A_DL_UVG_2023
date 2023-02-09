from postfix import *


#lenguaje
r = '(a|b)*abb'
# r = 'ab(a|b*)ab*ba'

post = Postfix(r)
new_infix = post.infix_Transformation()
postfix = post.transform_postfix(new_infix)
print(postfix)

