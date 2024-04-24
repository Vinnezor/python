
def game_core_v3(number: int = 1) -> int:
    # Выставляем максимальное число
    start_num = 100
    # Тут храним остаток для бинарного поиска
    remainder = start_num
    count = 0

    # Алгоритм бинарного поиска
    while number != start_num:
        count += 1
        remainder = 1 if remainder == 1 else remainder // 2
        if number > start_num:
            start_num = start_num + remainder
        elif number < start_num:
            start_num = start_num - remainder

    return count

