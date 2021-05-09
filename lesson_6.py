#задание 1

from  time import sleep

class TrafficLight:

    __color = ['Красный', 'Желтый', 'Зеленый']

    def runnig(self):
        i = 0
        while i !=3:
            print(TrafficLight.__color[i])
            
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(6)
            elif i == 2:
                sleep(5)
            i+=1

tim = TrafficLight()
tim.runnig()


#задание 2

class road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.height = 5
        self.weigth = 25
    
    def raschet(self):
        raschet = self._length * self._width * self.height * self.weigth / 1000
        print(f'Для покрытия всего дорожного полотна неободимо {round(raschet)} массы асфальта')


ras = road(5000, 20)
ras.raschet()


#задание 3

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.position + ' ' + self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

pos = Position('Vlad', 'Komarov', 'manager', '20000', '5000')
print(pos.get_full_name(), pos.get_total_income()) 


#задание 4

class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.speed = speed 
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f' {self.name} поехала.'
    def stop(self):
        return f'\n{self.name} остановилась.'
    def turn(self, direction):   
        return f'\n {self.name} поворачивает {direction}' 
    def show_speed(self):
        return f'\nВы движетесь со скоростью {self.speed}'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВы движитесь слишком быстро! Ваша скорость {self.speed}'
        else:
            return f'Скорость {self.name} нормальная'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВы движитесь слишком быстро! Ваша скорость {self.speed}'
        else:
            return f'Скорость {self.name} нормальная'

class PoliceCar(Car):
    pass


t = TownCar('Nissan', 80, 'blue', False)
print('1:\n' + t.go(), t.show_speed(), t.turn('налево'), t.turn('направо'), t.stop())

s = SportCar('VW', 170, 'red', False)
print('2:\n' + s.go(), s.show_speed(), s.turn('налево'), s.stop())

w = WorkCar('Chevrolet', 30, 'red', False)
print('3:\n' + w.go(), w.show_speed(), w.turn('направо'), w.stop())

p = PoliceCar('Toyota', 100, 'yellow', True)
print('4:\n' + p.go(), p.show_speed(), p.turn('направо'), p.stop())

#задание 5

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'

class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'
class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'
class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


p = Pen('ручкой')
print(p.draw())
pl = Pencil('карандашом')
print(pl.draw())
h = Handle('маркером')
print(h.draw())
