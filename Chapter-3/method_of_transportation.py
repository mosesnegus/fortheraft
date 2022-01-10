w = input("Is it currently raining? ")
if w == 'Yes':
    print('You should take the bus.')
elif w == 'No':
        distance = int(input("How far in km do you need to travel? "))
        if distance <= 2:
            print('You should walk.')
        elif distance <= 10:
            print('You should ride your bike.')
        elif distance >= 10:
            print('You should take the bus')