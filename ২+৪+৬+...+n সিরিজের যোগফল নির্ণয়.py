def sum_series_246_to_n(n):
    """
    2+4+6+...+n সিরিজের যোগফল নির্ণয় করে।

    :param n: মনিটরে প্রদর্শন করতে চাইলে সর্বাধিক সংখ্যা
    :return: সিরিজের যোগফল
    """
    result = sum(range(2, n + 1, 2))
    return result


# n এর মান ইনপুট নেওয়া
n_value = int(input("n এর মান ইনপুট দিন: "))

# সিরিজের যোগফল প্রদর্শন
print("২+৪+৬+...+n সিরিজের যোগফল:", sum_series_246_to_n(n_value))
