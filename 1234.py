class RedButton:

    def __init__(self):
        self.click_counter = 0

    def click(self):
        print('Тревога!')
        self.click_counter += 1
    def count(self):
        return self.click_counter

class Programmer:

    def __init__(self, name, position):
        self.position = position
        self.name = name
        self.worked_hours = 0
        self.promotion = 0

    def get_salary(self):
        if self.position == 'Junior':
            return 10
        elif self.position == 'Middle':
            return 15
        elif self.position == 'Senior':
            return 20
    def get_total_salary(self):
        return self.worked_hours * (self.promotion + self.get_salary())

    def info(self):
        return f'Имя: {self.name} | Отработанные часы: {self.worked_hours} | Должность: {self.position} | Зарплата: {self.get_total_salary()}'

    def work(self, time):
        self.worked_hours += time

    def rise(self):

        if self.position == 'Junior':
            self.position = 'Middle'

        elif self.position == 'Middle':
            self.position = 'Senior'

        elif self.position == 'Senior':
            self.promotion += 1




worker = Programmer('programmer1', 'Middle')
print(worker.info())
worker.work(10)
print(worker.info())
worker.rise()
print(worker.info())

print(worker.info())