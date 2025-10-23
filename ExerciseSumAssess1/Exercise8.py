names = ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave")
search = input('Enter the name you are looking for: ')

if search.capitalize() in names:
    print (f'{search} is in the list')
else:
    print (f'{search} is not in the list')