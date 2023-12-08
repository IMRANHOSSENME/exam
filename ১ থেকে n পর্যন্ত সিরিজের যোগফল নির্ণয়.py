def sum_series_1_to_n(n):
    """
    1+2+3+...+n সিরিজের যোগফল নির্ণয় করে।

    :param n: মনিটরে প্রদর্শন করতে চাইলে সর্বাধিক সংখ্যা
    :return: সিরিজের যোগফল
    """
    result = sum(range(1, n + 1))
    return result


# n এর মান ইনপুট নেওয়া
n_value = int(input("n এর মান ইনপুট দিন: "))

# সিরিজের যোগফল প্রদর্শন
print("১+২+৩+...+n সিরিজের যোগফল:", sum_series_1_to_n(n_value))
