import re
import os
import datetime
def readData():
    """
    Reading the names of files, opening input file and reading from it, then closing it. Creating a new file.
    :return: read data from first file(a list), opened second file for writing.
    """
    temp = input().split()
    try:
        openForReading = temp[0]
        with open(openForReading, "r") as openForReading:
            wholeFile = openForReading.readlines()
    except IOError or FileNotFoundError:
        print("DAT_GRESKA")
        quit()
    filesize = os.path.getsize(temp[0])
    if filesize == 0:
        print("DAT_GRESKA")
        quit()
    openNew = temp[1]
    return wholeFile, openNew
def readYears():
    """
    The function gets two numbers(years), range of years in which we are calculating the most unpopular movie.
    :return: two years
    """
    patty1 = re.compile(r".{4}")
    try:
        startYear = input()
        endYear = input()
        if patty1.search(startYear) and patty1.search(endYear):
            return int(startYear), int(endYear)
        else:
            print("POLJE_GRESKA")
            quit()
    except ValueError:
        print("KONV_GRESKA")
        quit()
def separateValues(darr):
    """
    :param darr: file separated into list with readlines function
    :return:list of years, revenue and genres
    """
    del darr[0]
    genre = []
    date = []
    money = []
    patt = re.compile(r".{2}\..{2}\..{4}")
    pattm = re.compile(r'\$.+(.)?')
    for i in range(len(darr)):
        temp = [item.strip() for item in darr[i].split(";")]
        genre.append(temp[2])
        date.append(temp[3])
        money.append(temp[5])
    for i in range(len(money)):
        try:
            if pattm.search(money[i]):
                money[i] = float(money[i][1:])
            else:
                print("POLJE_GRESKA")
                quit()
            if patt.search(date[i]):
                day = int(date[i][:2])
                month = int(date[i][3:5])
                date[i] = int(date[i][-4:])
                try:
                    date_check = datetime.datetime(date[i], month, day)
                except:
                    print("POLJE_GRESKA")
                    quit()
            else:
                print("POLJE_GRESKA")
                quit()
        except ValueError:
            print("KONV_GRESKA")
            quit()
    return genre, date, money
def processing(year, genre, money):
    """
    :param year: list of years
    :param genre: lst of genres
    :param money: revenue list
    :return: dict(keys are years, values are dicts whose keys are generes and values are revenues)
    """
    dic = {}
    for i in range(len(year)):
        if year[i] not in dic:
            dic[year[i]] = {}
        sp = genre[i].split("|")
        for gen in sp:
            if gen not in dic[year[i]]:
                dic[year[i]][gen] = 0
            dic[year[i]][gen] += money[i]
    return dic
def LeastPopularGenre(dict, syear, eyear):
    """
    :param dict: dict of data
    :param syear: starting year
    :param eyear: ending year
    :return: returns a list of strings, each string contains year, least popular movie genre/s of that year and there revenue
    """
    tup = ""
    g = ""
    temp = []
    for keys, item in dict.items():
        try:
            if int(keys) >= syear and int(keys) <= eyear:
                tem = min(item.values())
                gen = [i for i in item if item[i] == tem]
                if len(gen) == 1:
                    tup += str(keys) + ";" + str(gen[0]) + ";" + "%.2f" % tem + "\n"
                    temp.append(tup)
                    tup = ""
                else:
                    for k in range(len(gen)):
                        if k != len(gen) - 1:
                            g += gen[k] + "|"
                        else: g += gen[k]
                    tup += str(keys) + ";" + g + ";" + "%.2f" % tem + "\n"
                    temp.append(tup)
                    tup = g = ""
            for i in range(len(temp)):
                for j in range(i + 1, len(temp)):
                    if int(temp[i][:4]) > int(temp[j][:4]):
                        temp[i], temp[j] = temp[j], temp[i]
        except ValueError:
            print("KONV_GRESKA")
            quit()
    return temp
def writeToFile(file, arr):
    """
    :param file: name of an output file
    :param arr: list containing output data
    :return: None
    """
    s = "Year;Movie Genre;Genre Revenue\n"
    with open(file, "w") as file:
        file.write(s)
        for i in range(len(arr)):
            file.write(arr[i])

data, new = readData()
sYear, eYear = readYears()
genre, date, money = separateValues(data)
dictOfAll = processing(date, genre, money)
finalList = LeastPopularGenre(dictOfAll, sYear, eYear)
writeToFile(new, finalList)
