sentence = input()
punctation = [".", ",", "!", "?", ":", ";"]
def check(sentance):
    for i in sentance:
        if i not in punctation and i != " " and i.isalpha() == False and i.isdigit() == False:
            quit()
def prepare(sentance):
    sentance = sentance.strip()
    x = []
    s = ""
    pos = 0
    index1 = index2 = 0
    for i in range(len(sentance)):
        if sentance[i] in punctation:
            index1 = i
            if pos < index1:
                x.append(s)
                s = ""
            x.append(sentance[i])
        elif sentance[i] == " ":
            index2 = i
            if pos < index2:
                x.append(s)
                s = ""
            x.append(sentance[i])
        else:
            pos = i
            s += sentance[i]
    if len(s) != 0:
        x.append(s)
    return x
def recursion(element):
    if element[0].lower() == element[-1].lower() and len(element) > 2:
        temp = element[1:-1]
        return recursion(temp)
    return element
def withoutFirstandLast(elements):
    final = []
    for i in range(len(elements)):
        if elements[i] not in punctation:
            if len(elements[i]) >= 3:
                temp1 = recursion(elements[i])
                final.append(temp1)
            else:
                final.append(elements[i])
        else:
            final.append(elements[i])
    return final
def joinList(characters):
    tmp = "".join(characters)
    print(tmp, end="")
check(sentence)
tempor = prepare(sentence)
joinList(withoutFirstandLast(tempor))