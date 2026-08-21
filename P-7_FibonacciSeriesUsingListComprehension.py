'''Write a Python program to generate the Fibonacci series up to $n$ terms using list comprehension. '''

n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci series: [0]")
else:
    a, b = 0, 1

    fib_series = [a, b] + [(c := a + b, a := b, b := c)[0] for _ in range(n - 2)]
    
    print("Fibonacci series",*fib_series)


