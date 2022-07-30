class Solution:
    def increasingBST(self, root):
        self.curr = self.new= TreeNode()

        def inorder(root):
            if root is None:
                return None
            inorder(root.left)
            new_node= TreeNode(root.val)
            self.curr.right  = new_node
            self.curr = self.curr.right
            inorder(root.right)
        

        inorder(root)
        return self.new.right