def rgb_to_hex(r, g, b, a=None):
    if a is None:
        return "#{:02X}{:02X}{:02X}".format(r, g, b)
    else:
        return "#{:02X}{:02X}{:02X}{:02X}".format(r, g, b, a)

def get_user_input():
    try:
        r = int(input("Enter the red component (0-255): "))
        g = int(input("Enter the green component (0-255): "))
        b = int(input("Enter the blue component (0-255): "))
        
        alpha_input = input("Enter the alpha component (0-255), or press Enter to skip: ")
        a = int(alpha_input) if alpha_input else None

        return r, g, b, a
    except ValueError:
        print("Invalid input. Please enter integers between 0 and 255.")
        return None

def main():
    user_input = get_user_input()
    if user_input:
        r, g, b, a = user_input
        hex_color = rgb_to_hex(r, g, b, a)
        print(f"RGB{(r, g, b)}{' with alpha ' + str(a) if a is not None else ''} to Hex: {hex_color}")

if __name__ == "__main__":
    main()
