import random


class Node:
    def __init__(self, info=None):
        self.info = info
        self.prev = None
        self.next = None


class chainedList():
    def __init__(self):
        self.head = None  # inicijalizujemo praznu listu, pokazivac prvog cvora

    def empty(self):
        if self.head == None:
            return True
        return False

    def update(self, info):
        new_node = Node(info)
        if self.head == None:  # ako je prazna
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:  # dodavanje na kraj
            current = self.head
            while current.next != self.head:
                current = current.next
            r = current.next
            current.next = new_node
            new_node.next = self.head
            new_node.prev = current
            r.prev = new_node

    def elem_num(self):  # broj elemenata
        num = 1
        current = self.head
        if self.head == None:
            return 0
        while current.next != self.head:
            current = current.next
            num += 1
        return num

    def remove(self, node):
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


def rand_int(x):
    return random.randint(0, x)


students = chainedList()
queue = chainedList()
students.print_List()
index_list = []
simulation_step_count = 0

while 1:
    choice = input("""
                              1: Unesi studenta
                              2: Kraj upisa studenata u listu
                              3: Pokren simulaciju
                              4: Kraj programa 
                              Unesite neki od ponudjenih brojeva: """)
    if choice == "1":
        info = []
        name = input("Unesi ime studenta")
        info.append(name)
        lastname = input("Unesi prezime studenta")
        info.append(lastname)
        while True:
            ind_num = int(input("Unesi broj indeksa"))
            if ind_num not in index_list:
                index_list.append(ind_num)
                info.append(ind_num)
                break
            else:
                print("Vec postoji student s tim brojem indeksa")
        program = input("Studijski program")
        info.append(program)
        year = int(input("Godina studija"))
        info.append(year)
        students.update(info)
        students.print_List()
    if choice == "2":
        temp = students.elem_num()
        print("Trenutan broj studenata u listi je: {}".format(temp))
        n = temp - 1
        while temp != 0:
            rand = rand_int(n)
            print(rand)
            current = students.head
            while rand > 0:
                current = current.next
                rand -= 1
            print(current.info)
            queue.update(current.info)
            students.remove(current.info)
            n -= 1
            temp -= 1
        queue.print_List()
        students.print_List()
    if choice == "3":
        while True:
            try:
                x = float(input("Unesi neki broj 0 ≤ X ≤ 0.5"))
                if 0 <= x <= 0.5:
                    break
            except:
                print("Los unos")
                continue
        current = queue.head
        while queue.elem_num() != 0:
            s = random.random()
            print(s)
            queue.print_List()
            print(current.info)
            if s < x:
                queue.remove(current.info)
                queue.update(current.info)
                current = current.next
            elif s > x:
                temp = current.info
                print("{} {}, {}".format(temp[0], temp[1], temp[4]))
                queue.remove(current.info)
                current = current.next
            simulation_step_count += 1
        queue.print_List()
        print("Ukupan broj koraka simulacije: {}".format(simulation_step_count))
    if choice == "4":
        quit()
