
# lr.py
# Jacob Oaks
# 2/20/20

# imports
import sys
import dictTrie as dt
import math

# command line arguments:
# 0 - file name
# 1 - <formatted_train_input>
# 2 - <formatted_validation_input>
# 3 - <formatted_test_input>
# 4 - <dict_input>
# 5 - <train_out>
# 6 - <test_out>
# 7 - <metrics_out>
# 8 - <num_epoch>

# check argument count
print('\nChecking arguments...')
if len(sys.argv) < 9: # incorrect amount
	print('Invalid arguments. Please run as follows:')
	print('python3 lr.py <formatted_train_input> <formatted_validation_input> <formatted_test_input> <dict_input> <train_out> <test_out> <metrics_out> <num_epoch>\n')
	sys.exit()

# check number of epochs
try:
	numEpoch = int(sys.argv[8])
	if numEpoch < 0:
		print('Invalid number of epochs. Please use a number greater than or equal to 0.\n')
		sys.exit()
except ValueError:
	print('Invalid number of epochs. Please use an integer.\n')
	sys.exit()

# constant for learning rate
LEARNING_RATE = 0.1

# read in dictionary and add words to trie
print('Reading and formatting dictionary...')
fileIn = open(sys.argv[4], 'r')
fileContents = fileIn.readlines()
fileIn.close()
dictTrie = dt.DictTrie()
for line in fileContents:
	tokens = line.split(' ')
	dictTrie.add(tokens[0], int(tokens[1]))

# initialize parameters vector
print('Initializing parameters...')
parameters = [0] * (dictTrie.size() + 1)

# load training data
print('Loading training data...')
fileIn = open(sys.argv[1], 'r')
trainData = fileIn.readlines()
fileIn.close()

# returns the dot product (theta T x) given the parameters and a list of positive features
def dotProduct(parameters, positiveFeatures):
	dotProduct = 0
	for feature in positiveFeatures:
		dotProduct += (parameters[int(feature)] * 1)
	return dotProduct

# classifies a given sample using the given parameters
def classify(parameters, sample, output = None):
	tokens = sample.split('\t') # split data into tokens
	tokens.pop(0) # remove correct classification at beginning
	positiveFeatures = [0] # add positive features to a single array (start with idx 0 always for bias term)
	for token in tokens: # loop through tokens to get positive features
		if token[len(token) - 1] == '1': positiveFeatures.append(token[:-2])
	expdp = math.exp(-dotProduct(parameters, positiveFeatures)) # get e^theta T x
	yhat = 1/(1 + expdp)
	if yhat >= 0.5:
		if output != None: output.write('[' + str(1 - ((1.0 - yhat) / 0.5)) + ']: ')
		return 1 # return according to bernoulli
	if output != None: output.write('[' + str((0.5 - yhat) / 0.5) + ']: ')
	return 0

# classifies a dataset using the given parameters, writes the classifications to the given output location and returns the error
# if outputLocation is None, does not output classification
def classifyData(parameters, data, outputLocation = None, writeConfidence = False):
	if outputLocation != None: fileOut = open(outputLocation, 'w')
	incorrectPredictions = 0
	for sample in data:
		y = int(sample[0]) # get correct answer
		if writeConfidence: yhat = classify(parameters, sample, fileOut) # classify
		else: yhat = classify(parameters, sample) # classify
		if outputLocation != None: fileOut.write(str(yhat) + '\n')
		if yhat != y: incorrectPredictions += 1 # check if correct classification
	if outputLocation != None: fileOut.close()
	return incorrectPredictions / len(data) # calculate training error

# load validation data
print('Loading validation data...')
fileIn = open(sys.argv[2], 'r')
validationData = fileIn.readlines()
fileIn.close()

# loop through training data for a specified number of epochs
for i in range(0, int(sys.argv[8])):
	print('Training at epoch ' + str(i + 1) + '...')

	# loop through each training example
	for trainExample in trainData:
		tokens = trainExample.split('\t') # split data into tokens
		y = int(tokens.pop(0)) # correct classification
		positiveFeatures = [0] # add positive features to a single array (start with idx 0 always for bias term)
		for token in tokens:
			if token[len(token) - 1] == '1': positiveFeatures.append(token[:-2])
		expdp = math.exp(dotProduct(parameters, positiveFeatures)) # get e^theta T x
		update = y - (expdp / (1 + expdp)) # calculate update
		for feature in positiveFeatures: # update parameters
			parameters[int(feature)] += (LEARNING_RATE * update) # update

	# print validation error after each epoch
	print('Validation error: ' + str(classifyData(parameters, validationData)))

# classify training data and calculate training error
print('Classifying training data...')
trainError = classifyData(parameters, trainData, sys.argv[5])

# load test data
print('Loading test data...')
fileIn = open(sys.argv[3], 'r')
testData = fileIn.readlines()
fileIn.close()

# classify test data and calculate test error
print('Classifying test data...')
testError = classifyData(parameters, testData, sys.argv[6], True)

# record metrics
print('Recording metrics...')
fileOut = open(sys.argv[7], 'w')
fileOut.write('error(train): ' + str(trainError) + '\nerror(test): ' + str(testError) + '\n')
fileOut.close()

# give final report
print('Done!\n\nFinal Results:\nerror(train): ' + str(trainError) + '\nerror(test): ' + str(testError) + '\n')
