
# dictTrie.py
# Jacob Oaks
# 2/20/2020

# A generic symbol table node which contains a key, a corresponding value, a child reference, and a sibling reference
# the value is -1 if no value as this is meant to be a character-keyed node where the only nodes with values are the ones
# at the end of inserted strings. In such a case, the value is the value corresponding to the key which terminates with that character.
class Node(object):
	
	def __init__(self, key = None, value = None, child = None, sibling = None):
		self.key = key # character at this node
		self.value = value # symbol table value for this key. -1 if none
		self.child = child # children
		self.sibling = sibling # siblings

# A Trie implementation of a symbol table where the keys must be strings and the values can be of any type. Uses the Node implementation
# above.
class DictTrie(object):

	# constructor
	def __init__(self):
		self.__root = Node()
		self.__size = 0

	# adds a key-value pair
	# overwrites previous values
	# setting a key's value to None is the same as removing it
	def add(self, key: str, value):
		self.__addR(self.__root, value, 0, key)	# call recursive func

	# returns the size of the Trie
	def size(self): return self.__size

	# deletes a key-value pair
	def delete(self, key: str):
		self.add(key, None)

	# recursive function for adding a key-value pair
	def __addR(self, prev: Node, value, i: int, key: str):

		# base case -> string fully inserted
		if len(key) == i:
			if prev.value == None: self.__size += 1 # increment size if new entry
			elif value == None: self.__size -= 1 # decrement size if deletion
			prev.value = value # set correct value
			return

		# recursive case -> continue
		if prev.child == None:
			prev.child = Node(key[i]) # create child with value of current char
			self.__addR(prev.child, value, i+1, key) # recurse

		# if there is a child -> check them
		else:  
			child = prev.child # get first child
			found = False # found flag
			while (child != None and found == False): # keep looking until correct child found or end of children reached
				if (child.key == key[i]): found = True # if correct child, set correct flag to true
				else: child = child.sibling # otherwise look at next child
			if found: # if we found a a correct child
				self.__addR(child, value, i+1, key) # recurse
			else: # otherwise create new child as sibling
				newSib = prev.child
				prev.child = Node(key[i])
				prev.child.sibling = newSib;
				self.__addR(prev.child, value, i+1, key) # recurse

	# returns the value for a given key
	# returns None if no value for given key
	def getVal(self, key: str):
		node = self.__getNodeR(self.__root, key, 0) # call recursive func	
		if node == None: return None
		else: return node.value

	# recursive function for getting a node for a given key
	def __getNodeR(self, prev: Node, key: str, i: int):

		# base cases
		if (i == len(key)): return prev # end of key -> return val
		if prev.child == None: return None # no more path -> return None

		# recursive case -> continue
		child = prev.child # get first child
		found = False # found flag
		while (child != None and found == False): # continue looping until correct child found or end of children reached
			if child.key == key[i]: found = True # found correct child
			else: child = child.sibling # otherwise continue searching through children
		if found: return self.__getNodeR(child, key, i+1) # recurse with correct child
		else: return None # if no correct path to follow, return None
			

