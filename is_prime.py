def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if(number % i) == 0:
                print(number, "is not a prime number")
                break
            else:
                print(number, "is a prime number")
    else:
        print(number, "is not a prime number")
        
print(is_prime(7))
print(is_prime(8))