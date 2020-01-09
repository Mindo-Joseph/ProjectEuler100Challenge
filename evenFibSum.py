def evenFibSum(n):
    fib_numbers = [1,1,2]
    even_array = []

    for _ in range(n-3):
        fib_numbers.append(fib_numbers[-1]+fib_numbers[-2])
    for i in fib_numbers:
        if i%2 == 0:
            even_array.append(i)
    return sum(even_array)



