# check if a valid palindrome remove all no alphanumeric characters

palindrome = 'nitin'
not_palindrome = 'he ll o'


def check_palindrome(inp):
    left, right = 0, len(inp) - 1
    while left < right:

        while not inp[left].isalnum() and left < right:
            left += 1
        while not inp[right].isalnum() and left < right:
            right -= 1

        if inp[left] != inp[right]:
            return f"{inp} is not a palindrome"

        left += 1
        right -= 1

    return f"{inp} is a palindrome"


if __name__ == '__main__':
    print(check_palindrome(palindrome))
    print(check_palindrome(not_palindrome))
