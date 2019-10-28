import random

class Node(object):

	def __init__(self):
		self.nodes = {}  # First level [key: value, touple(): Node()]; Second level [key: value, edge: strength]
		self.totalStrength = 0
		self.currentNode = None



	def goNextNode(self, edge):
		"""update self.currentNode to node according to edges and their strength"""
		if edge == None:
			self.currentNode = random.choice(list(self.nodes.keys()))
		else:
			tempList = list(self.currentNode)
			tempList.pop(0)
			tempList.append(edge)
			self.currentNode = tuple(tempList)



	def addNode(self, node, edge=None):
		"""this function should be used to add Nodes to the graph"""

		if node in self.nodes:
			if edge in self.nodes[node].nodes:
				self.nodes[node].nodes[edge] += 1  # if node, edge combination exists, then increment its value by one
			else:
				self.nodes[node].nodes[edge] = 1  # else: add edge of strength(value) 1 associated with that node
		else:
			self.nodes[node] = Node()
			self.nodes[node].nodes[edge] = 1
		self.nodes[node].totalStrength += 1



