"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return
        randoms = {}
        curr = head
        while curr != None:
            randoms[curr] = Node(curr.val)
            curr = curr.next
        curr = head

        while curr:
            randoms[curr].next = randoms.get(curr.next)
            randoms[curr].random = randoms.get(curr.random)
            curr = curr.next
        return randoms[head]