"""
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.

    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

    Understand:
        1           1
       / \         / \
      2   3       2   3       True

      1      1 
     /        \
    2          2     False

    Plan:
        This problem can be solved recursivly. 
        
        The base case would be if both "p" and "q" (2 binary trees) are None, then they are the same tree. 

        If either p or q are None, then the trees are not the same

        If the value of p and q are not the same, then the trees are not the same.

        Else, we recurde the call.
"""

def same_tree(p, q):
    """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
    """    

    if p == None and q == None:
        return True

    if p == None or q == None:
        return False

    if p.val != q.val:
        return False

    return same_tree(p.left, q.left) and same_tree(p.right, q.right)