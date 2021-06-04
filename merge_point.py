"""Given pointers to the head nodes of  linked lists that merge together at some point, find the node where the two lists merge. The merge point is where both lists point to the same node, i.e. they reference the same memory location. It is guaranteed that the two head nodes will be different, and neither will be NULL. If the lists share a common node, return that node's  value."""

# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
  # find the length of the two lists
  length1 = get_length(head1)
  length2 = get_length(head2)
  
  # move head of the larger list the difference of the two lists
  if length1 > length2:
    diff = length1 - length2
    for i in range(diff):
      head1 = head1.next
      
  if length2 > length1:
    diff = length2 - length1
    for i in range(diff):
      head2 = head2.next
  
  # iterate over the two lists at the same time
  while head1 or head2:
    # compare the nodes
    # if they're equal, we've found the merge point
    if head1 == head2:
      return head1.data
    
    head1 = head1.next
    head2 = head2.next
    
    

def get_length(head):
  length = 0
  curr = head
  while curr is not None:
    length += 1
    curr = curr.next
  return length