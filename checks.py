def check_for_correct_characters(side):
    if side == "":
        print(f"\n\033[0;31mПомилка!\nВведіть непорожню строку.\n")
        return False
    if not side.isdigit():
        print("\n\033[0;31mПомилка!\nБудь ласка введіть ціле невід'ємне число у десятковій формі.\n")
        return False
    else:
        return True


def check_for_zero(side):
    int_side = int(side)
    if int_side == 0:
        print("\n\033[0;31mПомилка!\nСторона трикутника повинна бути ненульовою.\n")
        return False
    else:
        return True


def check_for_size(side):
    if len(side) >= 7:
        print("\n\033[0;31mПомилка!\nЗавелика сторона, введіть менше число.\n")
        return False
    else:
        return True


def check_existence(triangle):
    sorted_triangle = sorted(triangle, reverse=True)
    if sorted_triangle[0] > sorted_triangle[1] + sorted_triangle[2]:
        return [triangle.index(sorted_triangle[0]), triangle.index(sorted_triangle[0]) + 1]
    else:
        return None

