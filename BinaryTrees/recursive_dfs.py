class Node:
	def __init__(self,key):
		self.left = None
		self.key = key
		self.right = None

def printinorder(root):
	if root:
		printinorder(root.left)
		print(root.key, end=",")
		printinorder(root.right)

def printpreorder(root):
	if root:
		print(root.key, end=",")
		printpreorder(root.left)
		printpreorder(root.right)

def printpostorder(root):
	if root:
		printpostorder(root.left)
		printpostorder(root.right)
		print(root.key, end=",")

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)


print("Inorder: ", end=" ")
printinorder(root)
print("\nPreorder: ", end=" ")
printpreorder(root)
print("\nprintpostorder: ", end=" ")
printpostorder(root)
