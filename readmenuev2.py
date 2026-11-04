
def read_menu():
    menus = {}
    try:
        with open("menu.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line or ":" not in line:
                    continue

                category, detail = line.split(":", 1)
                menus[category.strip()] = detail.strip()
        return menus
    except FileNotFoundError:
        print("Please make sure menu.txt exists.")
        return menus
    except Exception as e:
        print(e)
        return menus

def split_into_variables(menu_items):
    shape = menu_items.get("SHAPE", "")
    style = menu_items.get("STYLE", "")
    metal = menu_items.get("METAL", "")
    diamond = menu_items.get("DIAMOND", "")
    return shape, style, metal, diamond

def print_menu(shape, style, metal, diamond):
    sections = (
        ("Shape", shape),
        ("Style", style),
        ("Metal", metal),
        ("Diamond", diamond),
    )

    for heading, choices in sections:
        print(f"{heading}\n")
        for choice in choices.split(','):
            print(f"\t{choice.strip()}")



def main():
    required_categories = {"SHAPE", "STYLE", "METAL", "DIAMOND"}
    missing_categories = required_categories - menu_items.keys()

    if missing_categories:
        print("Missing menu categories: " + ", ".join(sorted(missing_categories)))
        return

    shape, style, metal, diamond = split_into_variables(menu_items)
    print_menu(shape, style, metal, diamond)


if __name__ == "__main__":
    main()
