#Hello guys Welcome back again...
#Day 27 Testing...
#LAnguage Used: Pyhton 3
#Let's start coding..



def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

#We have to write our code after first function minimum_index
class TestDataEmptyArray(obkect):
    @staticmethod
    def get_array():
        return list()

class TestDataUniqueValues(object):
    @staticmethod
    def get_array():
        return[7,9,1,2,-7,10,22]

    @staticmethod
    def get_expected_result():
        return 4

class TestDataExactlyTwoDifferentMinimums(object):
    @staticmethod
    def get_array():
        return [7,9,1,2,-7,10,22,-7]

    @staticmethod
    def get_expected_result():
        return 4

#You have to write this code ion the terminal of hacker rank...
#Thankyou for the support...KEEEP CODING AND KEEP LEARNING..
#I will see you next timee..



def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False

def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")

