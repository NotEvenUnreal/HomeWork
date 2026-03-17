import numpy as np
import random

pc=12
members=24
# def random_seating_arrangement(pc):
col1 = []

for num_pc in range(1, pc+1):
    col1.append([num_pc])


col1 = np.array(col1)
member_ids = list(range(1, members+1))
random.shuffle(member_ids)



col2 = []
col3 = []

for num_pc in range(pc):
    col2.append([member_ids[num_pc]])
    col3.append([member_ids[num_pc+pc]])

col2 = np.array(col2)
col3 = np.array(col3)



result = []

for num_pc in range(pc):
    row = [
        col1[num_pc][0],
        col2[num_pc][0],
        col3[num_pc][0],
    ]
    result.append(row)
result = np.array(result)

print("Номера рабочих мест:", result[:, 0])
print("Ученик 1:           ", result[:, 1])
print("Ученик 2:           ", result[:, 2])





import numpy as np
import random


def random_seating_arrangement():
    print("Распределение - 2 ученика на 1 рабочее место")
    pc = int(input("Введите число рабочих мест:"))
    members = int(input("Введите число учащихся:"))
    col1 = []

    for num_pc in range(1, pc+1):
        col1.append([num_pc])


    col1 = np.array(col1)
    member_ids = list(range(1, members+1))
    random.shuffle(member_ids)



    col2 = []
    col3 = []

    for num_pc in range(pc):
        col2.append([member_ids[num_pc]])
        col3.append([member_ids[num_pc+pc]])

    col2 = np.array(col2)
    col3 = np.array(col3)



    result = []

    for num_pc in range(pc):
        row = [
            col1[num_pc][0],
            col2[num_pc][0],
            col3[num_pc][0],
        ]
        result.append(row)
    result = np.array(result)

    print("Номера рабочих мест:", result[:, 0])
    print("Ученик 1:           ", result[:, 1])
    print("Ученик 2:           ", result[:, 2])

random_seating_arrangement()

















import  numpy as np
class Weather:
    def __init__(self, date, temp_day, temp_night, wind_speed, humidity, precipitation, uv):

        """
        date - дата (строка "20.03")
        temp_day - температура днем
        temp_night - температура ночью
        wind_speed - скорость ветра м/c
        humidity - влажность (%)
        precipitation - вероятность осадков (%)
        uv - индекс ультрафиолета
        """

        self.date = date
        self.temp_day = temp_day
        self.temp_night = temp_night
        self.wind_speed = wind_speed
        self.humidity = humidity
        self.precipitation = precipitation
        self.uv = uv

days = [
    Weather("11.03", 6, -5, 4, 78, 20, 3),
    Weather("12.03", 6, -2, 3, 76, 34, 2),
    Weather("13.03", 8, -1, 3, 78, 33, 1),
    Weather("14.03", 9, 1, 3, 74, 25, 2),
    Weather("15.03", 9, -1, 1, 72, 68, 1),
    Weather("16.03", 8, -1, 1, 71, 37, 2),
    Weather("17.03", 8, 0, 1, 69, 56, 2),
    Weather("18.03", 8, 0, 2, 70, 54, 2),
    Weather("19.03", 8, -1, 1, 70, 66, 2),
    Weather("20.03", 4, -1, 2, 74, 81, 0)
]

# for day in days:
#     print(f"{day.date}: днём {day.temp_day}°C, {day.temp_night}°C,  ночью, скорость ветра {day.wind_speed}м/с, влажность {day.precipitation}%, вероятность осадков {day.humidity}%, индекс ультрафиолета {day.uv}")

print("Дата    День   Ночь   Ветер  Влажн  Осадки  УльтраФ")
print("-" * 50)
for day in days:
    print(f"{day.date}  {day.temp_day:3}°C  {day.temp_night:3}°C  {day.wind_speed:2}м/с  {day.humidity:3}%   {day.precipitation:3}%    {day.uv:2}")


temp_days = np.array([day.temp_day for day in days])

print("\nСтатистика по дневной температуре:")
print(f"Средняя: {temp_days.mean()}°C")
print(f"Максимальная: {temp_days.max()}°C")
print(f"Минимальная: {temp_days.min()}°C")


temp_nights = np.array([day.temp_night for day in days])

print("\nСтатистика по ночной температуре:")
print(f"Средняя: {temp_nights.mean()}°C")
print(f"Максимальная: {temp_nights.max()}°C")
print(f"Минимальная: {temp_nights.min()}°C")


print("\nТемпература за 11-14 марта:")
first_3 = days[:3]
temp_day_3 = np.array([day.temp_day for day in first_3])
temp_night_3 = np.array([day.temp_night for day in first_3])

print(f"Средняя дневная: {temp_day_3.mean():.1f}°C")
print(f"Средняя ночная: {temp_night_3.mean():.1f}°C")
print(f"Средняя за сутки: {(temp_day_3.mean() + temp_night_3.mean()) / 2:.1f}°C")


print("\nТемпература за 11-17 марта:")

week = days[:7]
temp_day_w = np.array([day.temp_day for day in week])
temp_night_w = np.array([day.temp_night for day in week])

print(f"Средняя дневная: {temp_day_w.mean():.1f}°C")
print(f"Средняя ночная: {temp_night_w.mean():.1f}°C")
print(f"Средняя за сутки: {(temp_day_w.mean() + temp_night_w.mean()) / 2:.1f}°C")

















print([i%4 for i in range(12)])


print([i * 5 for i in "Hello"])



print([ord(i) for i in "Hello"])


import random

a = [random.randint(-10, 10) for i in range(10)]
print(a)

b = [abs(i) for i in a]
print(b)

col = 5
s = 4
a = [[0]*s for i in range(col)]
a[3][1] = 100
print(a)
for i in a:
    print(i)


a = [(i, j) for i in "abc" for j in [1, 2, 3]]
print(a)


a = [(i * j) for i in "abc" for j in [1, 2, 3]]
print(a)


a = [(i * j) for i in [1, 2, 3, 4, 5] for j in [1, 2, 3] if i*j>=10]
print(a)


matrix1 = []
for i in range(1, 4):
    row = []
    for j in range(1, 4):
        if j%2 == 1:
            row.append(j)
        else:
            row.append(0)
    matrix1.append(row)
print(matrix1)


matrix2 = [[j if j % 2 == 1 else 0 for j in range(1,4)] for i in range(1, 4)]
print(matrix2)


print([[j if j % 2 == 1 else 0 for j in range(1,4)] for i in range(1, 4)])









































&НаКлиенте
Процедура КомандаВыполнить(Команда);
    Дни = Новый Массив();
    Дни.Добавить("Понедельник"); 
    Дни.Добавить("Вторник");
    Дни.Добавить("Среда");
    
    СтрокаВывода = "";
    
    Для Каждого Элемент Из Дни Цикл
        СтрокаВывода = СтрокаВывода + " " + Элемент;
    КонецЦикла;
    
    ЭтотОбъект.ВашРезультат = СтрокаВывода;
КонецПроцедуры

&НаКлиенте
Процедура КомВыполнить2(Команда);
    МойМассив = Новый Массив(3);
    МойМассив[0] = "Понедельник";
    МойМассив.Добавить("Вторник");
    МойМассив[2] = "Среда"; 
    Сообщить(МойМассив.Количество());
    
    Счетчик = 0;
    Пока Счетчик < МойМассив.Количество() Цикл
        Сообщить(МойМассив[Счетчик]);
        Счетчик = Счетчик + 1;
    КонецЦикла;
КонецПроцедуры

&НаКлиенте
Процедура КомВыполнить3(Команда)
    МойМассив1 = Новый Массив();
    МойМассив1.Добавить(1);
    МойМассив1.Добавить(2);
    МойМассив1.Добавить(3);
    МойМассив1.Добавить(4);
    МойМассив1.Добавить(5);
    
    Счетчик = 0;
    СуммаЧисел = 0;
    Пока Счетчик < МойМассив1.Количество() Цикл
        СуммаЧисел + МойМассив1[Счетчик];
        Счетчик = Счетчик + 1;
    КонецЦикла;
    
    ЭтотОбъект.Результат2 = СуммаЧисел;
КонецПроцедуры

&НаКлиенте
Процедура МояРаботаСоСтроками(Команда)
    МояСтрока = "Привет, мир!";
    
    // эксперимент 1 - длина строки
    Длина = СтрДлина(МояСтрока);
    Сообщить("Длина строки: " + Длина);
    
    // эксперимент 2 - регистр
    Сообщить("Верхний регистр: " + ВРег(МояСтрока));
    Сообщить("Нижний регистр: " + НРег(МояСтрока));
    
    // эксперимент 3 - ищем слово
    Позиция = Найти(МояСтрока, "мир");
    Сообщить("Слово 'мир' на позиции: " + Позиция);
    
    ЭтотОбъект.РезультатСтроки = МояСтрока;
КонецПроцедуры

&НаКлиенте
Процедура ЭкспериментСДатами(Команда)
    Сегодня = ТекущаяДата();
    Сообщить("Сегодня: " + Сегодня);
    
    // прибавляем 10 дней
    Будущее = Сегодня + 10 * 24 * 60 * 60;
    Сообщить("Через 10 дней: " + Будущее);
    
    // разница в днях
    НачГода = Дата(2026, 1, 1);
    ПрошлоДней = (Сегодня - НачГода) / (24 * 60 * 60);
    Сообщить("Дней с начала года: " + ПрошлоДней);
    
    ЭтотОбъект.РезультатДата = Будущее;
КонецПроцедуры

&НаКлиенте
Процедура ПравильнаяСумма(Команда)
    Числа = Новый Массив();
    Числа.Добавить(5);
    Числа.Добавить(10);
    Числа.Добавить(15);
    Числа.Добавить(20);
    
    Сумма = 0;
    Для Каждого Число Из Числа Цикл
        Сумма = Сумма + Число;
    КонецЦикла;
    
    Сообщить("Сумма чисел: " + Сумма);
    Среднее = Сумма / Числа.Количество();
    Сообщить("Среднее: " + Среднее);
    
    ЭтотОбъект.РезультатСумма = Сумма;
КонецПроцедуры







n = 1
result_revers = ""

while n > 0:
    result_revers += str(n % 2)
    n = n // 2

result = result_revers[::-1]
print(result)



n = 15
result_revers = []
while n > 0:
    result_revers.append(n % 2)
    n = n // 2

result = result_revers[::-1]
print(result)



result = [1, 0, 1, 0]
result_revers = result[::-1]
n = 0
exponent = 0
for i in result_revers:
    if i == 1:
        n += 2 ** exponent
    exponent += 1
print(n)



result = "1010"
result_revers = result[::-1]
n = 0
exponent = 0
for i in result_revers:
    if i == "1":
        n += 2 ** exponent
    exponent += 1
print(n)
