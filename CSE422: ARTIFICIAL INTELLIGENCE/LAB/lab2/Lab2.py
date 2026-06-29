
#Part-1
import random
# Step 1: Define the Chromosome Structure
parents = []
for count in range(4):
  stop_loss = random.randint(1, 99)
  take_profit = random.randint(1, 99)
  Trade_size = random.randint(1, 99)
  if stop_loss < 10:
    stop_loss = "0" + str(stop_loss)   #formate chromosome
  else:
    stop_loss = str(stop_loss)

  if take_profit < 10:
    take_profit = "0" + str(take_profit)
  else:
    take_profit = str(take_profit)

  if Trade_size < 10:
    Trade_size = "0" + str(Trade_size)
  else:
    Trade_size = str(Trade_size)

  # Step 2: Initialize Population
  parent = str(stop_loss + take_profit + Trade_size)
  parents.append(parent)
initial_population = parents
#print(initial_population)
#print(parents)

# Step 3: Evaluate Fitness (Profit Calculation)
for generation in range(10):   #Generating 10 generation.
  historical_price = [-1.2, 3.4, -0.8, 2.1, -2.5, 1.7, -0.3, 5.8, -1.1, 3.5]
  Initial_capital = 1000.0
  current_capital = Initial_capital
  fitness_scores = []

  #print(f"Generation : {generation + 1} {parents}")
  for p in parents:
    current_capital = Initial_capital
    for price in historical_price:           # Calculate fitness for each parent
      if price > int(p[2:4]):
        price = int(p[2:4])
      elif price < -int(p[0:2]):
        price = -int(p[0:2])

      trade_size = 1000 * (int(p[4:6]) / 100.0)
      new_captial = round(current_capital + (trade_size * (price / 100)), 2)
      current_capital = new_captial

    fitness_score = round((current_capital - Initial_capital), 2)  #Calculating fitness score with two decimal point
    fitness_scores.append(fitness_score)   #Appending each fitness_score in fitness_scores list

  fitness = []
  for i in range(len(fitness_scores)):
    fitness.append((fitness_scores[i], parents[i]))  #Storing fiteness score and its corresponding parents together

  for i in range(len(fitness)):
    for j in range(i + 1, len(fitness)):
      if fitness[i][0] < fitness[j][0]:            #Sorting fitness score manually
        fitness[i], fitness[j] = fitness[j], fitness[i]

  elitism = []
  elitism_scores = []
  for i in range(4):
    elitism_scores.append(fitness[i][0])  # Appending top 4 fitness score ----> elitism_scores
    elitism.append(fitness[i][1])  # Appending top 4 parents ----> elitism

  #print("Fitness score:", generation + 1, elitism_scores)

  parents = elitism  #Modifying parents with elite chromosome
  #print(len(elitism))

  random_parent1 = [parents[0], parents[1]]     #selecting parents for crossover. Here "parents" are generating randomly and I am just mentioning index for simplicity.
  random_parent2 = [parents[2], parents[3]]

  # Step 4: Select Parents (Random Selection)
  random_index1 = random.randint(0, len(random_parent1[0]) - 1)
  random_index2 = random.randint(0, len(random_parent1[1]) - 1)
  random_index3 = random.randint(0, len(random_parent2[0]) - 1)
  random_index4 = random.randint(0, len(random_parent2[1]) - 1)

  gene1 = list(random_parent1[0])  #Converting to list from string.
  gene2 = list(random_parent1[1])  #We need to convert the strings into lists because strings in Python are immutable, meaning you cannot modify individual characters directly.
  gene3 = list(random_parent2[0])  #Mutability refers to the ability of an object to be changed after it is created.
  gene4 = list(random_parent2[1])  ##Lists are mutable. Lists allow to change elements easily using indexing.

  # Step 5: Crossover (Recombine Parent Genes)
  temp1 = gene1[random_index1]
  gene1[random_index1] = gene2[random_index2]  #By exhanging one index, I implement crossover between parent1 and parent2.
  gene2[random_index2] = temp1

  temp2 = gene3[random_index3]
  gene3[random_index3] = gene4[random_index4] #Crossover between parent3 and parent4.
  gene4[random_index4] = temp2

  random_parent1[0] = "".join(gene1)
  random_parent1[1] = "".join(gene2)   #Again converting strings from lists for further operation.
  random_parent2[0] = "".join(gene3)
  random_parent2[1] = "".join(gene4)
  #print(random_parent1)
  #print(random_parent2)
  crossovers = []

  for i in range(len(random_parent1)):
    crossovers.append(random_parent1[i])  #Appending the crossovers in the crossovers list.
    crossovers.append(random_parent2[i])

    #print(crossovers)

  # Step 6: Mutation (Introduce Random Changes)
  muted_child = []
  for child in crossovers:
    child_list = list(child)                         #converting to list for mutability.
    random_count = random.randint(1, 100)
    if random_count <= 5:                                  #5% mutation. If "random_count" generate number that less than 5, it will perform mutation.
      random_idx = random.randint(0, len(child_list) - 1)  #Randomly choose a index called "random_idx".
      child_list[random_idx] = str(random.randint(0, 9))   #In that particular index("random_idx"), putting random number.
      muted_child.append("".join(child_list))              #Again convert to string and append in muted_chid list.
      #print("muted child : ",generation, muted_child)
    #else:
      #print("random -", generation)

  #Step 7: Generate New Population (Next Generation)
  newGeneration = crossovers + muted_child            #Calculating new generation.
  parents = newGeneration                             #New generation wil be the parents.

final_fitnessScore = max(elitism_scores)    #Finding maximum fitness score.

for score in elitism:
  strategy = elitism[elitism_scores.index(final_fitnessScore)]  #Extracting the parent chromosome for the maximum fitness score.

stop_loss = strategy[0:2]
take_profit = strategy[2:4]   #Extracting stop loss, take profit, trade size.
trade_size = strategy[4:6]

if stop_loss[0] == "0":
  stop_loss = stop_loss[1]

if take_profit[0] == "0":
  take_profit = take_profit[1]    #Handeling special case for "0" in index 0.

if trade_size[0] == "0":
  trade_size = trade_size[1]

strategy_dict = {}
strategy_dict["stop_loss"] = int(stop_loss)
strategy_dict["take_profit"] = int(take_profit)
strategy_dict["trade_size"] = int(trade_size)
print("best_strategy :",strategy_dict)                #Printing statement.
print("Final_profit :", final_fitnessScore)

#Part-2
twoPoint_parents = []
random_parent1 = random.randint(0, len(initial_population) - 1)

while True:
  random_parent2 = random.randint(0, len(initial_population) - 1)           #Randomly choosing 2 parents.
  if random_parent2 != random_parent1:
    break
#print(random_parent1, random_parent2)

twoPoint_parents.append(initial_population[random_parent1])          #Extracting parents and storing it to "twoPoint_parents".
twoPoint_parents.append(initial_population[random_parent2])

#print("Random selected parents : ", twoPoint_parents)
random_point1 = random.randint(0, len(twoPoint_parents[0]) - 3)                    #Randomly generating 2 points for two point crossover.
random_point2 = random.randint(random_point1+1, len(twoPoint_parents[0]) - 2)

#print(random_point1, random_point2)
Crossover_parent1 = twoPoint_parents[0][random_point1 : random_point2+1 : ]     #Cutting the numbers between two points fo both parents.
Crossover_parent2 = twoPoint_parents[1][random_point1 : random_point2+1 : ]
#print(Crossover_parent1, Crossover_parent2)

parent1 = list(twoPoint_parents[0])      #Converting to list for dealing with mutability.
parent2 = list(twoPoint_parents[1])

parent1[random_point1:random_point2+1] = list(Crossover_parent2)    #Swapping the cutting numbers between two points between two parent.
parent2[random_point1:random_point2+1] = list(Crossover_parent1)

parent1 = "".join(parent1)            #Converting in string.
parent2 = "".join(parent2)
twoPoint_parent = "  ".join(twoPoint_parents)
print("Random selected parents for two pointed crossover :",twoPoint_parent)
print("Two pointed crossover :", parent1, parent2)  #Printing statement.

twoPointmuted_child = []
for child in twoPoint_parents:                 #Performing one iteration.
  child_list = list(child)                      #converting to list for mutability.
  random_count = random.randint(1, 100)
  if random_count <= 5:                                  #5% mutation. If "random_count" generate number that less than 5, it will perform mutation.
    random_idx = random.randint(0, len(child_list) - 1)  #Randomly choose a index called "random_idx".
    child_list[random_idx] = str(random.randint(0, 9))   #In that particular index("random_idx"), putting random number.
    twoPointmuted_child.append("".join(child_list))              #Again convert to string and append in muted_chid list.
    #print("muted child : ",generation, muted_child)
  #else:
    #print("random")

newGeneration = [parent1 , parent2] + twoPointmuted_child        #Calculating new generation.
new_generation = "  ".join(newGeneration)
print("Two point crossover parents after the mutation :", new_generation)
fitness_scores = []
for p in newGeneration:
  current_capital = Initial_capital
  for price in historical_price:           # Calculate fitness for each parent
    if price > int(p[2:4]):
      price = int(p[2:4])
    elif price < -int(p[0:2]):
      price = -int(p[0:2])

    trade_size = 1000 * (int(p[4:6]) / 100.0)
    new_captial = round(current_capital + (trade_size * (price / 100)), 2)
    current_capital = new_captial

  fitness_score = round((current_capital - Initial_capital), 2)  #Calculating fitness score with two decimal point
  fitness_scores.append(fitness_score)   #Appending each fitness_score in fitness_scores list

twoPoint_bestProfit = max(fitness_scores)     #Finding maximum fitness score.
print("Two pointed crossover best profit :", twoPoint_bestProfit)

for score in newGeneration:
  twoPoint_bestParent = newGeneration[fitness_scores.index(twoPoint_bestProfit)]  #Extracting the parent chromosome for the maximum fitness score.

print("Two pointed crossover best fitness score's parent :" ,twoPoint_bestParent)  #Printing statement