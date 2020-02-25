
# command line arguments
# 0 - file name
# 1 - <test_dataset>
# 2 - <test_labels>
# 3 - <zero_class_name>
# 4 - <one_class_name>

# imports
import sys

# check argument count
print('\nChecking arguments...')
if len(sys.argv) < 5: # incorrect amount
	print('Invalid arguments. Please run as follows:')
	print('python3 results.py <test_dataset> <test_labels> <zero_class_name> <one_class_name>\n')
	sys.exit()

# read data
fileIn = open(sys.argv[1], 'r')
dataContents = fileIn.readlines()
fileIn.close()

# read labels
fileIn = open(sys.argv[2], 'r')
labelContents = fileIn.readlines()
fileIn.close()

# get class name
classZero = sys.argv[3]
classOne = sys.argv[4]

# print label
print('\n')
for i in range(0, len(labelContents)):

    # parse data
    tokens = dataContents[i].split('\t')
    item = tokens[1][:-1]
    if int(tokens[0][0:1]) == 0: correctClass = classZero
    else: correctClass = classOne

    # parse label
    tokens = labelContents[i].split(' ')
    confidence = float(tokens[0][1:7]) * 100 # as a percentage
    if int(tokens[1]) == 0: predictedClass = classZero
    else: predictedClass = classOne

    # print
    print(' item: ' + item)
    print(' correct classification: ' + correctClass)
    print(' predicted classification: ' + predictedClass)
    print(' confidence level: ' + str(confidence) + '%\n')
