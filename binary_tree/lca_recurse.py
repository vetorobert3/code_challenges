#You are given pointer to the root of the binary search tree and two values  and . You need to return the lowest common ancestor (LCA) of  and  in the binary search tree.

'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca_recurse(root, v1, v2):
    if v1 < root.info and v2 < root.info:
        return lca_recurse(root.left, v1, v2)

    elif v1 > root.info and v2 > root.info:
        return lca_recurse(root.right, v1, v2)

    else:
        return root