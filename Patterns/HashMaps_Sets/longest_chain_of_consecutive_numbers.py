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


if __name__ == "__main__":
    nums = [1, 6, 2, 5, 8, 7, 10, 3]
    brute_force(nums)