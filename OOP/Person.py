import my_dec as dec

# Тут я применяю деккоратор
@dec.check
def check_func(numb):

    return numb

class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age
        self.hobby = "Заполните это поле самостоятельно"
        self.advanced_info = "Отсутсвует"

        print(f"Создан объект класса Person с\nИменем: {self.name}\nВозрастом: {self.age}")

    def __del__(self):

        print(f"Объект класса Person с именем: {self.name} удален")

    def say(self):

        print(f"Введите число от 1 до 3, чтобы выбрать фразу которую скажет: {self.name}")
        
        numb = input()
        phrase = check_func(numb)

        # Пизда уродство, потом через case сделаю или че то по типу поиска диапазона
        if phrase == 1:
            print(f"Данные объекта:\nИмя: {self.name}\n Возраст: {self.age}")
        elif phrase == 2:
            print(f"Увлечения объекта: {self.hobby}")
        elif phrase == 3:
            print(f"Дополнительная информация об объекте: {self.advanced_info}")
        elif phrase > 3 or phrase < 1:

            phrase = "Ошибка"
            return phrase

        phrase = "Успешно"
        return phrase