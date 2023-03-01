total = 0 
appetizer_name = 0 
fire_flakes = False
burning_wings = False
smokey_bacon = False
jalapeno_mac_cheese = False

print("welcome to Dragon Dining")
print()
#list of menu and prices
#adding the charge 
num_loop = (int(input("How many items do you want")))
loop_count = 0
while num_loop != loop_count:
  appetizer = input("what would you like to have Fire flakes 5.99, Burning wings 8.99, Smokey bacon 4.99, Jalapeno mac and cheese 9.99.")
  print()


  if appetizer == "Fire flakes" or appetizer == "fire flakes" or appetizer == "fire Flakes" or appetizer == "Fire Flakes":
    total += 5.99
    appetizer_name += 1
    fire_flakes = True
  elif appetizer == "Burning wings" or appetizer == "burning wings" or appetizer == "Burning Wings" or appetizer == "burning Wings":
    total += 8.99
    appetizer_name += 2
    burning_wings = True
  elif appetizer == "Smokey bacon" or appetizer == "smokey bacon" or appetizer == "Smokey Bacon" or appetizer == "smokey Bacon":
    total += 4.99
    appetizer_name += 3
    smokey_bacon = True
  elif appetizer == "Jalapeno mac and cheese" or appetizer == "Jalapeno Mac and cheese" or appetizer == "Jalapeno Mac and Cheese" or appetizer == "jalapeno mac and cheese":
    total += 9.99
    appetizer_name += 4
    jalapeno_mac_cheese = True

    
  

  if  fire_flakes:
    print("you picked fire flakes")
  elif burning_wings:
    print("you picked Burning wings")
  elif smokey_bacon:
    print("you picked Smokey bacon")
  elif jalapeno_mac_cheese:
    print("you picked the mac and cheese")
  fire_flakes = False
  burning_wings = False
  loop_count += 1


print(total)
#satisfaction
happy = input("Did you enjoy your time here at Dragon dining pick y or n")

if happy == "y":
  print("Come some other time :)")
if happy == "n":
  print("I am sorry, tell us what went wrong next time.")


