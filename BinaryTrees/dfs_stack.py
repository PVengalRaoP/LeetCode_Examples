class Node:
	def __init__(self,key):
		self.right = None
		self.left = None
		self.key = key


def preorder(root):
	if root == None:
		return None
	stack = [root,]
	while(len(stack)>0):
		temp = stack.pop()
		print(temp.key)
		if temp.right:
			stack.append(temp.right)
		if temp.left:
			stack.append(temp.left)


def inorder(root):
	if root == None:
		return None
	stack = []
	currentnode = root

	while True:
		if currentnode:
			stack.append(currentnode)
			currentnode = currentnode.left
		else:
		    if len(stack)==0:
		        break
		    else:
		        temp = stack.pop()
		        print(temp.key)
		        currentnode = temp.right


def postorder(root):
	if root == None:
		return None
	stack1 = [root,]
	stack2 = []
	while (len(stack1)>0):
		temp = stack1.pop()
		if temp.left:
			stack1.append(temp.left)
		if temp.right:
			stack1.append(temp.right)
		stack2.append(temp)

	while(len(stack2)>0):
		print(stack2.pop().key)



root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)



print(" PreOrder : \n")
preorder(root)
print(" Inorder : \n")
inorder(root)
print(" Postorder :  \n")
postorder(root)
