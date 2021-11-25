

def find_divisors(number):

    divisors_list = []

    for divisor in range(1,number+1):
        if(number % divisor == 0):
            divisors_list.append(divisor)
    
    return divisors_list