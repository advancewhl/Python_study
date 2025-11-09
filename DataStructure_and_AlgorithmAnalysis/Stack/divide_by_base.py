from stack import Stack


def divide_by_base(decimal_num, base):
    digits = "0123456789ABCDEF"
    rem_num = Stack()

    while decimal_num > 0:
        rem = decimal_num % base
        rem_num.push(rem)
        decimal_num = decimal_num // base

    new_string = ""

    while not rem_num.is_empty():
        new_string = new_string + digits[rem_num.pop()]
    return new_string


print(divide_by_base(310000, 16))
