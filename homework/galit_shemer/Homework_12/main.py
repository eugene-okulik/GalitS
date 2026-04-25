from flowers import Rose, Tulip, Bouquet

rose1 = Rose("Rose", "red", 50, 8, 10, 7)
rose2 = Rose("Rose", "white", 45, 7, 9, 6)
tulip1 = Tulip("Tulip", "yellow", 40, 9, 5, 5)

bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(rose2)
bouquet.add_flower(tulip1)

print("Total price:", bouquet.total_price())
print("Average lifetime:", bouquet.average_lifetime())

bouquet.sort_by("price")
for f in bouquet.flowers:
    print(f.name, f.price)

found = bouquet.find_by("color", "red")
for f in found:
    print("Found:", f.name, f.color)
