def factorial(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def draw_line(tick_lenght: int, label: int | None = None) -> None:
    line = '-' * tick_lenght
    if label is not None:
        print(line, label)
    else:
        print(line)


def draw_section(major_tick_lenght: int) -> None:
    if major_tick_lenght == 0:
        return
    draw_section(major_tick_lenght - 1)
    draw_line(major_tick_lenght)
    draw_section(major_tick_lenght - 1)


def draw_sections(inches: int, major_tick_lenght: int) -> None:
    if inches == 0:
        return
    draw_sections(inches - 1, major_tick_lenght)
    draw_section(major_tick_lenght=major_tick_lenght)
    draw_line(tick_lenght=major_tick_lenght, label=inches)


def draw_ruler(inches: int, major_tick_lenght: int) -> None:
    draw_line(tick_lenght=major_tick_lenght, label=0)
    draw_sections(inches, major_tick_lenght)


draw_ruler(3, 3)
