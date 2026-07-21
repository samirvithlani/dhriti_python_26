data = {"guj":"gandhinagar","mah":"mumbai","guj":"ahmedabad"}

while data:
    x = data.popitem()
    print(f"{x[0]} - {x[1]}")
    