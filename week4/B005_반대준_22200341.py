class Solution:
    
	def __init__(self):
		self.theSet = set()

	def findTarget(self, root, k: int) -> bool:
		if not root.left and not root.right: return False

		stack = [root]

		while stack:

			node = stack.pop()

			if node.val in self.theSet:
				return True

			self.theSet.add(k - node.val)

			if node.left: stack.insert(0, node.left)
			if node.right: stack.insert(0, node.right)

		return False