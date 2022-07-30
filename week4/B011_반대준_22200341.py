def mergeTrees(self, root1, root2):   
    def helper(root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1
        new_root = TreeNode(root1.val + root2.val)
        new_root.left = helper(root1.left, root2.left)
        new_root.right = helper(root1.right, root2.right)
        return new_root
    return helper(root1, root2)