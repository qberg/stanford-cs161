import time
from bisect import bisect_left,bisect_right

def read_input(path):
    with open(path) as file:
        data = [int(line) for line in file]
    data = sorted(set(data))
    return data

def two_sum(data, lb=-10000, rb=10000):
    count = 0
    
    for x in data:
        left_idx = bisect_left(data, lb-x)
        right_idx = bisect_right(data, rb-x)
        for y in data[left_idx:right_idx]:
            count+=1
    return count


if __name__ == "__main__":
    start = time.time()

    path_to_file = "tests/twosum.txt"
    data = read_input(path_to_file)

    count = two_sum(data)
    print(f"Number of target values in the interval [-10000,10000] is {count}")
    print(f"Time taken for the algorithm to complete: {time.time() -start} seconds")
 

