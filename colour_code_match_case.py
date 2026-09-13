# Question: Use match case to find the colour from a colour code.

colour_code = input()
colour_code = colour_code.upper()

match colour_code:
    case 'Y':
        print("Yellow")
    case 'R':
        print("Red")
    case "G":
        print("Green")
    case "B":
        print("Blue")
    case 'V':
        print("Violet")
    case 'O':
        print("Orange")
    case 'I':
        print("Indigo")
    case _:
        print("Invalid")
