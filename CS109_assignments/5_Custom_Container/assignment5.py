from binarysearchtree import Node

class TreeDict:
	"""Implement a class called TreeDict that supports operators the same
	way as a dict. 

	TreeDict should be implemented using the binarysearchtree module I
	have provided (you can download it from canvas in the same folder as
	this file).

	You need to make sure you support the following operations with the
	same semantics as a normal Python dict:
	* td[key]
	* td[key] = value
	* key in td
	* td.get(key)
	* td.get(key, default)
	* td.update(iterable_of_pairs_or_dict_or_TreeDict)
	* len(td)
	* for key in td: pass
	* for key, value in td.items(): pass
	* A constructor: TreeDict(iterable_of_pairs_or_dict_or_TreeDict)

	Iteration should be in key order, this should be pretty easy to do
	just by traversing the tree using an in-order traversal. None of the
	iterator methods should make a copy of any of the data in the
	TreeDict. You should only implement in-order traversal once and use
	that implementation for both kinds of traversal.

	You should support a constructor which takes the same arguments as
	update and creates a TreeDict with just those values. There is an easy
	way to do this in just a couple of lines using your existing update
	method.

	For each operation, make sure it does the same thing as a dict and you
	handle errors by throwing the same type of exception as would be
	thrown by a dict. However you only need to handle the operations
	listed above, not all operations supported by dict. Unlike dict your
	implementation will not support None as a key and you should throw an
	appropriate exception if None is used as a key. Look at the available
	built in exceptions and pick the most appropriate one you find.

	Most of these methods will be very short (just a couple of lines of
	code), a couple will be a bit more complicated. However all the hard
	work should already be handled by the binarysearchtree module. It
	looks like a lot of operations, but it shouldn't actually take that
	long. Many of the operations are quite similar as well.

	Do not reimplement anything in the binarysearchtree module or copy
	code from it. You should not need to.

	For this assignment I expect you will have to use at least the
	following things you have learned:
	* Raising exceptions
	* Catching exceptions
	* Implementing magic methods
	* Generators using yield (and you will need to look up "yield from" in the Python documentation)
	* Type checks
	* Default values/optional arguments

	You will also need to read code which I think will help you learn to
	think in and use Python.

	To reiterate some of the things you should be aware of to avoid losing
	points:
	* None of the iterator methods should make a copy of any of the data
	  in the TreeDict.
	* You should only implement in-order traversal once and it should be
	  recursive (it's so much easier that way).
	* Do not reimplement anything in the binarysearchtree module or copy
	  code from it.
	* There are easy ways to implement all the required operations. If
	  your implementation of a method is long you may want to think if
	  there is a simpler way.

	Links:
	* https://docs.python.org/3.5/library/stdtypes.html#dict
	* http://en.wikipedia.org/wiki/Binary_search_tree#Traversal
	* https://docs.python.org/3.5/reference/expressions.html#yieldexpr
	"""


	# constructor
	def __init__(self, dictLikeObject = None):
		self.elem = Node()
		if dictLikeObject is not None:
			self.update(dictLikeObject)


	#td[key]
	def __getitem__(self, key):
		if key == None:
			raise KeyError("illegal input key - None")
		try:
			return self.elem.lookup(key).value
		except ValueError as error:
			raise KeyError("Invalid key input {} : {}".format(key, error))


	#td[key] = value
	def __setitem__(self, key, value):
		if key == None:
			raise KeyError("illegal input key - None")
		self.elem.insert(key, value)
 

	#key in td
	def __contains__(self, key):
		try:
			self.elem.lookup(key)
		except ValueError:
			return False
		else: 
			return True


	#helper function - for __iter__()
	def traversal(self, tree):
		if tree.left is not None:
			yield from self.traversal(tree.left)
		if tree.key is not None:
			yield tree.key
		if tree.right is not None:
			yield from self.traversal(tree.right)


	#Enables 'for loop' through TreeDict
	def __iter__(self):
		return self.traversal(self.elem)


	#len(td)
	def __len__(self):
		i = 0
		for key in self:
			i += 1
		return i


	#td.get(key, default) - WORKS
	def get(self, key, default = None):
		if key == None:
			raise KeyError("illegal input key - None")
		try:
			return self.elem.lookup(key).value
		except ValueError:
			return default

	# Enables extracting key and value within a for loop 
	def items(self):
		for key in self:
			yield key, self[key]


	#td.update(iterable_of_pairs_or_dict_or_TreeDict)
	def update(self, dictLikeObject):
			
		try:
			if isinstance(dictLikeObject, dict):
				for key, value in dictLikeObject.items():
					if key == None:
						raise KeyError("illegal input key - None")	
					self[key] = value
			
			elif isinstance(dictLikeObject, TreeDict):
				for key, value in dictLikeObject.items():
					if key == None:
						raise KeyError("illegal input key - None")		
					self[key] = value
			
			else:
				for x, y in dictLikeObject:
					if x == None:
						raise KeyError("illegal input key - None")
					else:
						self[x] = y

		except TypeError as error:
			raise TypeError("Input {} is not a dict/TreeDict/Iterable of pairs : {}".format(dictLikeObject, error))

