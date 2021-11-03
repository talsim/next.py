import functools

def main():
    print(double_letter("python"))
    print(double_letter("we are the champions!"))
    print(four_dividers(16))
    print(four_dividers(3))
    print(sum_of_digits(104))
    print(sum_of_digits(123))   

def double_letter(my_str):
    return ''.join(map(concat_chars, list(my_str), list(my_str)))
   
# double_letter helper function
def concat_chars(ch1, ch2):
    return ch1+ch2

def four_dividers(number):
    return list(filter(is_four_dividable, range(1, number+1)))

# four_dividers helper function
def is_four_dividable(num):
    return num % 4 == 0
    
def sum_of_digits(number):
    return functools.reduce(add, map(int, str(number)), 0)

# sum_of_digits helper function
def add(x, y):
    return x + y


if __name__ == '__main__':
    main()
