# function to check if a number is prime, appling the good pratices of split functions

def is_prime(a: int):
    return bool(a % 2)


def main ():
    print(is_prime(10))
    

if __name__ == "__main__":
    main()