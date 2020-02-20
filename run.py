
# run.py
# Jacob Oaks
# 2/20/20

# command line arguments:
# 0 - file name
# 1 - <data_name>
# 2 - <dict_input>
# 3 - <feature_flag>
# 4 - <num_epoch>
 
# imports
import os
import sys

# check argument count
print('\nChecking arguments...')
if len(sys.argv) < 5: # incorrect amount
	print('Invalid arguments. Please run as follows:')
	print('python3 run.py <data_name> <dict_input> <num_epoch>\n')
	sys.exit()

# run feature.py
print('Running feature.py...')
os.system('python3 feature.py input/' + sys.argv[1] + '_train.tsv input/' + sys.argv[1] + '_validation.tsv input/' + sys.argv[1] + '_test.tsv input/' + sys.argv[2] + '.txt formatted/' + sys.argv[1] + '_' + sys.argv[3] + '_train.tsv formatted/' + sys.argv[1] + '_' + sys.argv[3] + '_validation.tsv formatted/' + sys.argv[1] + '_' + sys.argv[3] + '_test.tsv ' + sys.argv[3])

# run lr.py
print('Running lr.py...')
os.system('python3 lr.py formatted/' + sys.argv[1] + '_' + sys.argv[3] + '_train.tsv formatted/' + sys.argv[1] + '_' + sys.argv[3] + '_validation.tsv formatted/' + sys.argv[1] + '_' + sys.argv[3] + '_test.tsv input/' + sys.argv[2] + '.txt output/' + sys.argv[1] + '_' + sys.argv[4] + '_train.labels output/' + sys.argv[1] + '_' + sys.argv[4] + '_test.labels output/' + sys.argv[1] + '_' + sys.argv[4] + '_metrics.txt ' + sys.argv[4])
