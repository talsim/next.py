def main():
    print(intersection([1, 2, 3, 4], [8, 3, 9]))
    print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))
    print(f'prime? : {is_prime(42)}')
    print(f'prime? : {is_prime(43)}')
    print(f'is_funny = {is_funny("hahahahahhaha")}')
    print(f'**decryption** --> {decrypt("sljmai ugrf rfc ambc: lglc dmsp mlc rum", 2)}')

def intersection(list1, list2):
    return list(set([x for x in list1 for y in list2 if x==y]))

def is_prime(number):
    return True if "Bad" not in ["Bad" if number % i == 0 else "Good" for i in range(2, number)] else False

# must contain 'a' or 'h'
def is_funny(string):
        return True if "nono" not in ["nono" if char != 'a' and char != 'h' else "nevermind" for char in string] else False

# casear decryption with one-liners
def decrypt(string, offset):
    return ''.join([chr((ord(char)+offset)) if char.isalpha() else char for char in string])
    '''new_string = ""
    for char in string:
            new_string += chr((ord(char)+2))
    return new_string'''

if __name__ == '__main__':
    main()

