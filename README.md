
## Introduction

This is a very basic natural language processing system using binary logistic regression. In data that I have tested it with I was able to get test errors as low as 0.15. It runs was sripted using python 3.6 and has very specific data formatting requirements. Once understood however, it is very accessible.

This program is split into two parts and is dependent on data formatted a certain way. There should be three different data sets: a training set, a validation set, and a test set. You could theoretically make them all the same, or make any of them just empty files if you do not wish to train, validate, or test respecively. However, staying true to the problem of machine learning, it is recommended that the user has three different datasets. This file will explain how this data is to be formatted and how the program runs. 

## Data Format

The data (training, validation, and testing) must all be formatted in separate files as follows:

```
<class>\t<word1> <word2> ... <wordN>\n
```

where the class is either 0 or 1, and the words are any tokens without spaces.
Example:

```
1 these are the words which will be read
0 these are words to be read from the next sample
4 th i s is  an invalid    sample \n\n\n
```

 * This program also relies on having an indexed dictionary which defines which words should be considered features. This should be formatted as follows:

```
<word> <index>
```

where the word is any token with a space and the index is a non-negative integer value.
Example:

```
this 0
is 1
the 2
dictionary 3
and 4
these 5
words 6
will 7
be 8
considered 9
features 10
```

# Running

 * This program is split into two parts but for convenience there is a single python script (run.py) that will run both. The first part (feature.py) reads in and formats/pre-processes the data, and the second part (lr.py) performs the learning on the formatted data. Both rely on dictTrie.py. The expected arguments for feature.py, lr.py, and run.py are given below:

 * feature.py expects these arguments:
 ```
<train_input> the file which holds the training data
<validation_input> the file which holds the validation data
<test_input> the file which holds the test data
<dict_input> the file which holds the dictionary
<formatted_train_out> the file to which will be written the pre-processed training data
<formatted_validation_out> the file to which will be written the pre-processed validation data
<formatted_test_out> the file to which will be written the pre-processed validation data
<feature_flag> a flag which should either be set to 1 (which will keep all occuring words in the data) or 2 (which will remove words which occur more than 4 times)
```

 * lr.py expects these arguments:
 ```
<formatted_train_input> the file which holds the pre-processed training data
<formatted_validation_input> the file which holds the pre-processed validation data
<formatted_test_input> the file which holds the pre-processed test data
<dict_input> the file which holds the dictionary
<train_out> the file to which will be written the classifications for the training data after training has occurred
<test_out> the file to which will be written the classifications for the test data after training has occurred
<metrics_out> the file to which test error and train error will be written after training has occurred
<num_epoch> the number of epochs (traversals of training data) to train for. 30-60 is recommended.
 ```

 * run.py expects these arguments:
 ```
<data_name> when run, run.py will look for data based on the following concatenation: 'input/<data_name>_<train|validation|test>.tsv'
<dict_input> when run, run.py will look for the dictionary based on the following concatenation: 'input/<dict_input>.txt'
<feature_flag> used in feature.py as described above
<num_epoch> when run, run.py will save its output based on the following concatenation: 'output/<data_name>_<num_epoch>_<train|test|metrics>.<labels|txt>
 ```
