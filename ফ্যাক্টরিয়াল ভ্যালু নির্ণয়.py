def factorial(n):

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# সংখ্যা ইনপুট নেওয়া
num = int(input("একটি সংখ্যা ইনপুট দিন: "))

# ফ্যাক্টরিয়াল ভ্যালু প্রদর্শন
result = factorial(num)
print(f"{num} এর ফ্যাক্টরিয়াল হলো: {result}")
