def isBalanced(self, root) -> bool:
    return self.helper(root)[1]

def helper(self,root):
    if root is None:
        return 0,True
    lh,left=self.helper(root.left)
    rh,right=self.helper(root.right)
    if abs(lh-rh)<=1 and left and right:
        return 1+max(lh,rh),True
    return 1+max(lh,rh),False