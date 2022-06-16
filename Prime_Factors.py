import math


def return_num(n):
    for i in range(2, n + 1):
        for j in range(math.ceil(i / 2) + 1):
            if (j == 0) or (j == 1):
                continue

            if i % j == 0:
                break
            else:
                if (j == math.ceil(i / 2)):
                    yield (i)
                else:
                    continue
        if i == 2:
            yield (i)


def return_fac(val, lst):
    for i in lst:
        if val % i == 0:
            val = val / i
            return val, i
    return val,-1


def main():
    m = int(input("Enter the number whose prime factors are required : "))
    lst = []
    for i in return_num(m):
        lst.append(i)

    fac_lst = []
    m,factor = return_fac(m, lst)
    if factor != -1:
            fac_lst.append(factor)
    while factor != -1:
        m,factor = return_fac(m, lst)
        if factor != -1:
            fac_lst.append(factor)

    print(fac_lst)


if __name__ == '__main__':
    main()

