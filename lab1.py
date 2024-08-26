#1➔ Напишите программу, которая запрашивает у пользователя последовательно день его рождения, месяц и год

def is_leap_year1(year):
    """Проверяет, является ли год високосным."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def is_valid_date(day, month, year):
    """Проверяет, является ли введённая дата корректной."""
    if month < 1 or month > 12:
        return False
    if year < 1:  # Предполагаем, что год должен быть положительным
        return False

    # Определение количества дней в месяце
    days_in_month = [31, 29 if is_leap_year1(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Проверка на корректность дня
    if day < 1 or day > days_in_month[month - 1]:
        return False

    return True

def main():
    while True:
        try:
            day = int(input('Введите день вашего рождения: '))
            month = int(input('Введите месяц вашего рождения: '))
            year = int(input('Введите год вашего рождения: ')) 
            
            if is_valid_date(day, month, year):
                print(f'Родились вы {day} дня {month} месяца {year} года!')
                break
            else:
                print('Некорректная дата. Пожалуйста, попробуйте снова.')
        except ValueError:
            print('Пожалуйста, введите корректные числовые значения.')

if __name__ == "__main__":
    main()

#2➔ Напишите функцию, которая определяет какому дню недели соответствует эта дата?
from datetime import datetime

def get_weekday(date):
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    
    # Преобразуем строку в объект даты
    date_obj = datetime.strptime(date, "%d-%m-%Y")
    
    # Получаем день недели
    weekday = date_obj.weekday()  # 0 - понедельник, 6 - воскресенье
    
    return date_obj.strftime("%d-%m-%Y"), days[weekday]

# Входные данные
date = input("Введите дату в формате 'дд-мм-гггг': ")
new_date, weekday_name = get_weekday(date)
print(f'Дата {new_date} соответствует {weekday_name}')


#3➔ Напишите функцию, которая определяет - високосный это был год, или нет?
def is_leap_year(year):
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        return True
    else:
        return False

year = int(input("Введите год:"))
leap_year_status = is_leap_year(year)

# Выводим результаты
print(f'Год {year} {"високосный" if leap_year_status else "не високосный"}')
#4➔ Напишите функцию, которая определяет сколько сейчас лет пользователю;
import datetime

def calculate_user_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# Ввод даты рождения от пользователя
birth_date_input = input("Введите вашу дату рождения в формате 'дд-мм-гггг': ")
day, month, year = map(int, birth_date_input.split('-'))
birth_date = datetime.date(year, month, day)

# Вычисляем возраст
age = calculate_user_age(birth_date)

print(f"Ваш возраст сейчас составляет: {age} лет.")



#5➔	Реализуйте вывод в консоль даты рождения пользователя в формате дд мм гггг,
#  где цифры прорисованы звёздочками (*), как на электронном табло.
import datetime

# Словарь для представления цифр в виде звёздочек
digit_to_star = {
    '0': [" *** ", "*   *", "*   *", "*   *", " *** "],
    '1': ["  *  ", " **  ", "  *  ", "  *  ", " *****"],
    '2': [" *** ", "    *", " *** ", "*    ", " *** "],
    '3': [" *** ", "    *", " *** ", "    *", " *** "],
    '4': ["*   *", "*   *", " *** ", "    *", "    *"],
    '5': [" *** ", "*    ", " *** ", "    *", " *** "],
    '6': [" *** ", "*    ", " *** ", "*   *", " *** "],
    '7': [" *** ", "    *", "   * ", "  *  ", " *   "],
    '8': [" *** ", "*   *", " *** ", "*   *", " *** "],
    '9': [" *** ", "*   *", " *** ", "    *", " *** "]
}

def is_valid_date1(day, month, year):
    try:
        datetime.datetime.strptime(f"{day}-{month}-{year}", "%d-%m-%Y")
        return True
    except ValueError:
        return False

def print_date_in_stars(date_str):
    # Преобразуем дату в формат дд мм гггг
    date_parts = date_str.split('-')

    # Проверка на количество частей
    if len(date_parts) != 3:
        print("Неправильный формат даты. Используйте дд-мм-гггг.")
        return
    
    day, month, year = date_parts

    # Проверка на корректность длины и содержимого
    if (len(day) != 2 or len(month) != 2 or len(year) != 4 or 
        not (day.isdigit() and month.isdigit() and year.isdigit())):
        print("Дата должна состоять из двух цифр для дня, двух цифр для месяца и четырёх цифр для года.")
        return

    # Преобразуем строки в числа
    day, month, year = int(day), int(month), int(year)

    # Проверка на диапазон для дня и месяца
    if not (1 <= day <= 31) or not (1 <= month <= 12):
        print("День должен быть от 01 до 31, а месяц от 01 до 12.")
        return
    
    # Проверка на корректность даты
    if not is_valid_date1(f"{day:02d}", f"{month:02d}", year):
        print("Некорректная дата.")
        return

    # Выводим дату в формате звёздочек
    for i in range(5):  # Каждая цифра имеет 5 строк
        output_line = ""
        for char in f"{day:02d} {month:02d} {year}":  # Добавляем пробел между частями даты
            if char in digit_to_star:
                output_line += digit_to_star[char][i] + "  "
            else:
                output_line += "     "  # Для пробела
        print(output_line)

# Ввод даты рождения от пользователя
birth_date_input = input("Введите вашу дату рождения в формате 'дд-мм-гггг': ")
print_date_in_stars(birth_date_input)
