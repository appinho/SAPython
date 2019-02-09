
class Node(object):

	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

class BinarySearchTree(object):

	def __init__(self, data):
		self.root = Node(data)

	def insert(self, data):

		# Tree not empty
		if self.root:

			current = self.root

			while current:
				if data < current.data:

					if current.left is None:
						current.left = Node(data)
						break
					else:
						current = current.left

				elif data > current.data:
					if current.right is None:
						current.right = Node(data)
						break
					else:
						current = current.right

		# First node in tree
		else:
			self.root = BinarySearchTree(data)

	def preorder(self, node=None): # root,left,right

		if node is None:
			node = self.root

		print(node.data)
		if node.left:
			self.preorder(node.left)
		if node.right:
			self.preorder(node.right)

	def inorder(self, node=None): # left,root,right

		if node is None:
			node = self.root

		if node.left:
			self.preorder(node.left)
		print(node.data)
		if node.right:
			self.preorder(node.right)

	def postorder(self, node=None): # left,right,root

		if node is None:
			node = self.root

		if node.left:
			self.preorder(node.left)
		if node.right:
			self.preorder(node.right)
		print(node.data)

	def bfs(self):
		print("BFS")
		to_visit = []

		if self.root:
			to_visit.append(self.root)

		while to_visit:
			current = to_visit.pop(0)
			print(current.data)
			if current.left:
				to_visit.append(current.left)
			if current.right:
				to_visit.append(current.right)

	def dfs(self):
		print("DFS")
		to_visit = []

		if self.root:
			to_visit.append(self.root)

		while to_visit:
			current = to_visit.pop()
			print(current.data)
			if current.right:
				to_visit.append(current.right)
			if current.left:
				to_visit.append(current.left)

t = BinarySearchTree(100)
t.insert(12)
t.insert(92)
t.insert(112)
t.insert(123)
t.insert(2)
t.insert(11)
t.insert(52)
t.insert(3)
t.insert(66)
t.insert(10)
t.preorder()
#t.inorder()
#t.postorder()
t.dfs()
t.bfs()
