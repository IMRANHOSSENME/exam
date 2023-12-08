def is_leap_year(year):
    """
    এই ফাংশনটি সালটি লিপিয়ার কিনা নির্ণয় করে।

    :param year: চেক করতে চাইলে সাল
    :return: লিপিয়ার হলে True, নন-লিপিয়ার হলে False
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


# সাল ইনপুট নেওয়া
input_year = int(input("সাল ইনপুট দিন: "))

# ফাংশনটি কল করে লিপিয়ার কিনা নির্ণয় এবং প্রদর্শন
if is_leap_year(input_year):
    print(f"{input_year} লিপিয়ার সাল।")
else:
    print(f"{input_year} নন-লিপিয়ার সাল।")
