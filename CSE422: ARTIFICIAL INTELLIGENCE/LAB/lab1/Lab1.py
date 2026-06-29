graph = {'Arad': ('Zerind', 'Timisoara', 'Sibiu'), 
         'Craiova': ('Dobreta', 'RimnicuVilcea', 'Pitesti'), 
         'Eforie': ('Hirsova',),
         'Fagaras': ('Sibiu', 'Bucharest'), 
         'Giurgiu': ('Bucharest',), 'Mehadia': ('Lugoj', 'Dobreta'), 
         'Neamt': ('lasi',),
         'Sibiu': ('Oradea', 'Arad', 'RimnicuVilcea', 'Fagaras'), 
         'Oradea': ('Zerind', 'Sibiu'),
         'Pitesti': ('RimnicuVilcea', 'Craiova', 'Bucharest'), 
         'RimnicuVilcea': ('Sibiu', 'Craiova', 'Pitesti'),
         'Dobreta': ('Mehadia', 'Craiova'), 
         'Hirsova': ('Urziceni', 'Eforie'),
         'lasi': ('Vaslui', 'Neamt'),
         'Lugoj': ('Timisoara', 'Mehadia'), 
         'Timisoara': ('Arad', 'Lugoj'),
         'Urziceni': ('Bucharest', 'Hirsova', 'Vaslui'), 
         'Vaslui': ('Urziceni', 'lasi'), 'Zerind': ('Oradea', 'Arad'),
         'Bucharest': ('Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni')}

heuristic = {"Arad" : 366,
             "Bucharest" : 0,
             "Craiova" : 160,
             "Dobreta" : 242,
             "Eforie" : 161,
             "Fagaras" : 178,
             "Giurgiu" : 77,
             "Hirsova" : 151,
             "Iasi" : 226, 
             "Lugoj" : 244,
             "Mehadia" : 241,
             "Neamt" : 234,
             "Oradea" : 380,
             "Pitesti" : 98,
             "RimnicuVilcea" : 193,
             "Sibiu" : 253,
             "Timisoara" : 329,
             "Urziceni" : 80,
             "Vaslui" : 199,
             "Zerind" : 374}

# Read input file containing city distances
with open("input1.txt", "r") as file:
    inputs = file.read()
    input_split = inputs.split()

# Parse the input data to store path costs
path_cost = {}
for item in range(0, len(input_split), 2):
    city = input_split[item]
    adjacent_cityCost = int(input_split[item + 1]) 
    if city in path_cost:
        path_cost[city].append(adjacent_cityCost)
    else:
        path_cost[city] = [adjacent_cityCost]
        
# Build a dictionary storing parent-child relationships with costs
costFromParent = {}
count = 1
for city in graph.keys():
    if city in input_split:
        city_index = input_split.index(city) # Get index of the city in input
        city_cost = input_split[count]  # Retrieve cost associated with the city
        count += 2  # Move to next pair of city-cost values
        adjacent_cities = []
        for neighbor in graph[city]:  
            if neighbor in input_split:
                neighbor_cost = input_split[count] # Get neighbor's cost
                count += 2 # Move to next pair of neighbor-cost values
                adjacent_cities.append(f"{neighbor} : {neighbor_cost}") # Store neighbor cost with the neighbor itself
        costFromParent[f"{city} : {city_cost}"] = tuple(adjacent_cities)  # Store city and its adjacent cities with costs in dictionary

        
def A_star(n):
    total_cost = 0
    current_city = n
    closed_set = []  
    path = {}  
    final_path = [n]  
    h_cost = 366
    total_PathCost = 0

    while current_city != "Bucharest" and h_cost != 0:
        if current_city not in closed_set:
            closed_set.append(current_city)  # Mark those cities which are visited

        adj_costSet = []     # Stores costs of adjacent cities
        for m, l in graph.items(): # Iterate over current city and its neighbor city
            if m == current_city:
                for adj_city in l:
                    if adj_city not in closed_set:
                        for parent, adjacents in costFromParent.items():
                             parent_city = parent.split(" : ")[0] # Extract parent city name
                             if parent_city == current_city: # if parent city and current city name equals then find its child city
                                 for adjacent in adjacents:  # Iterate over neighbors of the current city
                                     neighbor, cost = adjacent.split(" : ")
                                     if neighbor == adj_city:
                                         adj_cost = int(cost)  # Convert path cost to integer of child city
                                         adj_h = heuristic[adj_city] # Get heuristic value of child city 
                                         adjTotal_cost = adj_h + adj_cost # Compute total cost [f(n) = h(n) + g(n)]
                                         adj_costSet.append(adjTotal_cost)  #Append the total cost of all the cities
                                         path[adj_city] = adjTotal_cost #store in dictionary with city as key and total cost as value
                      
        if adj_costSet:
            total_cost = min(adj_costSet) # Select the city with the lowest cost
            for i, j in path.items():
                if j == total_cost:
                    final_path.append(i) # Append city with the lowest cost to the final path

        # Check if a valid path exists
        if not final_path or final_path[-1] == current_city:
            print("NO PATH FOUND")
            break  # If no valid path is found or we are stuck in a loop, break the execution
            
        current_city = final_path[-1] # Move to the next city
        h_cost = heuristic[current_city]  # Update heuristic cost
        prev_pathCost = (total_cost - h_cost) #calculates the actual travel cost from the previous city to the current city
        total_PathCost += prev_pathCost # Update total cost
    final_path = (" -> ".join(final_path))
    
    return final_path, total_PathCost

start_city = "Arad"
final_path, total_PathCost = A_star(start_city)
final_path = final_path.replace("RimnicuVilcea", "Rimnicu")
print("Path:", final_path)
print("Total distance:", total_PathCost, "km")