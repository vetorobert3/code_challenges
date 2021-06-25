#You are given pointer to the root of the binary search tree and two values  and . You need to return the lowest common ancestor (LCA) of  and  in the binary search tree.

'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca_iter(root, v1, v2):
    current = root

    while current:
        if v1 < current.info and v2 < current.info:
            current = current.left

        elif v1 > current.info and v2 > current.info:
            current = current.right

        else:
            return current