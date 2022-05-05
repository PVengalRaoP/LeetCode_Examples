class Node:
	def __init__(self,key):
		self.left= None
		self.key = key
		self.right = None

def bfs(temp):
	if temp == None:
		return None
	qu=[]
	#visited = {}
	qu.append(temp)
	while qu:
		k=qu.pop(0)
		print(k.key, end=" , ")
		if k.left != None:
			qu.append(k.left)
		if k.right != None:
			qu.append(k.right)

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)


print("BFS: ", end=" ")
bfs(root)
