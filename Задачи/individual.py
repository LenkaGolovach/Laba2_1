# Известно значение температуры по шкале Цельсия. Найти соответствующее значение
# температуры по шкале:
# Фаренгейта;
# Кельвина.
# Для пересчета по шкале Фаренгейта необходимо исходное значение температуры умножить
# на 1,8 и к результату прибавить 32, а по шкале Кельвина абсолютное значение нуля
# соответствует –273,15 градуса по шкале Цельсия.

cels = int(input("Print cels - "))
Far = (cels * 1.8) + 32
Kel = -273.15 + cels
print(cels, Far, Kel)