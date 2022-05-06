class Node:
	def __init__(self,key):
		self.key = key
		self.right = None
		self.left = None

root =Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.left = Node(5)
root.left.right = Node(6)
root.right.left = Node(7)


def height(root):
	if root is None:
		return 0
	else:
		return 1+max(height(root.left),height(root.right))

print(height(root))
