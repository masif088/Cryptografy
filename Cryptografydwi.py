def pola1(depan, belakang):
    final = []
    belakang[0], belakang[3] = belakang[3], belakang[0]
    belakang[1], belakang[2] = belakang[2], belakang[1]
    for n in range(len(belakang)):
        final.append(depan[n] + belakang[n])
    return final

def pola2(depan, belakang):
    reverse = []
    for n in belakang:
        reverse.append(n[::-1])
    rez = [[depan[j][i] for j in range(len(depan))] for i in range(len(depan[0]))]
    reza = [[reverse[j][i] for j in range(len(reverse))] for i in range(len(reverse[0]))]
    tranposeDepan = []
    tranposeBelakang = []
    temp = ""
    for i in rez:
        for j in i:
            temp += j
        tranposeDepan.append(temp)
        temp = ""
    for i in reza:
        for j in i:
            temp += j
        tranposeBelakang.append(temp)
        temp = ""
    final = []
    for n in range(len(belakang)):
        final.append(tranposeDepan[n] + tranposeBelakang[n])
    return final

plain = "dwiidwiidwiidwii"
asciicode = []
depan = []
belakang = []
for i in plain:
    z = '{0:08b}'.format(ord(i))
    depan.append(str(z)[0:4])
    belakang.append(str(z)[4:8])
    asciicode.append(z)
while len(asciicode) % 4 != 0:
    asciicode.append('{0:08b}'.format(32))
    depan.append('{0:08b}'.format(32)[0:4])
    belakang.append('{0:08b}'.format(32)[4:8])
belakanga = []
depana = []
final = []
for n in range(int(len(asciicode) / 4)):
    for m in range(4):
        belakanga.append(belakang[n * 4 + m])
        depana.append(depan[n * 4 + m])
    if n % 2 == 0:
        final.append(pola1(depana, belakanga))
    else:
        final.append(pola2(depana, belakanga))
    belakanga = []
    depana = []
final1 = []
for z in final:
    for y in z:
        final1.append((int(y, 2)))
print(final1)
key = (10, 25, 20, 10)
chiper = []
keyadd = []
aaaa=[]
for i in range(len(final1)):
    temp = final1[i] + key[i % len(key)]
    temp = temp % 256
    if 126 < temp <= 160:
        temp += 33
        keyadd.append(1)
    elif temp < 32:
        temp += 32
        keyadd.append(1)
    else:
        keyadd.append(0)
    chiper.append(chr(temp))
    aaaa.append(temp)
print(aaaa)
asd=[]
for i in range(len(chiper)):
    temp = ord(chiper[i])
    if keyadd[i] == 1:
        if temp < 65:
            temp -= 32
        else:
            temp -= 33
    temp -= key[i % len(key)]
    if temp < 0:
        temp += 256
    asd.append(temp)
for i in asd:
    print('{0:08b}'.format(i))
# print(asd)