# Predefined list of Florida cities
florida_cities = ["Miami", "Orlando", "Tampa", "Jacksonville", "Fort Lauderdale"]


# Display the initial list of cities
print("Top 5 cities in Florida:")
for x in florida_cities:
  print(x)
 
# Prompt the user to enter a city to remove
city_to_move = input("What city would you like to move? ")
position = input("Which position for this city (1-5)?")

if int(position) > 5:
   print("Position must be a number between 1 and 5")
else:   
  new_position = int(position) -1
 
 
  if city_to_move in florida_cities:
        index_to_move = florida_cities.index(city_to_move)
        florida_cities.pop(index_to_move)
        florida_cities.insert(int(new_position),city_to_move)
        print(f"Moved '{city_to_move}' to position {position}.")
  else:
        print(f"'{city_to_move}' is not in the list of cities.")
    
  # Display the updated list of cities
  print("Updated top 5 cities:")
  for x in florida_cities:
   print(x)