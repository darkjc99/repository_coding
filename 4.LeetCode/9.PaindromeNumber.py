def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    original = x
    reverse = 0

    while x > 0:
        last_digit = x % 10  # Extract last digit
        reverse = reverse * 10 + last_digit  # Add last digit to variable "reverse"
        x //= 10  # Eliminate last digit
    return original == reverse


print(isPalindrome(-121))
