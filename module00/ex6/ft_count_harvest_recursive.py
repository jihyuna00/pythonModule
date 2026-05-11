def _harvest_helper(day, days):
    print("Day", day)
    if (day == days):
        print("Harvest time!")
    else:
        _harvest_helper(day + 1, days)

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    if days > 0:
        _harvest_helper(1, days)
