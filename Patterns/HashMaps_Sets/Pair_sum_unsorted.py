# Pair sum Unsorted
# Given a list of interges find a pair that makes tha target

# note the array is unsorted here

inp = [-1,3,4,5,8,1,0,2]
target = 5


def two_pass_approach():
    index_map = dict()

    # iterate over the array and set value and index in map
    for idx,val in enumerate(inp):
        index_map[val] = idx

    for idx, val in enumerate(inp):
        comp = target - val
        if comp in index_map:
            return idx, index_map[comp]
    return

def one_pass_approach():
    index_map = {}

    for idx, num in enumerate(inp):
        comp = target - num
        if comp in index_map.keys():
            return idx, index_map[comp]
        else:
            # add the number itself as it will be someones complement
            index_map[num] = idx
    return


if __name__ == "__main__":
    print(two_pass_approach())
    print(one_pass_approach())