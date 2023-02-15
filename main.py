from postfix import *
from Tree import *

#lenguaje
r = '(a|b)*abb'
# r = '(a|)*abb'
# r = 'ab(a|b*)ab*ba'
# r = 'ab(abba|bbb*)aab*baba|a'

post = Postfix(r)
new_infix = post.infix_Transformation()
postfix = post.transform_postfix(new_infix)
# print(postfix)
tree = Tree()
tree.build_tree_from_postfix(postfix)
# tree.print_tree('tree.png')
result = tree.left_most()
print(result)
