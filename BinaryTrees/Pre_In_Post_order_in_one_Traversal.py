class Node:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.key = key

def dfs(root):
	preorder = []
	inorder = []
	postorder = []
	stack = [[root,1],]
	while(len(stack)>0):
		if stack[-1][1]==1:
			preorder.append(stack[-1][0].key)
			stack[-1][1]=2
			if stack[-1][0].left:
				stack.append([stack[-1][0].left,1])
	
		if stack[-1][1]==2:
			inorder.append(stack[-1][0].key)
			stack[-1][1]=3
			if stack[-1][0].right:
				stack.append([stack[-1][0].right,1])

		if stack[-1][1]==3:
			postorder.append(stack[-1][0].key)
			stack.pop()
	print("Preorder: ", preorder)
	print("inorder: ", inorder)
	print("Postorder: ", postorder)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

dfs(root)
