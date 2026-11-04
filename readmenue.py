
def read_menu():
    menus = {}
    try:
        with open("menu.txt", 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                category, detail = line.split(':', 1)
                menus[category.strip().upper()] = detail.strip()
        return menus
    except FileNotFoundError:
        print("Please make sure menu.txt exists.")
        return menus
    except ValueError:
        print("Each menu line must contain a category and value separated by ':'.")
        return menus
    except Exception as e:
        print(e)

def split_into_variables(menu_items):
    shape = menu_items.get("SHAPE")
    style = menu_items.get("STYLE")
    metal = menu_items.get("METAL")
    diamond = menu_items.get("DIAMOND")
    print(shape)
    return shape, style, metal, diamond

def print_menu(shape, style, metal, diamond):
    """ This section deliberately incomplete """
    print("Shape\n")
    print(shape)
    shape_item = shape.split(',')
    for item in shape_item:
        print(f"\t{item.strip()}")

    print("Style\n")
    shape_item = style.split(',')
    for item in shape_item:
        print(f"\t{item.strip()}")

    print("Metal\n")
    shape_item = metal.split(',')
    for item in shape_item:
        print(f"\t{item.strip()}")


    print("Diamond\n")
    shape_item = diamond.split(',')
    for item in shape_item:
        print(f"\t{item.strip()}")



def main():
    menu_items = read_menu()
    shape, style, metal, diamond = split_into_variables(menu_items)
    print_menu(shape, style, metal, diamond)

if __name__ == "__main__":
    main()
