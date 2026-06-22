season = input("enter season :")

# match season:
#     case "summer":
#         print("hot outside :")
#     case "winter":
#         print("cold outside :")    
#     case "monsoon":
#         print("rain outside :")    
#     case _:
#         print("invalid choice !")    

match season:
    case "summer" | "SUMMER" |"S"|"s":
        print("hot outside :")
    case "winter":
        print("cold outside :")    
    case "monsoon":
        print("rain outside :")    
    case _:
        print("invalid choice !")    