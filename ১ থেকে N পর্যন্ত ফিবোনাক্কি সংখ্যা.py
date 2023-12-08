def display_fibonacci_numbers(N):
    """
    1 থেকে N পর্যন্ত ফিবোনাক্কি সংখ্যা মনিটরে প্রদর্শন করে।

    :param N: মনিটরে প্রদর্শন করতে চাইলে সর্বাধিক সংখ্যা
    """
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= N:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    for number in fib_sequence:
        print(number)


# N এর মান ইনপুট নেওয়া
N = int(input("N এর মান ইনপুট দিন: "))

# ফিবোনাক্কি সংখ্যা প্রদর্শন
display_fibonacci_numbers(N)
