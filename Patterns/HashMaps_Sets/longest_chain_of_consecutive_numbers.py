# Find the longest chain of consecutive numbers in an array. Two numbers are consecutive if
# they have a difference of 1.
# Example:
# Input: nums = [1, 6, 2, 5, 8, 7, 10, 3]
# Output: 4
# Explanation: The longest chain of consecutive numbers is 5, 6, 7, 8

def brute_force(inp):
    if not nums:
        return 0

    longest_chain_len= 0
    longest_chain = None
    inp = set(inp)

    for i in inp:
        chain = [i]
        j = i+1
        while j in inp:
            chain.append(j)
            j+=1
        if len(chain) > longest_chain_len:
            longest_chain_len = len(chain)
            longest_chain = chain
    print(longest_chain,longest_chain_len)


def optimized(inp):
    if not nums:
        return 0

    longest_chain_len= 0
    longest_chain = None
    inp = set(inp)

    for i in inp:
        # check if its the smallest element in chain, if yes it means a chain starts from there
        # if not then we can skip the iteration over nums to check each element
        if i-1 not in inp:
            chain = [i]
            j = i + 1
            while j in inp:
                chain.append(j)
                j += 1
            if len(chain) > longest_chain_len:
                longest_chain_len = len(chain)
                longest_chain = chain

    print(longest_chain,longest_chain_len)


if __name__ == "__main__":
    nums = [0,-1, 1, 6, 2, 8, 7, 10, 3]
    brute_force(nums)
    optimized(nums)