#!/usr/bin/python3
a = 10
b = 5

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    add = add(a, b)
    sub = sub(a, b)
    mul = mul(a, b)
    div = div(a, b)

    output = "{} + {} = {}\n{} - {} = {}\n{} * {} = {}\n{} / {} = {}"
    .format(a, b, add, a, b, sub, a, b, mul, a, b, div)

    print(output)
