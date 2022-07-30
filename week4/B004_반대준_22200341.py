from collections import deque
class Solution:
    def isSymmetric(self, root) -> bool:
        # level order traversal 
        if not root :
            return True
        queue = deque([(root.left, root.right)])
        while queue:
            l,r = queue.popleft()
            if l and r and l.val == r.val:
                #already adding it to the queue according to the required format
                queue.extend([(l.right, r.left), (l.left, r.right)])
            elif l == r:
                continue
            else:
                return False
        return True