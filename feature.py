
# feature.py
# Jacob Oaks
# 2/20/20

# imports
import sys
import dictTrie as dt

# command line arguments:
# 0 - file name
# 1 - <train_input>
# 2 - <validation_input>
# 3 - <test_input>
# 4 - <dict_input>
# 5 - <formatted_train_out>
# 6 - <formatted_validation_out>
# 7 - <formatted_test_out>
# 8 - <feature_flag>

# check argument count
print('\nChecking arguments...')
if len(sys.argv) < 9: # incorrect amount
	print('Invalid arguments. Please run as follows:')
	print('python3 feature.py <train_input> <validation_input> <test_input> <dict_input> <formatted_train_out> <formatted_validation_out> <formatted_test_out> <feature_flag>\n')
	sys.exit()

# check feature flag
try:
	featureFlag = int(sys.argv[8])
	if featureFlag < 1 or featureFlag > 2:
		print('Invalid feature flag. Please use 1 or 2.\n')
		sys.exit()
except ValueError:
	print('Invalid feature flag. Please use 1 or 2.\n')
	sys.exit()

# constant for avoiding words that occur too much
THRESHOLD = 4

# class for counting occurence of various objects
class Counter:

	# constructor
	def __init__(self):
		self.keys = []
		self.counts = []

	# iterates a key's cout
	def add(self, key):
		found = False
		for i in range(0, len(self.keys)): # search for and iterate
			if self.keys[i] == key:
				self.counts[i] += 1
				found = True
		if found == False: # add if not found
			self.keys.append(key)
			self.counts.append(0)

# function that returns the contents of a file
def fileContents(location: str):
	fileIn = open(location, 'r')
	contents = fileIn.readlines()
	fileIn.close()
	return contents

# functcion that formats the data from inLocation and outputs it to outLocation
def formatData(inLocation: str, outLocation: str, dictTrie: dt.DictTrie()):

	contents = fileContents(inLocation)
	fileOut = open(outLocation, 'w')
	for line in contents:

		# record class and format tokens
		tokens = line.split(' ')
		classification = tokens[0][0] # classification is the first character of the first token
		tokens[0] = tokens[0][2:] # remove class and tab from first token
		validTokens = [] # create features array

		# if feature_flag is 2, count and remote those tokens whose occurences are greater than the threshold
		if (int(sys.argv[8]) == 2):
			counter = Counter() # count occurences of each key
			for token in tokens: # loop through tokens and count occurence and add to trie
				counter.add(token) # iterate count
			for i in range(0, len(counter.keys)):
				if counter.counts[i] < THRESHOLD: # remove if too frequent
					validTokens.append(counter.keys[i])

		# otherwise, just add each token that occurs
		else: 
			for token in tokens: 
				if token not in validTokens: validTokens.append(token)

		# finally, format and write line
		fileOut.write(classification + '\t')
		for token in validTokens:
			index = dictTrie.getVal(token)
			if index != None and index != 0:
				fileOut.write(str(index) + ':1\t')
		fileOut.write('\n')
	fileOut.close()

# read in dictionary and add words to trie
print('Reading and formatting dictionary...')
dictContents = fileContents(sys.argv[4])
dictTrie = dt.DictTrie()
for dictLine in dictContents:
	tokens = dictLine.split(' ')
	dictTrie.add(tokens[0], int(tokens[1]))

# read in and format all data types
print('Reading and formatting training data...')
formatData(sys.argv[1], sys.argv[5], dictTrie) # train data
print('Reading and formatting validation data..')
formatData(sys.argv[2], sys.argv[6], dictTrie) # validation data
print('Reading and formatting test data...')
formatData(sys.argv[3], sys.argv[7], dictTrie) # test data
print('Done!\n')



