def blocks(n):
    return 0 if n <= 0 else blocks(n - 1) + n

#print(blocks(8))
#print(blocks(0))
#print(blocks(-1))
#print(blocks(1))
#print(blocks(990))

def sum_of_digits(n):
    return 0 if n <= 0 else sum_of_digits(n // 10) + n % 10

#print(sum_of_digits(1234))
#print(sum_of_digits(45))
#print(sum_of_digits(900))

def factorial(n):
    return 1 if n <= 0 else factorial(n - 1) * n

#print(factorial(5))
#print(factorial(0))
#print(factorial(10))

def is_palindrome(s):
    s_backwards= s[::-1]
    

def print_count_down(n):
    if n <= 0:
        print("BOOM")
    else:
        print(n)
        print_count_down(n - 1)

print_count_down(4)