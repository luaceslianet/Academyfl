def print_city_list(cities):

    print("The top cities in Florida are:")

    for index, city in enumerate(cities, start=1):

        print(f"{index}) {city['city']} (Rank: {city['rank']})")
 
# List of top cities in Florida with ranks (as dictionaries)

florida_cities = [

    {"city": "Miami", "rank": "1"},

    {"city": "Orlando", "rank": "2"},

    {"city": "Tampa", "rank": "3"},

    {"city": "Jacksonville", "rank": "4"},

    {"city": "Fort Lauderdale", "rank": "5"}

]
 
# Print the formatted list of cities with ranks

print_city_list(florida_cities)
 
# Prompt the user to select a city by name

city_name = input("Enter the name of a city to view its current rank: ")
 
# Find the city in the list of dictionaries

selected_city = None

for city in florida_cities:

    if city["city"].lower() == city_name.lower():

        selected_city = city

        break
 
# If the city is found, display its current rank and confirm

if selected_city:

    print(f"The city you chose ({selected_city['city']}) is currently ranked #{selected_city['rank']}.")

    new_rank = input("Enter the new rank: ")

    confirm = input("Are you certain you want to proceed? (yes/no): ")

    if confirm.lower() == "yes":

        print("Proceeding with the selected city...")
        for city_info in florida_cities:
          if city_info["city"] == city_name:
            city_info["rank"] = new_rank

        # Convert "rank" values to integers
         
        sorted_cities = sorted(florida_cities, key=lambda x:x['rank'])
       
           
        # Print the sorted list of cities with ranks
        print_city_list(sorted_cities)
    else:

        print("Operation canceled.")

else:

    print(f"City '{city_name}' not found in the list of top cities in Florida.")
