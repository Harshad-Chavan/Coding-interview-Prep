# move all zeros to the end, maintain the order or relative elemtns perfrom modification in place

arr = [1,0,4,0,5,0,0,0,2]


def basic_with_temp_space():
    temp = []
    for _ in arr:
        if _ != 0:
            arr.remove(_)
            temp.append(_)
    return temp+arr

def shift_zeros_to_right(inp):
    left = 0
    # left is placed at the start, keeps track of where to place the non zero
    # right is looped to find the non-zero
    for right in range(len(inp)):
        if inp[right] != 0:
            inp[left],inp[right] = inp[right], inp[left]
            left += 1
    return inp

def shift_zeros_to_left(inp):
    right = len(inp) - 1
    for left in range(len(inp)-1,-1,-1):
        if inp[left] != 0:
            inp[left], inp[right] = inp[right], inp[left]
            right -= 1
    return inp


if __name__ == "__main__":
    print(basic_with_temp_space())
    print(shift_zeros_to_right([1,0,4,0,5,0,0,0,2]))
    print(shift_zeros_to_left([1,0,4,0,5,0,0,0,2]))