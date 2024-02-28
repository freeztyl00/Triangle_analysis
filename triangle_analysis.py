import checks

triangle = list()
i = 0


print("\nПрограма аналізу трикутника за сторонами...")
while i <= 2:
    side = input(f"\033[0mВведіть {i + 1} сторону: ")
    # Перевірка на некоректні символи включаючи букви, порожні строки та від'ємні числа
    if not checks.check_for_correct_characters(side):
        continue
    # Перевірка на нуль
    elif not checks.check_for_zero(side):
        continue
    # Перевірка на кількість символів
    elif not checks.check_for_size(side):
        continue
    elif i == 2 or len(triangle) == 3:
        # Якщо знадобиться переписати існуючу сторону після непроходження некст перевірки
        if len(triangle) == 3:
            triangle[i] = int(side)
        else:
            triangle.append(int(side))
        # Перевірка на можливість існування трикутника
        final_check = checks.check_existence(triangle)
        if final_check is not None:
            print(f"\n\033[0;31mПомилка!\nCторона {final_check[1]}"
                  f" більша за суму двох інших сторін, трикутник неможливий.")
            answer = input("\n\033[0;36mБажаєте змінити усі сторони чи лише найбільшу?\n(Так - 1, Ні - 0): ")
            if answer == "1":
                i = 0
                triangle.clear()
                continue
            else:
                i = final_check[0]
                continue
        else:
            break
    else:
        triangle.append(int(side))
        i += 1

print("\n\033[1;33mТрикутник зі сторонами: ")
for s in triangle:
    print("{:>4}".format(s), end="\t")
triangle_srtd = sorted(triangle, reverse=True)
print("\n\033[1;34mЄ", end=" ")

# Перевірки тупокутного трикутника
if pow(triangle_srtd[0], 2) > pow(triangle_srtd[1], 2) + pow(triangle_srtd[2], 2):
    print("\033[1;34mтупокутним та", end=" ")
    if (triangle_srtd[0]
            == triangle_srtd[1] or triangle_srtd[0] == triangle_srtd[2] or triangle_srtd[1] == triangle_srtd[2]):
        print("\033[1;34mрівнобедренним.")
    else:
        print("\033[1;34mрізностороннім.")

# Перевірки гострокутного трикутника
elif pow(triangle_srtd[0], 2) < pow(triangle_srtd[1], 2) + pow(triangle_srtd[2], 2):
    print("\033[1;34mгострокутним та", end=" ")
    if (triangle_srtd[0]
            == triangle_srtd[1] or triangle_srtd[0] == triangle_srtd[2] or triangle_srtd[1] == triangle_srtd[2]):
        if (triangle_srtd[0]
                == triangle_srtd[1] & triangle_srtd[0] == triangle_srtd[2] & triangle_srtd[1] == triangle_srtd[2]):
            print("\033[1;34mрівностороннім.")
        else:
            print("\033[1;34mрівнобедренним.")
    else:
        print("\033[1;34mрізностороннім.")

# Перевірки прямокутного трикутника
else:
    print("\033[1;34mпрямокутним та", end=" ")
    if (triangle_srtd[0]
            == triangle_srtd[1] or triangle_srtd[0] == triangle_srtd[2] or triangle_srtd[1] == triangle_srtd[2]):
        print("\033[1;34mрівнобедренним.")
    else:
        print("\033[1;34mрізностороннім.")
