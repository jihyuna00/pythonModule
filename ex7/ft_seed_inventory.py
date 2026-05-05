def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    string = seed_type.capitalize() + " seeds:"
    match unit:
        case "packets":
            print(string, quantity, "packets available")
        case "grams":
            print(string, quantity, "grams total")
        case "area":
            print(string, "covers", quantity, "square meters")
        case _:
            print("Unknown unit type")


