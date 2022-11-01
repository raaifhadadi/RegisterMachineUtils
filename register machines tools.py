import math


def decodeall(n):
    if (n == 0):
        print("\n")
        return []
    if (n % 2 == 0):
        pn = int(n) & ~int(n-1)
        p = math.log2(pn)
        c = ((n / pn) - 1) / 2
        print("\n"+ str(n) + " = \n<<" + str(p) + ", " + str(c) + ">>")
        return [p] + decodeall(c)
    else:
        print("\n"+ str(n) + "= \n<<" + str(0) + ", " + str((n-1) / 2) + ">>")
        return [0] + decodeall((n-1) / 2)

def decode(n):
    if (n == 0):
        return [n]
    if (n % 2 == 0):
        pn = int(n) & ~int(n-1)
        p = math.log2(pn)
        c = ((n / pn) - 1) / 2
        return [p, c]
    else:
        return [0, (n-1) / 2]


def dti(x, y):
    return (2**x * (2*y + 1))

def sti(x, y):
    return (2**x * (2*y + 1)) - 1

def itda(n):
    pn = n & ~(n-1)
    p = math.log2(pn)
    x =  p
    yn = n / (2**x)
    y = (yn - 1) / 2
    return "<<" + str(x) + ", " + str(y) + ">>"

def itsa(n):
    return itda(n+1)[1:-1]


def rmi(r,x,y):
    print("<< " + str(2*r+1) + ", " + "<" + str(x) + ", " + str(y) + "> " + ">>")
    print("<< " + str(2*r+1) + ", " + str(sti(x,y)) + ">>")
    return dti(2 * r + 1, sti(x,y))

def rma(r,x):
    print("<< " + str(2*r) + ", " + str(x)  + ">>")
    return dti(2*r, x)


def main():

    # print ("\n\n")
    # print(decodeall(2**46*20483))
    # print ("\n\n")
    # print(decodeall(2**216*833))

    print(decodeall(70602));

    # print ("\n\n")
    # print(itsa(1))

if __name__ == "__main__":
    main()