# pair sum - sorted

# given an array find the indexex for two values that when summed will give the target value


arr = [-5,-2,-2,1,3,9]
target = -7

def pair_sum_sorted_brute_force(arr):
    result_list= []
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                result_list.append((i,j))
    return result_list

def pair_sum_sorted_pointer(arr):
    left, right = 0, len(arr)-1
    while left < right:
        _sum = arr[left] + arr[right]
        if _sum < target:
            left += 1
        elif _sum > target:
            right -= 1
        else:
            return [left,right]
    return  []


if __name__ == "__main__":
    print(pair_sum_sorted_brute_force(arr))
    print(pair_sum_sorted_pointer(arr))
