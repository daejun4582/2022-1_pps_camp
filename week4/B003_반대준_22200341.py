def sumLeft(self, root):
    if not root:
        return 0
    if not root.left and not root.right:
        return root.val
    return self.sumLeft(root.left) + self.sumOfLeftLeaves(root.right)

def sumOfLeftLeaves(self, root) -> int:
    if not root:
        return 0
    return self.sumLeft(root.left) + self.sumOfLeftLeaves(root.right)