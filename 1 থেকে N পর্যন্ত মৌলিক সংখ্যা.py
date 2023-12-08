def is_prime(number):

    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def prime_numbers(N):

    for number in range(1, N + 1):
        if is_prime(number):
            print(number)

N = int(input("মান ইনপুট দিন: "))

prime_numbers(N)
