# Задание 6: Расчет количества чайников в розетке
# Используется лямбда-функция для вычисления тока

# Справочные данные
VOLTAGE = 220  # Напряжение в сети, В
COPPER_RESISTIVITY = 0.0175  # Удельное сопротивление меди, Ом*мм2/м
MAX_CURRENT_DENSITY = 10  # Максимально допустимая плотность тока для меди, А/мм2 (стандарт)

def check_kettles():
    print("--- Расчет нагрузки на розетку ---")
    try:
        power_one = float(input("Введите мощность одного чайника (Вт): "))
        cable_section = float(input("Введите сечение медного кабеля (мм²): "))

        # Лямбда-функция для расчета максимально допустимого тока для кабеля
        # I_max = плотность тока * сечение
        get_max_current = lambda section: MAX_CURRENT_DENSITY * section
        
        # Лямбда-функция для расчета тока одного чайника
        # I_one = P / U
        get_kettle_current = lambda p, u: p / u

        max_current = get_max_current(cable_section)
        current_per_kettle = get_kettle_current(power_one, VOLTAGE)

        # Считаем количество чайников 
        # Используем int() для округления вниз, так как нельзя включить "половину" чайника
        count = int(max_current // current_per_kettle)

        print(f"\nМаксимально допустимый ток для кабеля {cable_section} мм²: {max_current:.1f} А")
        print(f"Ток потребления одного чайника: {current_per_kettle:.2f} А")
        print(f"Можно одновременно включить чайников: {count}")

        if count == 0:
            print("Внимание: Даже один чайник превысит допустимую нагрузку на этот кабель!")

    except ValueError:
        print("Ошибка: Пожалуйста, вводите числовые значения.")

if __name__ == "__main__":
    check_kettles()