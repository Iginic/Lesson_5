class House:
    def __init__(self, name, number_of_floors):
        self.new_floor = None
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = int(new_floor)
        for i in range(1, new_floor+1):
            if new_floor > self.number_of_floors or new_floor < 1:
                print('Такого этажа не существует!')
                return
            else:
                print(i)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 5)
h1.go_to(19)
h2.go_to(2)
