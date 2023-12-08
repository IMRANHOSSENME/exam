
number = float(input("একটি সংখ্যা ইনপুট দিন: "))

if number > 0:
    print(f"{number} হলো ধনাত্নক সংখ্যা।")
elif number < 0:
    print(f"{number} হলো ঋণাত্বক সংখ্যা।")
else:
    print("এটি শূন্য সংখ্যা।")
