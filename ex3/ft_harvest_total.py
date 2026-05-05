def ft_harvest_total():
    day1_harvest = int(input("Day 1 harvest: "))
    day2_harvest = int(input("Day 2 harvest: "))
    day3_harvest = int(input("Day 3 harvest: "))

    total_harvest = day1_harvest + day2_harvest + day3_harvest

    print(f"Total harvest: {total_harvest}")
