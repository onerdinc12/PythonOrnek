aPartisiVekili = 0
bPartisiVekili = 0
cPartisiVekili = 0
secilecekVekilSayisi = 6
type(secilecekVekilSayisi)


aPartisiOyu = 90000
bPartisiOyu = 60000
cPartisiOyu = 35000

for i in range(0,secilecekVekilSayisi):
    if(aPartisiOyu > bPartisiOyu and aPartisiOyu>cPartisiOyu):
        aPartisiOyu = aPartisiOyu / 2
        aPartisiVekili = aPartisiVekili + 1
    elif (bPartisiOyu > aPartisiOyu and bPartisiOyu > cPartisiOyu):
        bPartisiOyu = bPartisiOyu / 2
        bPartisiVekili = bPartisiVekili+1
    elif(cPartisiOyu>aPartisiOyu and cPartisiOyu>bPartisiOyu):
        cPartisiOyu = cPartisiOyu / 2
        cPartisiVekili = cPartisiVekili + 1
    else:
        print("Bişiler Hatalı")

print("Sonuçlar a partisi vekili",aPartisiVekili,"B partisi vekili",bPartisiVekili,"C partisi vekili ",cPartisiVekili)