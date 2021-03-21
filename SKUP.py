# GRESKE PRILIKOM UNOSA PODATAKA
class Node:
    def __init__(self, info=None):
        self.prev = None
        self.info = info
        self.next = None


class chainedList():
    def __init__(self):
        self.head = None  # inicijalizujemo praznu listu, pokazivac prvog cvora

    def empty(self):
        return self.head == None

    def add_new_Node(self, info):  # po rastucem redosledu
        new_node = Node(info)
        if self.head == None:  # ako je prazna
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        elif new_node.info < self.head.info:  # ako umetamo vrednost ispred prvog
            current = self.head.prev
            r = self.head
            current.next = new_node
            new_node.next = self.head
            new_node.prev = current
            r.prev = new_node
            self.head = new_node
        else:  # ako umetamo vrednost bilo gde gledamo po vrednosti cvorove i redjamo rastuce
            current = self.head
            while current.next != self.head and current.next.info < new_node.info:
                current = current.next
            r = current.next
            new_node.next = r
            new_node.prev = current
            current.next = new_node
            r.prev = new_node

    def in_the_list(self, info):
        current = self.head
        if self.head == None:
            return False
        while current.next != self.head:
            if current.info == info:
                return True
            current = current.next
        if current.next == self.head and current.info != info:
            return False
        else:
            return True

    def card_list(self):
        card = 1
        current = self.head
        if self.head == None:
            return 0
        while current.next != self.head:
            current = current.next
            card += 1
        return card

    def remove_Node(self, node):
        current = self.head
        if self.head.next == self.head:
            self.head = None
            return None
        while current.info != node:
            current = current.next
        if current == self.head:
            r = current.next
            t = current.prev
            r.prev = current.prev
            t.next = r
            self.head = r
            del current
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
            del current

    def print_List(self):
        current = self.head
        if current == None:
            print("prazan skup")
            return
        while current.next != self.head:
            print(current.info, end=" ")
            current = current.next
        print(current.info)


def union(set1, set2):
    union_set = chainedList()
    head1 = set1.head
    head2 = set2.head
    while head1 != None or head2 != None:
        addedFrom1 = False
        addedFrom2 = False
        if head1 != None and head2 == None:
            addedFrom1 = True
            union_set.add_new_Node(head1.info)
            head1 = head1.next
        elif head2 != None and head1 == None:
            addedFrom2 = True
            union_set.add_new_Node(head2.info)
            head2 = head2.next
        elif head1 != None and head2 != None and head1.info > head2.info:
            addedFrom2 = True
            union_set.add_new_Node(head2.info)
            head2 = head2.next
        elif head1 != None and head2 != None and head1.info < head2.info:
            addedFrom1 = True
            union_set.add_new_Node(head1.info)
            head1 = head1.next
        elif head1 != None and head2 != None and head1.info == head2.info:
            addedFrom1 = True
            addedFrom2 = True
            union_set.add_new_Node(head2.info)
            head2 = head2.next
            head1 = head1.next
        if head1 != None and head1 == set1.head and addedFrom1:
            head1 = None
        if head2 != None and head2 == set2.head and addedFrom2:
            head2 = None
    return union_set


def intersection(set1, set2):
    intersection_set = chainedList()
    head1 = set1.head
    head2 = set2.head
    while head1 != None and head2 != None:
        addedFrom1 = False
        addedFrom2 = False
        if head1 != None and head2 != None and head1.info == head2.info:
            intersection_set.add_new_Node(head1.info)
            head1 = head1.next
            head2 = head2.next
            addedFrom1 = True
            addedFrom2 = True
        elif head1 != None and head2 != None and head1.info < head2.info:
            head1 = head1.next
            addedFrom1 = True
        elif head1 != None and head2 != None and head1.info > head2.info:
            head2 = head2.next
            addedFrom2 = True
        if head1 != None and head1 == set1.head and addedFrom1:
            head1 = None
        if head2 != None and head2 == set2.head and addedFrom2:
            head2 = None
    return intersection_set


def difference(set1, set2):
    difference_set = chainedList()
    head1 = set1.head
    head2 = set2.head
    while head1 != None or head2 != None:
        addedFrom1 = False
        addedFrom2 = False
        if head1 != None and head2 == None:
            addedFrom1 = True
            difference_set.add_new_Node(head1.info)
            head1 = head1.next
        elif head2 != None and head1 == None:
            addedFrom2 = True
            # difference_set.add_new_Node(head2.info)
            head2 = head2.next
        elif head1 != None and head2 != None and head1.info == head2.info:
            head1 = head1.next
            head2 = head2.next
            addedFrom1 = True
            addedFrom2 = True
        elif head1 != None and head2 != None and head1.info < head2.info:
            difference_set.add_new_Node(head1.info)
            head1 = head1.next
            addedFrom1 = True
        elif head1 != None and head2 != None and head1.info > head2.info:
            # difference_set.add_new_Node(head2.info) ako je asimetricna
            head2 = head2.next
            addedFrom2 = True
        if head1 != None and head1 == set1.head and addedFrom1:
            head1 = None
        if head2 != None and head2 == set2.head and addedFrom2:
            head2 = None
    return difference_set


def remove_set(set):
    current = set.head
    while current.next != set.head:
        set.remove_Node(current.info)
        current = current.next
    set.remove_Node(current.info)


def menu(dictionary):
    choice = input("""
                          1: Ucitavanje novog skupa
                          2: Dodavanje clana skupa
                          3: Brisanje clana skupa
                          4: Ispis skupa
                          5: Unija dva skupa
                          6: Presek dva skupa
                          7: Razlika dva skupa
                          8: Brisanje skupa
                          9: Kraj programa
                          Unesite neki od ponudjenih brojeva: """)
    if choice == "1":
        if len(dictionary) > 5:
            print("Ispunili ste max broj skupova(5)")
            menu(dictionary)
        name = input("Unesite ime skupa")
        if name not in dictionary:
            dictionary[name] = chainedList()
        print("Unosite vrednosti skupa")
        while True:
            info = input()
            if len(info) > 0:
                try:
                    if not dictionary[name].in_the_list(int(info)):
                        dictionary[name].add_new_Node(int(info))
                except:
                    print("Los unos")
            else:
                break
        dictionary[name].print_List()
    if choice == "2":
        name = input("Unesite ime skupa u koji zelite da dodate element")
        if name not in dictionary:
            print("Ne postoji taj skup")
            menu(dictionary)
        try:
            print("Unesite vrednost")
            info = int(input())
        except:
            print("Los unos")
        if not dictionary[name].in_the_list(info):
            dictionary[name].add_new_Node(info)
    if choice == "3":
        name = input("Unesite ime skupa iz kojeg zelite da obrisete element")
        if name not in dictionary:
            print("Ne postoji taj skup")
            menu(dictionary)
        try:
            print("Unesite vrednost")
            info = int(input())
            if dictionary[name].in_the_list(info):
                dictionary[name].remove_Node(info)
            else:
                print("Ne postoji taj element u skupu")
        except:
            print("Los unos")
    if choice == "4":
        name = input("Unesite ime skupa koji zelite da ispisete")
        if name not in dictionary:
            print("Ne postoji taj skup")
            menu(dictionary)
        dictionary[name].print_List()
    if choice == "5":
        name = input("Unesite ime skupa 1")
        name1 = input("Unesite ime skupa 2")
        name2 = input("Unesite ime nastalog skupa")
        if name2 not in dictionary:
            dictionary[name2] = union(dictionary[name], dictionary[name1])
        else:
            print("Vec postoji to ime skupa")
    if choice == "6":
        name = input("Unesite ime skupa 1")
        name1 = input("Unesite ime skupa 2")
        name2 = input("Unesite ime nastalog skupa")
        if name2 not in dictionary:
            dictionary[name2] = intersection(dictionary[name], dictionary[name1])
            if dictionary[name2].empty() == True:
                print("Nema preseka")
        else:
            print("Vec postoji to ime skupa")
    if choice == "7":
        name = input("Unesite ime skupa 1")
        name1 = input("Unesite ime skupa 2")
        name2 = input("Unesite ime nastalog skupa")
        if name2 not in dictionary:
            dictionary[name2] = difference(dictionary[name], dictionary[name1])
            if dictionary[name2].empty() == True:
                print("Nema razlike")
        else:
            print("Vec postoji to ime skupa")
    if choice == "8":
        name = input("Unesite ime skupa koji zelite da izbrisete")
        if name not in dictionary:
            print("Ne postoji taj skup")
        remove_set(dictionary[name])
        del dictionary[name]
    if choice == "9":
        quit()
    menu(dictionary)


dictionary = {}
while 1: menu(dictionary)
