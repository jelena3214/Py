sent = input()
def removeLetter(sent):
    lista = sent.split(" ")
    inter = [".", ",", "!", "?", ":", ";"]
    temp = []
    for i in range(len(lista)):
        st = lista[i]
        if st[0].lower() == st[len(st)-1].lower():
            temp.append(st[1:len(st)-1])
        elif st[0] in inter:
            if st[1].lower() == st[len(st)-1].lower() and len(st[1:len(st)-1]) != 2:
                temp.append(st[0]+st[2:len(st)-1])
            else:
                temp.append(st)
        elif st[len(st)-1] in inter:
            if st[0].lower() == st[len(st)-2].lower() and len(st[0:len(st)-1]) != 2:
                temp.append(st[1:len(st)-2]+st[len(st)-1])
            else:
                temp.append(st)
        else:
            temp.append(st)
    return temp
temp1 = removeLetter(sent)
isp = " ".join(temp1)
print(isp)