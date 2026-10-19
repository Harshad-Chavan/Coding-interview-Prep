# given an array of integers return all triplets [a,b,c] where a + b + c = target
# solution must not contain duplicate triplets [1,2,3] X [3,2,1]
# no such triplets are foung return empty array


arr = [-4, -3, -2, -1, 0, 1, 3, 6, 9, 10]
target = -9


def triplet_sum_sorted(arr):
    triplets = set()

    # main loops
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if arr[i] + arr[j] + arr[k] == target:
                    triplets.add(tuple(sorted([i,j,k])))

    return triplets


# Approach 2 : a + b + c = target
# in our case b + c = target - a
# b + c = 15 - a

# this loops traverses the main arr elemnets
def main_loop(arr):
    triplets = []

    arr.sort()
    for a in range(len(arr)):

        # this check is for same numbers in sqequence
        if a > 0 and arr[a] == arr[a-1]:
            continue

        pairs = pair_sum_sorted_pointer(arr, a+1, target-arr[a])

        for pair in pairs:
            triplets.append([a,*pair])

    return triplets

def pair_sum_sorted_pointer(nums,start,target_val):
    pairs = []
    end = len(nums)-1
    while start < end:
        _sum = nums[start] + nums[end]
        if _sum < target_val:
            start +=1
        elif _sum > target_val:
            end -= 1
        else:
            pairs.append([start,end])
            start += 1
    return pairs

if __name__ == "__main__":
    print(triplet_sum_sorted(arr))
    print(main_loop(arr))