#being called for main program
def read_menu():
    menus = {}
    try:
        with open("menu.txt", 'r') as file:
            for line in file:
                parts_of_line = line.strip().split(':')
                category = parts_of_line[0].strip()
                detail = parts_of_line[1].strip()
                menus[category] = detail
                print(f"contents of menu{menus}")
        return menus
    except FileNotFoundError:
        print("Please make sure menu.txt exists.")
    except IndexError:
        return menus # this handles blank lines in the text file
    except Exception as e:
        print(e)

def split_into_variables(menu_items):
    print(menu_items)
    shape = menu_items.get("SHAPE")
    style = menu_items.get("STYLE")
    metal = menu_items.get("METAL")
    diamond = menu_items.get("DIAMOND")
    return shape, style, metal, diamond

# def print_menu(shape, style, metal, diamond):
def print_shape(shape):
    print("Shape\n")
    print(shape)
    count = 1
    shape_item = shape.split(',')
    for item in shape_item:
        print(f"{count}.    {item.strip()}")
        count += 1

def print_style(style):
    print("Style\n")
    print(style)
    count = 1
    shape_item = style.split(',')
    for item in shape_item:
        print(f"{count}.    {item.strip()}")
        count += 1

def print_metal(metal):
    print("Metal\n")
    print(metal)
    count = 1
    shape_item = metal.split(',')
    for item in shape_item:
        print(f"{count}.    {item.strip()}")
        count += 1

def print_diamond(diamond):
    print("Diamond\n")
    print(diamond)
    count = 1
    shape_item = diamond.split(',')
    for item in shape_item:
        print(f"{count}.    {item.strip()}")
        count += 1



