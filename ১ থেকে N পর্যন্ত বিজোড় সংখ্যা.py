def display_odd_numbers(N):
    """
    1 থেকে N পর্যন্ত বিজোড় সংখ্যা মনিটরে প্রদর্শন করে।

    :param N: মনিটরে প্রদর্শন করতে চাইলে সর্বাধিক সংখ্যা
    """
    for number in range(1, N + 1):
        if number % 2 != 0:
            print(number)


# N এর মান ইনপুট নেওয়া
N = int(input("N এর মান ইনপুট দিন: "))

# বিজোড় সংখ্যা প্রদর্শন
display_odd_numbers(N)
