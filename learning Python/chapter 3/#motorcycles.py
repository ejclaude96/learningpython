#motorcycles.py
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#motorcycles.append('ducati') 
#print(motorcycles)
#motorcycles = []
#@motorcycles.append('honda')
#@motorcycles.append('yamaha')
#@motorcycles.append('suzuki')

#print(motorcycles)

motorcycles.insert(0, 'ducati')
#print(motorcycles)

#first_owned = motorcycles.pop()
#print(motorcycles)
#print(f"the first motorcycle I owned was a {first_owned.title()}")

motorcycles.remove('honda')
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me")

