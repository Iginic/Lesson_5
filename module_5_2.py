class House:
    def __init__(self, name, number_of_floors):
        self.new_floor = None
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        prt = f'Название:{self.name}, кол-во этажей :{self.number_of_floors}'
        return prt

    def go_to(self, new_floor):
        self.new_floor = int(new_floor)
        for i in range(1, new_floor+1):
            if new_floor > self.number_of_floors or new_floor < 1:
                print('Такого этажа не существует!')
                return
            else:
                print(i)


h1 = House('ЖК Горский', 10)
h2 = House('Домик в деревне', 20)
#h1.go_to(9)
#h2.go_to(3)

print(h1)
print(h2)
print(len(h1))
print(len(h2))