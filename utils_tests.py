import utils_class

test = utils_class.utils()

# Test case 1: reversed with int
testCase1 = test.reversed(901)

if (testCase1 == 109):
    print('Test Case 1: Passed')
else:
    print('Test Case 1: Failed')

# Test case 2: reversed with float
testCase2 = test.reversed(5.06)

if (testCase2 == -1):
    print('Test Case 2: Passed')
else:
    print('Test Case 2: Failed')

# Test case 3: reversed with string
testCase3 = test.reversed('901')

if (testCase3 == -1):
    print('Test Case 3: Passed')
else:
    print('Test Case 3: Failed')

# Test case 4: formatter with int
testCase4 = test.formatter(105)

if (testCase4 == ['0b1101001', '0o151']):
    print('Test Case 4: Passed')
else:
    print('Test Case 4: Failed')

# Test case 5: formatter with float
testCase5 = test.formatter(86.02)

if (testCase5 == [-1, -1]):
    print('Test Case 5: Passed')
else:
    print('Test Case 5: Failed')

# Test case 6: formater with string
testCase6 = test.formatter('105')

if (testCase6 == [-1, -1]):
    print('Test Case 6: Passed')
else:
    print('Test Case 6: Failed')