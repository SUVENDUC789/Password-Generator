import random


def listGenerator(start, end):
    a = []
    for i in range(start, end):
        a.append(chr(i))
    return a


if __name__ == '__main__':
    small = listGenerator(97, 123)
    big = listGenerator(65, 91)
    number = listGenerator(48, 58)
    special = listGenerator(35, 39)+list(chr(64))
    try:
        n = int(input("Enter size of your password : "))
        i = 0
        passW = ''
        while (True):
            item = random.choice(small)
            passW += item
            i = i+1
            if n==i:
                break
            item = random.choice(big)
            passW += item
            i = i+1
            if n==i:
                break
            item = random.choice(number)
            passW += item
            i = i+1
            if n==i:
                break
            item = random.choice(special)
            passW += item
            i = i+1
            if n==i:
                break
        print("Your Password length is :",len(passW),"\n")
        print(passW,end='\n')
    except Exception as e:
        print("Note : ", e, " Please enter number ")

    input("\nPress any key to continue ...")
