from interview import water_stored_basic
from interview_opt import water_stored
import random
# let's test our solution against our basic solution 
def generic_test_black_box(heights):
    # let's use our basic solution as a black box
    print(f"testing heights: {heights}")
    expected = water_stored_basic(heights)
    sol = water_stored(heights)
    if sol == expected:
        print("Asserted Equal")
    else:
        print("Error")

def random_test():
    print("Running Random Test")
    heights = []
    for i in range(20):
        heights.append(random.randint(1, 20))
    generic_test_black_box(heights)

def identical_test(num):
    print("Running Identical Test")
    heights = [num]*20
    generic_test_black_box(heights)

def descending_test():
    print("Running Descending Test")
    heights = []
    for i in range(20):
        heights.append(20-i)
    generic_test_black_box(heights)

def ascending_test():
    print("Running Ascending Test")
    heights = []
    for i in range(1, 21):
        heights.append(i)
    generic_test_black_box(heights)

def generic_test(heights, expected):
    sol = water_stored_basic(heights)
    if sol == expected:
        print("Asserted Equal")
    else:
        print("Error")

def water_stored_basic_test():

    print("Running tests on basic function...")

    heights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    expected = 0
    generic_test(heights, expected)

    heights = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    expected = 0
    generic_test(heights, expected)

    heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    expected = 0
    generic_test(heights, expected)
    
    heights = [14, 17, 15, 3, 18, 19, 6, 10, 19, 7, 10, 9, 16, 11, 1, 17, 12, 3, 13, 17]
    expected = 109
    generic_test(heights, expected)

    heights = [11, 7, 12, 3, 9, 16, 16, 19, 14, 18, 1, 10, 12, 8, 6, 11, 14, 7, 9, 16]
    expected = 86
    generic_test(heights, expected)

    print("\n")

def water_stored_test():
    print("Running tests on optimized function...")
    identical_test(10)
    descending_test()
    ascending_test()
    random_test()
    random_test()
    random_test()

def main():
    water_stored_basic_test()
    water_stored_test()

if __name__ == '__main__':
    main()