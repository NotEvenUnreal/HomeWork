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








































import pandas as pd

# 1. СОЗДАНИЕ DATAFRAME
print("1. СОЗДАНИЕ DATAFRAME:")
df = pd.DataFrame({
    'Имя': ['Анна', 'Иван', 'Мария', 'Петр', 'Ольга'],
    'Возраст': [25, 30, 28, 35, 22],
    'Город': ['Москва', 'Питер', 'Москва', 'Казань', 'Питер'],
    'Зарплата': [50000, 70000, 60000, 80000, 45000]
})
print(df)
print("\n" + "="*50 + "\n")

# 2. ПРОСМОТР ДАННЫХ
print("2. ПРОСМОТР ДАННЫХ:")
print("head() - первые 3 строки:")
print(df.head(3))
print("\ntail() - последние 2 строки:")
print(df.tail(2))
print("\ninfo() - информация о таблице:")
print(df.info())
print("\nshape - размер таблицы (строк, колонок):")
print(df.shape)
print("\n" + "="*50 + "\n")

# 3. СТАТИСТИКА
print("3. СТАТИСТИКА:")
print("describe() - вся статистика:")
print(df.describe())
print("\nmean() - средний возраст:", df['Возраст'].mean())
print("max() - максимальный возраст:", df['Возраст'].max())
print("min() - минимальный возраст:", df['Возраст'].min())
print("std() - стандартное отклонение возраста:", df['Возраст'].std())
print("\n" + "="*50 + "\n")

# 4. ВЫБОР КОЛОНОК
print("4. ВЫБОР КОЛОНОК:")
print("df['Имя'] - одна колонка:")
print(df['Имя'])
print("\ndf[['Имя', 'Возраст']] - несколько колонок:")
print(df[['Имя', 'Возраст']])
print("\n" + "="*50 + "\n")

# 5. ФИЛЬТРАЦИЯ СТРОК
print("5. ФИЛЬТРАЦИЯ СТРОК:")
print("df[df['Возраст'] > 25] - кто старше 25:")
print(df[df['Возраст'] > 25])
print("\ndf[df['Город'] == 'Москва'] - кто из Москвы:")
print(df[df['Город'] == 'Москва'])
print("\n" + "="*50 + "\n")

# 6. СОРТИРОВКА
print("6. СОРТИРОВКА:")
print("sort_values('Возраст') - по возрастанию:")
print(df.sort_values('Возраст'))
print("\nsort_values('Возраст', ascending=False) - по убыванию:")
print(df.sort_values('Возраст', ascending=False))
print("\n" + "="*50 + "\n")

# 7. ГРУППИРОВКА
print("7. ГРУППИРОВКА:")
print("groupby('Город')['Зарплата'].mean() - средняя зарплата по городам:")
print(df.groupby('Город')['Зарплата'].mean())
print("\n" + "="*50 + "\n")

# 8. ДОБАВЛЕНИЕ КОЛОНКИ
print("8. ДОБАВЛЕНИЕ КОЛОНКИ:")
df['Налог'] = df['Зарплата'] * 0.13
print("df['Налог'] = df['Зарплата'] * 0.13 - добавили колонку с налогом:")
print(df)
print("\n" + "="*50 + "\n")

# 9. УНИКАЛЬНЫЕ ЗНАЧЕНИЯ
print("9. УНИКАЛЬНЫЕ ЗНАЧЕНИЯ:")
print("unique() - список уникальных городов:")
print(df['Город'].unique())
print("\nvalue_counts() - сколько раз встречается каждый город:")
print(df['Город'].value_counts())
print("\n" + "="*50 + "\n")

# 10. ЧТЕНИЕ/ЗАПИСЬ ФАЙЛОВ
print("10. ЧТЕНИЕ/ЗАПИСЬ ФАЙЛОВ:")
print("Сохраняем в CSV...")
df.to_csv('data.csv', index=False)
print("Читаем из CSV...")
df2 = pd.read_csv('data.csv')
print("Прочитано успешно, первые 3 строки:")
print(df2.head(3))

# df.to_excel('data.xlsx', index=False)
# df2 = pd.read_excel('data.xlsx')









&НаКлиенте
Процедура ВыполнитьЗадание(Команда)
    
    Текст = ЭтотОбъект.ВведенныйТекст;
    Слова = СтрРазделить(Текст, " ", Ложь);
    КоличествоСлов = Слова.Количество();
    
    Если КоличествоСлов < 4 ИЛИ КоличествоСлов > 8 Тогда
        Сообщить("Ошибка! Нужно 4-8 слов. Сейчас: " + КоличествоСлов);
        Возврат;
    КонецЕсли;
    
    Результат = "";
    
    Для Каждого Слово Из Слова Цикл
        ДлинаСлова = СтрДлина(Слово);
        
        Для Поз = 1 По ДлинаСлова Цикл
            Символ = Сред(Слово, Поз, 1);
            
            Если Найти("0123456789", Символ) > 0 Тогда
                Цифра = Число(Символ);
                Для Счетчик = 1 По Цифра Цикл
                    Случ = 1072 + Цел(СлучайноеЧисло(0, 32));
                    Результат = Результат + Символ(Случ);
                КонецЦикла;
            Иначе
                Результат = Результат + Строка(ДлинаСлова);
            КонецЕсли;
        КонецЦикла;
        
        Результат = Результат + " ";
    КонецЦикла;
    
    Результат = СокрЛП(Результат);
    
    Длина = СтрДлина(Результат);
    Часть = Цел(Длина / 3);
    
    Строка1 = Сред(Результат, 1, Часть);
    Строка2 = Сред(Результат, Часть + 1, Часть);
    Строка3 = Сред(Результат, Часть * 2 + 1);
    
    ЭтотОбъект.Результат1 = Строка1;
    ЭтотОбъект.Результат2 = Строка2;
    ЭтотОбъект.Результат3 = Строка3;
    
    Сообщить("1: " + Строка1);
    Сообщить("2: " + Строка2);
    Сообщить("3: " + Строка3);
    
КонецПроцедуры




























import pandas as pd
import numpy as np

#1 Создание одномероного массива
print("Создание одномероного массива")
s = pd.Series([10, 20, 30, 40, 50])
print(s)


# Создание одномероного массива с собственными индексами
print("Создание одномероного массива с собственными индексами")
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)



# Создание Series из массива NumPy:
data = np.array([10, 20, 30, 40, 50])
series = pd.Series(data)
print(series)




#2
print("Просмотр начала/конца")
print(s.head(2))  # первые 2 элемента
print(s.tail(2))  # последние 2 элемента


#3 iloc - выбор по позиции
s_ind = pd.Series([10, 25, 15, 30, 20], index=['a', 'b', 'c', 'd', 'e'])
print("Исходный Series с индексами a,b,c,d,e:")
print(s_ind)
print(f"\niloc[2] (элемент на позиции 2): {s_ind.iloc[2]}")
print("iloc[[0, 2]] (элементы на позициях 0 и 2):")
print(s_ind.iloc[[0, 2]])




#4 isin - проверка вхождения
print("\nisin([15, 30]) - проверка вхождения в список:")
print(s_ind.isin([15, 30]))
print("Выбор элементов, которые есть в списке [15, 30]:")
print(s_ind[s_ind.isin([15, 30])])




#5 loc - выбор по метке
print(f"\nloc['c'] (элемент с меткой 'c'): {s_ind.loc['c']}")
print("loc['b':'d'] (элементы с метками от 'b' до 'd'):")
print(s_ind.loc['b':'d'])




#6 MultiIndex.from_tuples
print("Создание мультииндекса из кортежей:")
tuples = [('a', 1), ('a', 2), ('b', 1), ('b', 2)]
index = pd.MultiIndex.from_tuples(tuples)
s_multi = pd.Series([10, 20, 30, 40], index=index)
print(s_multi)




#7 MultiIndex.from_product
print("\nСоздание мультииндекса из всех комбинаций:")
index = pd.MultiIndex.from_product([['a','b'], [1,2]])
s_multi2 = pd.Series([100, 200, 300, 400], index=index)
print(s_multi2)




#8 describe - описательная статистика
print("\ndescribe() - описательная статистика:")
s_stat = pd.Series([15, 25, 10, 30, 20, 25, 15])
print(s_stat.describe())
print("describe(percentiles=[0.1, 0.9]) - с дополнительными процентилями:")
print(s_stat.describe(percentiles=[0.1, 0.9]))


#9 count - количество не-NaN элементов
print(f"\ncount() - количество не-NaN элементов: {s_stat.count()}")


#10 argsort - индексы для сортировки
print(f"\nargsort() - индексы, которые отсортируют значения:")
print(f"Исходные значения: {s_stat.values}")
print(f"argsort(): {s_stat.argsort().values}")


# argmin - позиция минимума
print(f"\nargmin() - позиция минимума: {s_stat.argmin()}, значение: {s_stat.min()}")


# argmax - позиция максимума
print(f"argmax() - позиция максимума: {s_stat.argmax()}, значение: {s_stat.max()}")





#11 astype - преобразование типа данных
print("\nastype - преобразование типа данных:")
s_astype = pd.Series([1, 2, 3, 4, 5])
print("Исходный (int):")
print(s_astype)
print("\nastype(float):")
print(s_astype.astype(float))
print("\nastype(str):")
print(s_astype.astype(str))
print("\nastype('category'):")
print(s_astype.astype('category'))


#12 value_counts - подсчет уникальных значений
print("\nvalue_counts() - подсчет уникальных значений:")
s_counts = pd.Series(['a', 'b', 'a', 'c', 'b', 'b'])
print(s_counts.value_counts())


































import pandas as pd

url = "https://docs.google.com/spreadsheets/d/1WWCqNemEJTfqPaMPR2rF3qoLzdilovemsrAuvLJNv-A/export?format=csv" #ссылка Гугл таблицу
df = pd.read_csv(url) #создание переменной для ссылки
print(df) #вывод всей таблицы
subjects =['subject1', 'subject2', 'subject3', 'subject4', 'subject5'] #создаём переменную для удобного вывода средних баллов по  5 предметам
print(df[['subject1', 'subject2', 'subject3', 'subject4', 'subject5']].mean()) #не удобно
print(df[subjects].mean()) #удобно
print(df[subjects].mean().mean()) #средний балл по всем предметам
no_triples = df[(df['subject1'] >= 4) &     #фильтр по предметам > 4
                (df['subject2'] >= 4) &
                (df['subject3'] >= 4) &
                (df['subject4'] >= 4) &
                (df['subject5'] >= 4)]

print(no_triples[['student','subject1', 'subject2', 'subject3', 'subject4', 'subject5']]) #ввывод имена студентов без троек и его оценки
without_stipend =  df[df['stipend'] == 0] #фильтр стипендия = 0
print(without_stipend[['student']]) #вывод студентов без стипендии
nonresidents = df[df['city'] != 'Шумерля'] #иногородние
for idx, row in nonresidents.iterrows():
    fives = [] #лист для пятёрок
    if row['subject1'] == 5: fives.append('subject1')
    if row['subject2'] == 5: fives.append('subject2')
    if row['subject3'] == 5: fives.append('subject3')
    if row['subject4'] == 5: fives.append('subject4')
    if row['subject5'] == 5: fives.append('subject5')

    if fives:  #только если есть хотя бы одна пятёрка
        print(f"{row['student']}, {row['city']}: {', '.join(fives)}") #вывод иногороних хотя бы с 1 пятёркой

local_resident = df[df['city'] != 'Шумерля'] #шумерлинские
df['avg'] = df[subjects].mean(axis=1) #средний балл студента
print(df[(df['city'] == 'Шумерля') & (df['avg'] >= 4.5)]) #вывод шумерлинских с  avg >= 4.5




#группируем по возрасту и считаем средний балл
age_avg = df.groupby('age')['avg'].mean().round(2)
for age, avg in age_avg.items():
    print(f"Возраст {age} лет: средний балл {avg}") #вывод корреляции возраста и успеваемости

for subject in subjects:
    best = df[df[subject] == df[subject].max()]['student'].tolist() #создание переменной, где сравниваем средний балл каждого студента с максимумом и превращаем в список
    print(f"{subject}: {', '.join(best)} ({df[subject].max()})") #вывод топов


city_stats = df.groupby('city')['avg'].agg(['mean', 'count']).round(2).sort_values('mean', ascending=False)
print("Топ-3 города по успеваемости:")
for i, (city, row) in enumerate(city_stats.head(3).iterrows(), 1):
    print(f"{i}. {city}: {row['mean']} (студентов: {row['count']})") #вывод топ-3 города

# groupby()	Группирует данные по значениям
# agg()	Применяет функции к группам (mean, sum, count)
# round(2)	Округляет числа до 2ух знаков после точки
# sort_values(ascending=False)	Сортирует по колонке от большего к меньшему
# head()	Берёт первые N строк
# iterrows()	Проходит по строкам по одной
# enumerate()	Нумерует итерации

print(df.columns.tolist())



































































rus_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" #33
rus_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" #33
eng_lower = "abcdefghijklmnopqrstuvwxyz" #26
eng_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #26
digits = "0123456789"   #10
symbols = " .,!?-:;'()[]{}@#$%^&*+=" #24
alfabet = rus_lower + rus_upper + eng_lower + eng_upper + digits + symbols #152
full_code = ""

text = input("Что закодировать:")

for character in text: #цикл по каждому символу текста
    num = alfabet.find(character) #находим номер буквы в алфавите
    if num == -1:
        print(f"Символ '{character}' не найден в алфавите")
        continue
    binary = "" #стирается после, того как зашифруется 1 символ
    for i in range(7, -1, -1):  # i = 7,6,5,4,3,2,1,0 #идём от старшего к младшему разряду
        if num >= 2**i: #помещается ли число в этот бит?
            binary += "1"
            num -= 2**i #убираем использованную степень
        else:
            binary += "0"
    full_code += binary
    print(f"{character} -> {binary}")
print(full_code)



https://docs.google.com/spreadsheets/d/e/2PACX-1vQ_pPA7cWecnsx8iWl3fOWGfLH_sJfVFlkS9auYYKx9Ue57q052TH6rPnCKTbnS1vGc6lt7BnjrePGV/pub?output=xlsx







#Функция перевода числа в троичную систему
def troichnoe(n):
    res = "" #строка для результата
    while n > 0:
        res = str(n % 3) + res #остаток (0,1,2) → строка → добавляем В НАЧАЛО
        n //= 3 #делим на 3 (целочисленно)
    return res or "0" #если n было 0, вернуть "0", иначе вернуть res


#Функция перевода троичной строки в десятичное число
def to_dec(s):
    return int(s, 3) # int("12", 3) = 5


#Основной алгоритм по задаче
def R(N):
    tr = troichnoe(N) #шаг 1: N → троичная строка

    if N % 3 != 0: #шаг 2: если N НЕ кратно 3
        ost = N % 3 #остаток от деления (1 или 2)
        add = ost * 5 #остаток умножаем на 5
        tr += troichnoe(add) #дописываем в конец троичную запись add

    return to_dec(tr) #шаг 3: троичная строка → десятичное число


# Ввод и вывод
N = int(input("N = ")) #пользователь вводит число
print("R =", R(N)) #выводим результат
