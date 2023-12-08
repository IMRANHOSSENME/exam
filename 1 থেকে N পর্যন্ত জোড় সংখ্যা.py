def even_numbers(N):

    for number in range(1, N + 1):
        if number % 2 == 0:
            print(number)

N = int(input("মান ইনপুট দিন: "))

even_numbers(N)
