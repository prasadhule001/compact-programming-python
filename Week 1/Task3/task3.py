# Task 3 - data type conversion

zahl = 10
zahl_als_float = float(zahl)
print("1. int -> float:", zahl, "becomes", zahl_als_float)

kommazahl = 10.5
kommazahl_als_int = int(kommazahl)
print("2. float -> int:", kommazahl, "becomes", kommazahl_als_int)

zahl2 = 7
zahl2_als_text = str(zahl2)
print("3. int -> string:", zahl2, "becomes", zahl2_als_text)

zahlentext = "123"
zahlentext_als_int = int(zahlentext)
print("4. string -> int:", zahlentext, "becomes", zahlentext_als_int)

zahl3 = 1
zahl3_als_bool = bool(zahl3)
print("5. int -> bool:", zahl3, "becomes", zahl3_als_bool)
