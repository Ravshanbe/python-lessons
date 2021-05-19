from random import randint, choice
game =True
ck = 1
ch = 1
def findNum(n):
    print("1 dan 10 gacha son o'yladim topa olasizmi?:")
    a = list(range(1, n + 1))
    r = choice(a)



    while True:
        inp = int(input())
        if inp == r:
            print(f"TOPDINGIZ!!! Tabriklayman")
            print(f"Siz {ck} ta urinishda topdingiz")
            break
        elif inp < r:
            print("Xato! Men o'ylagan son bundan kattaroq")
            ck += 1
        else:
            print("Xato! Men o'ylagan son bundan kichikroq")
            ck += 1
def findpc(n):
    while True:
        a = list(range(1, n + 1))
        q = a[:]
        c = choice(q)

        inh = input(
            f"Siz o'ylagan son {c}:(T)to'g'ri,(+)men o'ylagan son bundan kattaroq,(-)men o'ylagan son bundan kichikroq??")

        if inh.lower() == 't':
            print(f"Soningizni {ch} ta taxmin bilan topdim")
            break
        elif inh == '+':
            q = q[c:]
            ch += 1
        elif inh == '-':
            q = q[:c]
            ch += 1
while True:

    print("Keling o'ylagan sonni topish o'yini o'ynaymiz!")
    #
    # print("1 dan 10 gacha son o'ylang. Men topishga harakat qilaman")
    findNum(10)
    s=input("Son o'ylagan bo'lsangiz istalgan tugmani bosing: ")
    if s:
        findpc(10)
    if game:
        if ck == ch:
            print(f"Durrang!! Ikkalamiz ham {ch} ta urinishda topdik")
        elif ck < ch:
            print(f"Siz {ck} ta urinish bilan topdingiz va meni yutdingiz")
        else:
            print(f"Men {ch} ta urinish bilan topdim va yutdim")

    again=input("Yana o'ynaymizmi:(1)ha,(0)yo'q")
    if(again=='0'):
        break








