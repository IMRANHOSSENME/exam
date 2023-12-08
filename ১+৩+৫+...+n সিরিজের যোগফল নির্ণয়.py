def sum_series_135_to_n(n):
    """
    1+3+5+...+n সিরিজের যোগফল নির্ণয় করে।

    :param n: মনিটরে প্রদর্শন করতে চাইলে সর্বাধিক সংখ্যা
    :return: সিরিজের যোগফল
    """
    result = sum(range(1, n + 1, 2))
    return result


# n এর মান ইনপুট নেওয়া
n_value = int(input("n এর মান ইনপুট দিন: "))

# সিরিজের যোগফল প্রদর্শন
print("১+৩+৫+...+n সিরিজের যোগফল:", sum_series_135_to_n(n_value))
