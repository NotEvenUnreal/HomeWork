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



# Поиск минимального N
N = 1
while True:
    if R(N) >= 146:
        print(f"Минимальное N = {N}, R = {R(N)}")
        break
    N += 1


# Ввод и вывод
N = int(input("N = ")) #пользователь вводит число
print("R =", R(N)) #выводим результат

























import matplotlib.pyplot as plt
import numpy as np

#Данные
x = np.linspace(-2 * np.pi, 2 * np.pi, 500) #массив x от -2π до 2π, 500 точек
y_sin = np.sin(x) #синус для каждого x
y_cos = np.cos(x) #косинус для каждого x
y_asin = np.arcsin(np.clip(x, -1, 1)) #арксинус (x ограничен [-1,1])
rect_x = [-1, 1, 1, -1, -1] #координаты x для прямоугольника
rect_y = [-0.5, -0.5, 0.5, 0.5, -0.5] #координаты y для прямоугольника

#Настройка графика
plt.figure(figsize=(10, 6)) #размер окна 10x6 дюймов
ax = plt.gca() #берём текущие оси

#Переносим оси в центр
ax.spines['left'].set_position('center') #ось y в центр
ax.spines['bottom'].set_position('center') #ось x в центр
ax.spines['right'].set_color('none') #скрываем правую ось
ax.spines['top'].set_color('none') #скрываем верхнюю ось

#Графики
plt.plot(x, y_sin, label='sin(x)', linewidth=2) #синус сплошной линией
plt.plot(x, y_cos, label='cos(x)', linewidth=2) #косинус сплошной линией
plt.plot(np.clip(x, -1, 1), y_asin, label='arcsin(x)', linewidth=2, linestyle='--') #арксинус пунктиром
plt.plot(rect_x, rect_y, label='Прямоугольник', linewidth=2, color='green') #прямоугольник зелёный

#Оформление
plt.xlim(-2.5, 2.5) #границы x от -2.5 до 2.5
plt.ylim(-1.5, 1.5) #границы y от -1.5 до 1.5
plt.title('Синус, косинус, арксинус и прямоугольник') #заголовок
plt.legend() #показываем легенду
plt.grid(True) #включаем сетку

plt.show() #показываем график






























import matplotlib.pyplot as plt
import numpy as np

agrad = 30 #угол атаки в градусах
arad = np.radians(agrad) #перевод угла атаки в радианы
g = 9.81 #постоянная приятяжения Земли
v0km = 20 #км/ч
v0 = v0km * 1000 / 3600 #перевод в м/с
nachalo = 0

l = (v0**2 * np.sin(2 * arad)) / g #дальность полёта
t = (2 * v0 * np.sin(arad)) / g #время полёта

x = np.linspace(nachalo, l, 100) #горизонтальные координаты
y = x * np.tan(arad) - (g * x**2) / (2 * v0**2 * np.cos(arad)**2) #высота в каждой точке x

plt.figure(figsize=(8, 4.5))
ax = plt.gca()

plt.plot(x, y, label='Полёт камня', linewidth=4)

#автоматические границы по данным
plt.xlim(0, l + 0.5)
plt.ylim(0, max(y) + 0.2)

plt.legend()
plt.grid(True)
plt.xlabel('x (м)')
plt.ylabel('y (м)')
plt.title('Траектория полёта камня')

#     .2f - округление до 2 знаков после запятой
print(f"Время полёта: {t:.2f} с")
print(f"Максимальная высота: {max(y):.2f} м")
print(f"Место Запуска: x = {0} м, y = {0} м")
print(f"Место Приземления: x = {l:.2f} м, y = {0} м")

plt.show()
























# Входные данные:
# Одномерный массив целых чисел от 1 до 10 включительно:
# Выходные данные (что программа должна вывести):
# Сумму всех элементов массива
# Среднее арифметическое
# Максимальный элемент
# Минимальный элемент
# Массив, где каждый элемент умножен на 2
# Массив, состоящий только из элементов, которые больше 5
# Массив, состоящий только из элементов, которые меньше 5
# Количество элементов, равных 5
# Требования к реализации:
# Использовать библиотеку NumPy
# Запрещено использовать циклы for и while
# Вывод должен быть оформлен в виде понятных сообщений



import numpy as np


arr = np.arange(1, 11)

print("Исходный массив:", arr)
print("Сумма:", np.sum(arr))
print("Среднее:", np.mean(arr))
print("Максимум:", np.max(arr))
print("Минимум:", np.min(arr))
print("Умножение на 2:", arr * 2)
print("Элементы > 5:", arr[arr > 5])
print("Элементы < 5:", arr[arr < 5])
print('Количество элементов равное 5:', np.count_nonzero(arr == 5))























# import datetime
# import pandas as pd
# df = pd.DataFrame({ #кредитованные клиенты
#     "id": ["1", "2", "3"],
#     "target": ["Потребительский", "Автокредит", "Бизнес-кредит"],
#     "loan": [20000, 5000000, 20000000], #выдача кредита
#     "repayment": [0,0,0], #полученные с учётом процентов
#     "days": [365, 365, 365], #срок кредита
#     "rate": [0.26, 0.2, 0.18], #кредитная ставка
#     "frequency": [30, 30, 30], #регулярность погашения
# })
#
# bank_own_funds = -5000000000 #собственные средства
# reserve = 0.1 #резервная ставка
#
# cb = { #обязательсва перед ЦБ
#     "id": ["1"],
#     "loan": 25020000, #полученные средства
#     "repayment": 0, #выдача с учётом процентов
#     "days": 365, #срок кредита
#     "rate": 0.15, #кредитная ставка
#     "frequency": 30 #регулярность погашения
# }
# total_loans = df["loan"].sum() #выданные средства банком
# total_money = (cb["loan"] + bank_own_funds) #доступные банку средства
# max_days = max(df["days"].max(), cb["days"]) #используем кредит с максимальным количеством дней для цикла
# print(max_days)
#
# for i in range(1, max_days+1):
#     total_money -= total_loans
#     df.loc[df["loan"]] !!!!!!!!!!!!!!!!!!!!!!!!
#     if total_money > (cb["loan"] + bank_own_funds) * (1 - reserve): #проверка на банкротство
#         print("Ошибка: банк оформил больше кредитных средств, чем ему позволяет резерв!")
#     if total_money < 0:
#         print("!!!КРИТИЧЕСКАЯ СИТАЦИЯ!!!: БАНК ПОД УГРОЗОЙ БАНКРОТСВА!")
#         break
# print(total_money)




































import matplotlib.pyplot as plt
count = 1
for i in range(4):
    #данные для синусоиды
    x = np.linspace(0, count * np.pi, 50) #50 точек для периодов от 0.5 до 2
    y = np.sin(x)
    plt.bar(x, y, width= count*0.1, color='skyblue', edgecolor='black')

    #настройка поля матплотлиб
    plt.title('Гистограмма синусоидальной формы')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.grid(True, alpha=0.3)
    plt.show()
    count += 1




import matplotlib.pyplot as plt
#данные: минуты и объёмы (тысячи акций)
minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
volumes = [128.55, -38.87, 22.99, -38.18, 50.00, -71.53, 29.68, 48.12, -75.17, -290.47]

#зелёный если объём положительный, красный если отрицательный
colors = ['green' if v > 0 else 'red' for v in volumes]

plt.bar(minutes, volumes, color=colors, edgecolor='black', alpha=0.7)

#настройка поля матплотлиб
plt.title('NVDA объём торгов')
plt.xlabel('Минута')
plt.ylabel('Изменение объёма (k)')
plt.grid(axis='y', alpha=0.3)
plt.axhline(y=0, color='black', linewidth=0.8)  # нулевая линия
plt.show()




















import matplotlib.pyplot as plt

labels = ['Чувашия', 'Марий Эл', 'Татарстан', 'Нижегородская обл.', 'Ульяновская обл.', 'Мордовия']
sizes = [11.4, 6.5, 38.6, 29.9, 11.6, 7.5] #проценты
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'orange', 'pink']
explode = (0.1, 0, 0, 0, 0, 0) #вырезать Чувашию

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=135)
plt.title('Население Чувашии и соседних регионов (в процентах)')

plt.show()


















































import urllib.request
import json
from rich.table import Table
from rich.console import Console

#1 загружаем JSON по ссылке
url = "https://jsonplaceholder.typicode.com/users"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

console = Console()

#таблица 1 Контакты
table1 = Table(title="Контакты", show_lines=True)
table1.add_column("id")
table1.add_column("name")
table1.add_column("username")
table1.add_column("email")
table1.add_column("phone")

for user in data:
    table1.add_row(
        str(user["id"]),
        user["name"],
        user["username"],
        user["email"],
        user["phone"]
    )

console.print(table1)

#таблица 2 Адреса
table2 = Table(title="Адреса", show_lines=True)
table2.add_column("id")
table2.add_column("street")
table2.add_column("suite")
table2.add_column("city")
table2.add_column("zipcode")

for user in data:
    address = user["address"]
    table2.add_row(
        str(user["id"]),
        address["street"],
        address["suite"],
        address["city"],
        address["zipcode"]
    )

console.print(table2)

#таблица 3 Компании
table3 = Table(title="Компании", show_lines=True)
table3.add_column("id")
table3.add_column("company_name")
table3.add_column("catchPhrase")
table3.add_column("bs")

for user in data:
    company = user["company"]
    table3.add_row(
        str(user["id"]),
        company["name"],
        company["catchPhrase"],
        company["bs"]
    )

console.print(table3)

























from functools import lru_cache

# Проблема: Функция вызывается много раз с одними и теми же аргументами, но каждый раз заново считает результат
#
# Решение: lru_cache запоминает результат и при повторном вызове просто возвращает его мгновенно

@lru_cache
def square(x):
    print(f"Считаю {x}...")
    return x * x

print(square(3))  # Считает 3... → 9
print(square(3))  # → 9 (не передаёт (x) в square(x), потому что результат уже запомнен)






from functools import reduce

# Проблема: Нужно применить функцию к парам элементов, накапливая результат (например, перемножить все числа).
#
# Решение: reduce делает это в одну строку.

numbers = [2, 3, 4]
# 2*3=6, 6*4=24
result = reduce(lambda x, y: x * y, numbers)
print(f"Перемножение {numbers} = {result}")  # 24






from functools import partial

# Проблема: У тебя есть функция с 2 параметрами. Ты постоянно передаёшь второй одинаковый
#
# Решение: partial «замораживает» часть параметров, создавая новую функцию с меньшим количеством аргументов

def show_city(city, country):
    print(f"{city} — город в {country}")

# Создаём новую функцию, где country уже = "Россия"
show_russian_city = partial(show_city, country="Россия")

show_russian_city("Москва")     # Москва — город в Россия
show_russian_city("Казань")     # Казань — город в Россия
show_russian_city("Волгоград")  # Волгоград — город в Россия













from functools import singledispatch

# Проблема: Хочется иметь одну функцию, которая по‑разному обрабатывает целые числа, строки, списки, но без кучи if type(x) == ....
#
# Решение: singledispatch позволяет перегружать функцию для разных типов.

@singledispatch
def process(arg):
    print(f"Базовый тип: {type(arg)}")

@process.register(int)
def _(arg):
    print(f"Целое число: {arg}")

@process.register(list)
def _(arg):
    print(f"Список длины {len(arg)}")

process(42)        # Целое число: 42
process([1,2,3])   # Список длины 3
process("hello")   # Базовый тип: <class 'str'>


















import asyncio
import websockets

# Множество для хранения всех подключённых клиентов
connected_clients = set()

async def handler(websocket):
    # Добавляем нового клиента
    connected_clients.add(websocket)
    try:
        # Ждём сообщения от клиента
        async for message in websocket:
            print(f"Получено: {message}")
            # Отправляем сообщение всем остальным клиентам
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    finally:
        # Клиент отключился — удаляем его
        connected_clients.remove(websocket)

async def main():
    # Запускаем сервер на localhost, порт 9999
    async with websockets.serve(handler, "localhost", 9999):
        print("WebSocket сервер запущен на ws://localhost:9999")
        await asyncio.Future()  # Бесконечно работаем

if __name__ == "__main__":
    asyncio.run(main())





























import asyncio
import websockets
import sys

async def receive_messages(websocket):
    """Принимает сообщения от сервера и выводит их"""
    try:
        async for message in websocket:
            print(f"\n[Сообщение]: {message}")
            print("Вы: ", end="", flush=True)
    except websockets.exceptions.ConnectionClosed:
        print("\nСоединение закрыто")

async def send_messages(websocket):
    """Читает ввод пользователя и отправляет сообщения"""
    while True:
        message = await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)
        if message.strip():
            await websocket.send(message.strip())

async def main():
    uri = "ws://localhost:9999"
    try:
        async with websockets.connect(uri) as websocket:
            print("Подключено к чату. Введите сообщение:")
            # Запускаем приём и отправку параллельно
            await asyncio.gather(
                receive_messages(websocket),
                send_messages(websocket)
            )
    except ConnectionRefusedError:
        print("Сервер не запущен. Запусти сначала server.py")

if __name__ == "__main__":
    asyncio.run(main())




































































import random
import string


class PasswordGenerator:
    """Генератор случайных паролей"""

    def __init__(self, length=8):
        self.length = length
        self.history = []

    def generate(self, use_digits=True, use_punctuation=False):
        chars = string.ascii_letters
        if use_digits:
            chars += string.digits
        if use_punctuation:
            chars += string.punctuation

        # Генерируем пароль: случайно выбираем символ из набора chars,
        # повторяем это self.length раз, затем склеиваем все символы в строку
        password = ''.join(random.choice(chars) for _ in range(self.length))
        self.history.append(password)
        return password

    def show_history(self):
        if not self.history:
            print("Пароли пока не генерировались")
            return
        print(f"История паролей (длина {self.length}):")
        for i, pwd in enumerate(self.history, 1):
            print(f"{i}. {pwd}")




# Генератор с паролями по умолчанию (8 символов)
gen_default = PasswordGenerator()  # length=8 по умолчанию

# Генератор с длинными паролями (32 символа)
gen_long = PasswordGenerator(length=32)

# Генерируем 2 пароля для каждого
p1 = gen_default.generate(use_digits=True)               # 8 символов, буквы+цифры
p2 = gen_default.generate(use_punctuation=True)          # 8 символов, буквы+цифры+символы

p3 = gen_long.generate(use_digits=True)                  # 32 символа, буквы+цифры
p4 = gen_long.generate(use_punctuation=True)             # 32 символа, буквы+цифры+символы

print("Новые пароли:")
print(p1)
print(p2)
print(p3)
print(p4)


gen_default.show_history()


gen_long.show_history()












































































# class Magic:
#     """Класс для демонстрации всех магических методов"""
#
#     # ==================== ОСНОВНЫЕ МЕТОДЫ ====================
#
#     def __init__(self, name, data=None):
#         """
#         __init__ - конструктор
#         Вызывается при создании объекта: объект = Класс()
#         """
#         print("1. __init__: создание объекта")
#         self.name = name
#         self.data = data if data is not None else []
#         self.value = 42
#         self._private_attr = "скрыто"
#
#     def __str__(self):
#         """
#         __str__ - строковое представление для пользователей
#         Вызывается при: print(объект), str(объект)
#         Должен возвращать строку
#         """
#         print("2. __str__: вызван print()")
#         return f"Magic: {self.name}, данные: {self.data}"
#
#     def __repr__(self):
#         """
#         __repr__ - строковое представление для разработчиков
#         Вызывается при: repr(объект), в интерактивной консоли
#         Должен возвращать строку, по которой можно восстановить объект
#         """
#         print("3. __repr__: вызван repr()")
#         return f"Magic('{self.name}', {self.data})"
#
#     def __len__(self):
#         """
#         __len__ - длина объекта
#         Вызывается при: len(объект)
#         Должен возвращать целое число
#         """
#         print("4. __len__: вызван len()")
#         return len(self.data)
#
#     # ==================== ДОСТУП ПО ИНДЕКСУ ====================
#
#     def __getitem__(self, key):
#         """
#         __getitem__ - доступ по индексу или ключу
#         Вызывается при: объект[индекс]
#         """
#         print(f"5. __getitem__: обращение к индексу {key}")
#         return self.data[key]
#
#     def __setitem__(self, key, value):
#         """
#         __setitem__ - установка значения по индексу
#         Вызывается при: объект[индекс] = значение
#         """
#         print(f"6. __setitem__: установка {key} = {value}")
#         self.data[key] = value
#
#     def __delitem__(self, key):
#         """
#         __delitem__ - удаление по индексу
#         Вызывается при: del объект[индекс]
#         """
#         print(f"7. __delitem__: удаление индекса {key}")
#         del self.data[key]
#
#     def __contains__(self, item):
#         """
#         __contains__ - проверка наличия элемента
#         Вызывается при: элемент in объект
#         Должен возвращать True/False
#         """
#         print(f"8. __contains__: проверка {item} in объект")
#         return item in self.data
#
#     # ==================== МАТЕМАТИЧЕСКИЕ ОПЕРАЦИИ ====================
#
#     def __add__(self, other):
#         """
#         __add__ - сложение объектов
#         Вызывается при: объект1 + объект2
#         Должен возвращать новый объект
#         """
#         print("9. __add__: сложение объектов")
#         new = Magic(f"{self.name}+{other.name}")
#         new.data = self.data + other.data
#         return new
#
#     def __sub__(self, other):
#         """
#         __sub__ - вычитание объектов
#         Вызывается при: объект1 - объект2
#         """
#         print("10. __sub__: вычитание объектов")
#         result = []
#         for x in self.data:
#             if x not in other.data:
#                 result.append(x)
#         new = Magic(f"{self.name}-{other.name}", result)
#         return new
#
#     def __mul__(self, number):
#         """
#         __mul__ - умножение объекта на число
#         Вызывается при: объект * число
#         """
#         print(f"11. __mul__: умножение на {number}")
#         return Magic(f"{self.name}*{number}", self.data * number)
#
#     def __truediv__(self, number):
#         """
#         __truediv__ - деление объекта на число
#         Вызывается при: объект / число
#         """
#         print(f"12. __truediv__: деление на {number}")
#         part = len(self.data) // number
#         return Magic(f"{self.name}/{number}", self.data[:part])
#
#     # ==================== ОПЕРАЦИИ СРАВНЕНИЯ ====================
#
#     def __eq__(self, other):
#         """
#         __eq__ - равенство
#         Вызывается при: объект1 == объект2
#         """
#         print("13. __eq__: сравнение ==")
#         return self.data == other.data
#
#     def __lt__(self, other):
#         """
#         __lt__ - меньше
#         Вызывается при: объект1 < объект2
#         """
#         print("14. __lt__: сравнение <")
#         return len(self.data) < len(other.data)
#
#     def __le__(self, other):
#         """
#         __le__ - меньше или равно
#         Вызывается при: объект1 <= объект2
#         """
#         print("15. __le__: сравнение <=")
#         return len(self.data) <= len(other.data)
#
#     def __gt__(self, other):
#         """
#         __gt__ - больше
#         Вызывается при: объект1 > объект2
#         """
#         print("16. __gt__: сравнение >")
#         return len(self.data) > len(other.data)
#
#     def __ge__(self, other):
#         """
#         __ge__ - больше или равно
#         Вызывается при: объект1 >= объект2
#         """
#         print("17. __ge__: сравнение >=")
#         return len(self.data) >= len(other.data)
#
#     # ==================== ВЫЗОВ КАК ФУНКЦИИ ====================
#
#     def __call__(self, coefficient=2):
#         """
#         __call__ - объект ведёт себя как функция
#         Вызывается при: объект(аргументы)
#         """
#         print(f"18. __call__: объект как функция, коэффициент={coefficient}")
#         return [x * coefficient for x in self.data]
#
#     # ==================== РАБОТА С АТРИБУТАМИ ====================
#
#     def __getattr__(self, name):
#         """
#         __getattr__ - при обращении к несуществующему атрибуту
#         Вызывается когда атрибут не найден обычным способом
#         """
#         print(f"19. __getattr__: атрибут '{name}' не найден")
#         return "значение_по_умолчанию"
#
#     def __setattr__(self, name, value):
#         """
#         __setattr__ - при установке ЛЮБОГО атрибута
#         Вызывается при: объект.атрибут = значение
#         """
#         print(f"20. __setattr__: установка {name} = {value}")
#         super().__setattr__(name, value)
#
#     def __delattr__(self, name):
#         """
#         __delattr__ - при удалении атрибута
#         Вызывается при: del объект.атрибут
#         """
#         print(f"21. __delattr__: удаление атрибута {name}")
#         super().__delattr__(name)
#
#     # ==================== ИТЕРАЦИЯ ====================
#
#     def __iter__(self):
#         """
#         __iter__ - возвращает итератор
#         Вызывается при: for x in объект
#         """
#         print("22. __iter__: начало итерации")
#         self._index = 0
#         return self
#
#     def __next__(self):
#         """
#         __next__ - следующий элемент при итерации
#         Вызывается на каждом шаге цикла for
#         Должен выбрасывать StopIteration когда элементы кончились
#         """
#         if self._index < len(self.data):
#             result = self.data[self._index]
#             self._index += 1
#             print(f"23. __next__: следующий элемент {result}")
#             return result
#         raise StopIteration
#
#     # ==================== КОНТЕКСТНЫЙ МЕНЕДЖЕР ====================
#
#     def __enter__(self):
#         """
#         __enter__ - при входе в контекстный менеджер
#         Вызывается при: with объект as переменная:
#         """
#         print("24. __enter__: вход в контекстный менеджер")
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         """
#         __exit__ - при выходе из контекстного менеджера
#         Вызывается после блока with (даже если была ошибка)
#         """
#         print("25. __exit__: выход из контекстного менеджера")
#
#     # ==================== ХЕШИРОВАНИЕ И ЛОГИКА ====================
#
#     def __hash__(self):
#         """
#         __hash__ - хеш объекта (нужен чтобы использовать объект как ключ словаря)
#         Вызывается при: dict[объект] или set(объект)
#         """
#         print("26. __hash__: вычисление хеша")
#         return hash(tuple(self.data))
#
#     def __bool__(self):
#         """
#         __bool__ - проверка объекта в логическом контексте
#         Вызывается при: if объект, bool(объект)
#         Должен возвращать True/False
#         """
#         print("27. __bool__: проверка в логическом контексте")
#         return len(self.data) > 0
#
#     # ==================== УНАРНЫЕ ОПЕРАЦИИ ====================
#
#     def __neg__(self):
#         """
#         __neg__ - унарный минус
#         Вызывается при: -объект
#         """
#         print("28. __neg__: унарный минус")
#         return Magic(f"-{self.name}", [-x for x in self.data if isinstance(x, (int, float))])
#
#     def __abs__(self):
#         """
#         __abs__ - абсолютное значение
#         Вызывается при: abs(объект)
#         """
#         print("29. __abs__: абсолютное значение")
#         return Magic(f"abs({self.name})", [abs(x) for x in self.data if isinstance(x, (int, float))])
#
#     def __invert__(self):
#         """
#         __invert__ - побитовое НЕ (~)
#         Вызывается при: ~объект
#         """
#         print("30. __invert__: побитовое НЕ")
#         return Magic(f"~{self.name}", [~x for x in self.data if isinstance(x, int)])
#
#
# # ==================== КОМПАКТНАЯ ДЕМОНСТРАЦИЯ ====================
#
# if __name__ == "__main__":
#     # Создание объектов
#     m1 = Magic("A", [1, 2, 3, 4, 5])
#     m2 = Magic("B", [3, 4, 5, 6, 7])
#     m3 = Magic("C", [])
#
#     # Группа 1: строки и длина
#     print(f"\n>>> {m1}")  # __str__
#     print(f">>> {repr(m1)}")  # __repr__
#     print(f">>> len = {len(m1)}")  # __len__
#
#     # Группа 2: доступ по индексу
#     print(f">>> m1[2] = {m1[2]}")  # __getitem__
#     m1[2] = 99  # __setitem__
#     print(f">>> after set: {m1.data}")
#     del m1[2]  # __delitem__
#     print(f">>> after del: {m1.data}")
#     print(f">>> 4 in m1? {4 in m1}")  # __contains__
#
#     # Группа 3: математика
#     print(f">>> m1 + m2 = {m1 + m2}")  # __add__
#     print(f">>> m1 - m2 = {m1 - m2}")  # __sub__
#     print(f">>> m1 * 2 = {m1 * 2}")  # __mul__
#     print(f">>> m1 / 2 = {m1 / 2}")  # __truediv__
#
#     # Группа 4: сравнения
#     print(f">>> m1 == m2? {m1 == m2}")  # __eq__
#     print(f">>> m1 < m2? {m1 < m2}")  # __lt__
#     print(f">>> m1 > m2? {m1 > m2}")  # __gt__
#
#     # Группа 5: вызов как функция
#     print(f">>> m1(3) = {m1(3)}")  # __call__
#
#     # Группа 6: атрибуты
#     print(f">>> missing attr: {m1.xyz}")  # __getattr__
#     m1.new = "hello"  # __setattr__
#     del m1.new  # __delattr__
#
#     # Группа 7: итерация
#     print(">>> iteration:", end=" ")
#     for x in m1:  # __iter__ + __next__
#         print(x, end=" ")
#     print()
#
#     # Группа 8: контекстный менеджер
#     with Magic("ctx", [1, 2]) as ctx:  # __enter__ + __exit__
#         print(f">>> in context: {ctx}")
#
#     # Группа 9: хеш и логика
#     d = {m1: "value"}  # __hash__
#     print(f">>> dict key: {d[m1]}")
#     print(f">>> bool(m1): {bool(m1)}")  # __bool__
#     print(f">>> bool(m3): {bool(m3)}")  # __bool__
#
#     # Группа 10: унарные операции
#     m4 = Magic("nums", [1, -2, 3, -4, 5])
#     print(f">>> -m4 = {-m4}")  # __neg__
#     print(f">>> abs(m4) = {abs(m4)}")  # __abs__
#
#     m5 = Magic("ints", [1, 2, 3, 4])
#     print(f">>> ~m5 = {~m5}")  # __invert__









import numpy as np

# ===== 1-6: СОЗДАНИЕ МАССИВОВ =====
arr1 = np.array([1, 2, 3])                     # 1. Из списка
arr2 = np.zeros((2, 3))                        # 2. Нули
arr3 = np.ones((2, 3))                         # 3. Единицы
arr4 = np.full((2, 3), 7)                      # 4. Заполнить значением
arr5 = np.eye(3)                               # 5. Единичная матрица
arr6 = np.arange(0, 10, 2)                     # 6. Диапазон [0 2 4 6 8] - 5 элементов

# ===== 7-12: ФОРМА И ПРЕОБРАЗОВАНИЯ =====
arr7 = arr6.reshape(5, 1)                      # 7. Изменить форму (5 строк, 1 столбец) ✅
arr8 = np.resize(arr6, (3, 2))                 # 8. Изменить размер (3x2=6 элементов, дополняет)
arr9 = arr5.flatten()                          # 9. В плоский массив (копия)
arr10 = arr5.ravel()                           # 10. В плоский (view)
arr11 = arr5.transpose()                       # 11. Транспонирование
arr12 = np.concatenate([arr6, arr6])           # 12. Объединить массивы

# ===== 13-18: СТАТИСТИКА =====
data = np.array([1, 2, 3, 4, 5, 6])
mean = np.mean(data)                           # 13. Среднее
median = np.median(data)                       # 14. Медиана
std = np.std(data)                             # 15. Стандартное отклонение
var = np.var(data)                             # 16. Дисперсия
min_val = np.min(data)                         # 17. Минимум
max_val = np.max(data)                         # 18. Максимум

# ===== 19-24: ОПЕРАЦИИ С МАССИВАМИ =====
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
sum_arr = np.add(a, b)                         # 19. Сложение
prod_arr = np.multiply(a, b)                   # 20. Умножение
dot_prod = np.dot(a, b)                        # 21. Скалярное произведение
sqrt_arr = np.sqrt(a)                          # 22. Квадратный корень
exp_arr = np.exp(a)                            # 23. Экспонента
log_arr = np.log(a)                            # 24. Натуральный логарифм

# ===== 25-30: ИНДЕКСАЦИЯ, СОРТИРОВКА, УНИКАЛЬНОСТЬ =====
arr = np.array([[1, 2, 3], [4, 5, 6]])
idx = np.where(arr > 3)                        # 25. Индексы элементов >3
sorted_arr = np.sort(arr)                      # 26. Сортировка
unique_vals = np.unique([1, 2, 2, 3, 3, 3])   # 27. Уникальные значения
sum_axis = np.sum(arr, axis=0)                 # 28. Сумма по оси (столбцы)
cumsum_arr = np.cumsum([1, 2, 3])              # 29. Кумулятивная сумма [1,3,6]
clip_arr = np.clip([1, 5, 10, 15], 3, 12)      # 30. Ограничить значения [3,5,10,12]

# Вывод примеров
print("=" * 50)
print("30 МЕТОДОВ NUMPY")
print("=" * 50)

print("\n[1] np.array() →", arr1)
print("[2] np.zeros() →", arr2.shape, "\n", arr2)
print("[3] np.ones() →", arr3.shape, "\n", arr3)
print("[4] np.full() →", arr4.shape, "\n", arr4)
print("[5] np.eye() →\n", arr5)
print("[6] np.arange() →", arr6)

print("\n[7] reshape() →\n", arr7)
print("[8] resize() →\n", arr8)
print("[9] flatten() →", arr9)
print("[10] ravel() →", arr10)
print("[11] transpose() →\n", arr11)
print("[12] concatenate() →", arr12)

print("\n[13] np.mean() →", mean)
print("[14] np.median() →", median)
print("[15] np.std() →", f"{std:.2f}")
print("[16] np.var() →", f"{var:.2f}")
print("[17] np.min() →", min_val)
print("[18] np.max() →", max_val)

print("\n[19] np.add() →", sum_arr)
print("[20] np.multiply() →", prod_arr)
print("[21] np.dot() →", dot_prod)
print("[22] np.sqrt() →", sqrt_arr)
print("[23] np.exp() →", exp_arr)
print("[24] np.log() →", log_arr)

print("\n[25] np.where() →", idx)
print("[26] np.sort() →\n", sorted_arr)
print("[27] np.unique() →", unique_vals)
print("[28] np.sum(axis=0) →", sum_axis)
print("[29] np.cumsum() →", cumsum_arr)
print("[30] np.clip() →", clip_arr)






import pandas as pd
import numpy as np

# ==================== ПОДГОТОВКА ДАННЫХ ====================
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'age': [25, 30, 35, 28, 32],
    'salary': [50000, 60000, 70000, 55000, 65000],
    'city': ['NY', 'LA', 'NY', 'CHI', 'LA']
})

s = pd.Series([10, 20, 30, 40, 50], name='numbers')





# ==================== 15 МЕТОДОВ DATAFRAME ====================
print("\n" + "=" * 50)
print("15 МЕТОДОВ DATAFRAME")
print("\n" + "=" * 50)


# 1. head() - первые N строк
print("\n[1] df.head(3) → первые 3 строки")
print(df.head(3))

# 2. info() - информация о DataFrame
print("\n[2] df.info() → информация о типах и null")
df.info()

# 3. describe() - статистика по числовым колонкам
print("\n[3] df.describe() → статистика")
print(df.describe())

# 4. shape - размерность (строки, колонки)
print(f"\n[4] df.shape → {df.shape} строк и колонок")

# 5. columns - список колонок
print(f"\n[5] df.columns → {df.columns.tolist()}")

# 6. dtypes - типы данных
print("\n[6] df.dtypes → типы колонок")
print(df.dtypes)

# 7. isna() / isnull() - проверка на пропуски
print("\n[7] df.isna().sum() → количество пропусков")
print(df.isna().sum())

# 8. dropna() - удалить пропуски
print("\n[8] df.dropna() → удалить строки с NaN")
print(df.dropna())  # здесь нет NaN, просто демонстрация

# 9. fillna() - заполнить пропуски
df_with_na = df.copy()
df_with_na.loc[0, 'age'] = np.nan
print("\n[9] df.fillna(0) → заполнить NaN нулями")
print(df_with_na.fillna(0))

# 10. groupby() - группировка
print("\n[10] df.groupby('city')['salary'].mean() → средняя зарплата по городам")
print(df.groupby('city')['salary'].mean())

# 11. sort_values() - сортировка
print("\n[11] df.sort_values('age', ascending=False) → сортировка по возрасту (убыв)")
print(df.sort_values('age', ascending=False))

# 12. merge() - объединение DataFrames
df2 = pd.DataFrame({'name': ['Alice', 'Bob'], 'bonus': [5000, 3000]})
print("\n[12] df.merge(df2, on='name') → объединение по колонке name")
print(df.merge(df2, on='name', how='left'))

# 13. apply() - применить функцию
print("\n[13] df['salary'].apply(lambda x: x * 1.1) → повышение зарплаты на 10%")
print(df['salary'].apply(lambda x: x * 1.1))

# 14. loc[] - доступ по меткам
print("\n[14] df.loc[df['age'] > 30] → строки с возрастом > 30")
print(df.loc[df['age'] > 30])

# 15. iloc[] - доступ по индексам
print("\n[15] df.iloc[1:4, 0:2] → строки 1-3, колонки 0-1")
print(df.iloc[1:4, 0:2])

# ==================== 15 МЕТОДОВ SERIES ====================
print("\n" + "=" * 50)
print("15 МЕТОДОВ SERIES")
print("\n" + "=" * 50)


# 1. value_counts() - подсчет уникальных значений
print("\n[1] s.value_counts() → частота каждого значения")
print(pd.Series([1, 2, 2, 3, 3, 3]).value_counts())

# 2. sum() - сумма
print(f"\n[2] s.sum() → {s.sum()}")

# 3. mean() - среднее
print(f"\n[3] s.mean() → {s.mean()}")

# 4. median() - медиана
print(f"\n[4] s.median() → {s.median()}")

# 5. min() / max() - минимум/максимум
print(f"\n[5] s.min() → {s.min()}, s.max() → {s.max()}")

# 6. std() - стандартное отклонение
print(f"\n[6] s.std() → {s.std():.2f}")

# 7. unique() - уникальные значения
print(f"\n[7] s.unique() → {s.unique()}")

# 8. nunique() - количество уникальных
print(f"\n[8] s.nunique() → {s.nunique()}")

# 9. sort_values() - сортировка
print(f"\n[9] s.sort_values(ascending=False) → {s.sort_values(ascending=False).values}")

# 10. sort_index() - сортировка по индексу
s2 = pd.Series([100, 200, 300], index=[3, 1, 2])
print(f"\n[10] s2.sort_index() → {s2.sort_index().values}")

# 11. reset_index() - сброс индекса
print(f"\n[11] s.reset_index(drop=True) → {s.reset_index(drop=True).values}")

# 12. astype() - смена типа
s_float = s.astype(float)
print(f"\n[12] s.astype(float) → {s_float.values}")

# 13. isin() - проверка вхождения
print(f"\n[13] s.isin([20, 40]) → {s.isin([20, 40]).values}")

# 14. cumsum() - кумулятивная сумма
print(f"\n[14] s.cumsum() → {s.cumsum().values}")

# 15. apply() - применить функцию
print(f"\n[15] s.apply(lambda x: x ** 2) → {s.apply(lambda x: x**2).values}")
