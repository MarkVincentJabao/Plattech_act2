import json

places = []

while True:
    place = input("Enter a place (or 'q' tp quit): ")
    if place == "q":
        break
    places.append(place)

places_json = json.dumps(places)

print("all places entered:")
for place in places:
    print(place)