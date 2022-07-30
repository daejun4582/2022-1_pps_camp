def diameterOfBinaryTree(self, root) -> int:
    
    self.diameter = 0
    
    def dfs(root):
        if not root: return 0
        left = dfs(root.left)
        right = dfs(root.right)
        self.diameter = max(self.diameter, left + right)
        return 1 + max(left, right)
    
    dfs(root)
    return self.diameter