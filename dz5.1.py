def readData():
    #EXCEPT ZA UNOS NEPOSTOJECE I PRAZNE DATOTEKE
    '''
    Reading the names of files, opening input file and reading from it, then closing it. Creating a new file.
    :return: read data from first file(a list), opened second file for writing.
    '''
    temp = input().split()
    try:
        openForReading = open(temp[0], "r")
    except IOError:
        print("DAT_GRESKA")
        quit()
    openNew = open(temp[1], "w")
    wholeFile = openForReading.readlines()
    openForReading.close()
    return wholeFile, openNew
def readYears():
    #NEPRAVILAN UNOS GODINA
    '''
    The function gets two numbers(years), range of years in which we are calculating the most unpopular movie.
    :return: two years
    '''
    try:
        startYear = int(input())
        endYear = int(input())
    except EOFError:
        quit()
    return startYear, endYear
def separateList(arr):
    '''
    Separate the original data from an input file to lists of parameters we need for calculation
    :param arr: list of data from a file
    :return: lists of needed parameters
    '''
    del arr[0]
    genre = []
    date = []
    money = []
    for i in range(len(arr)):
        temp = [item.strip() for item in arr[i].split(";")]
        genre.append(temp[2])
        date.append(temp[3])
        money.append(temp[5])
    for i in range(len(money)):
        money[i] = float(money[i][1:-1])
    return genre, date, money
def genreList(genre):
    '''
    :param genre: Gets a list of all generes in a file, unseparated
    :return: returs a list of all generes that are in the file
    '''
    genrelist = []
    for gen in range(len(genre)):
        sp = genre[gen].split("|")
        for i in range(len(sp)):
            if sp[i] not in genrelist:
                genrelist.append(sp[i])
    return genrelist
def positionOfaGenre(genre,arr):
    '''
    Gives information of all genre positions in a file.
    :param genre: one genre that we want to know all positions of in a original data file
    :param arr: input data file
    :return:
    '''
    genPosition = []
    for i in range(len(arr)):
        if genre in arr[i]:
            genPosition.append(i)
    return genPosition
def GenreRevenueForTheYear(arr, gen, yarr, genre, year1, year2):
    '''
    :param arr: list of money that each movie made
    :param gen: list of all genres that appear in that input file
    :param yarr: list of all the years
    :param genre: list of all movie genres in an input file
    :param year1: starting year
    :param year2: ending year
    :return: returns list of lists, each list has how much money each genre made that year
    '''
    #NEPRAVILNA KONVERZIJA TIPA PODATAKA
    final = []
    while year1 <= year2:
        moneyOfGenresPerYear = []
        for i in range(len(gen)):
            cost = []
            genP = positionOfaGenre(gen[i], genre)
            for j in genP:
                if int(yarr[j][-4:]) == year1:
                    cost.append(arr[j]) #lista para jednog zanra za jednu godinu
            sumMoney = sum(cost) if len(cost) > 0 else -1
            moneyOfGenresPerYear.append((gen[i], sumMoney))
        final.append(moneyOfGenresPerYear)
        year1 += 1
    return final
def leastPopularGenre(arr):
    '''
    :param arr: list of lists, each list has information about how much each genre made that year
    :return: returns list of lists, each list has minimum revenue of the year
    '''
    k = []
    least = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            s = arr[i][j][1]
            if s != -1:
                k.append(s)
        minG = min(k) if len(k) != 0 else 0
        k = []
        least.append(minG)
    return least
def writeFile(arrm,arrmg, file,year):
    '''
    Writes to an opened file
    :param arrm: list of lists, each list has minimum revenue of the year
    :param arrmg: list of lists, each list has how much money each genre made that year
    :param file: file to write into
    :param year: starting year
    :return: None
    '''
    file.write("Year;Movie Genre;Genre Revenue\n")
    final = []
    tmp = []
    for i in range(len(arrmg)):
        for j in range(len(arrmg[i])):
            if arrm[i] == arrmg[i][j][1]:
                tmp.append(arrmg[i][j])
        final.append(tmp)
        tmp = []
    st = ""
    for k in range(len(final)):
        if len(final[k]) == 1:
            file.write(str(year) + ";" + str(final[k][0][0]) + ";" + "%.2f" % (final[k][0][1])+"\n")
        elif len(final[k]) > 1:
            for s in range(len(final[k])):
                if s != len(final[k])-1:
                    st += str(final[k][s][0]) + "|"
                else: st += final[k][s][0]
            file.write(str(year) + ";" + str(st) + ";" + str(final[k][1][1]) + "\n")
            st = ""
        year += 1
    file.close()

data, new = readData()
sYear, eYear = readYears()
genre, date, money = separateList(data)
genres = genreList(genre)
listOfMoneyPerYearsOfGenre = GenreRevenueForTheYear(money, genres, date, genre, sYear, eYear)
listOfMoney = leastPopularGenre(listOfMoneyPerYearsOfGenre)
writeFile(listOfMoney, listOfMoneyPerYearsOfGenre, new, sYear)