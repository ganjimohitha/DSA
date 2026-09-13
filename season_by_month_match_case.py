# Question: Find the season using the month number.

season = int(input())

match season:
    case 3|4|5:
        print("Summer")
    case 6|7|8|9:
        print("Rainy")
    case 10|11|12|1|2:
        print("Winter")
    case _:
        print("Invalid")
