import random

chromosomes = ["010101", "110001", "000101", "101100"]
generations = 10
mutation_rate = 0.1
for generation in range(generations):

    # Step 1: Convert binary strings to decimal
    decimal_values = []
    for x in chromosomes:
        decimal_values.append(int(x, 2))

    # Step 2: Evaluate fitness values
    fitness_values = []
    for x in decimal_values:
        raw_fitness = (x / 63) * 100
        fitness_values.append(raw_fitness)

    # Step 3: Find the best chromosome
    best_fitness = max(fitness_values)
    best_index = fitness_values.index(best_fitness)
    best_chromosome = chromosomes[best_index]
    print(f"Generation {generation}: Best Fitness = {best_fitness}, Best Chromosome = {best_chromosome}")

    # Step 4: Selection
    selection_probs = []
    for x in fitness_values:
        selection_probs.append(x / sum(fitness_values))
    selected_parents = random.choices(chromosomes, weights=selection_probs, k=2)

    # Step 5: Crossover
    parent1, parent2 = selected_parents
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]


    #2 point crossover
    # binary = ['001010','001011']
    # point1 = random.randint(1,len(binary[0])-1)
    # point2 = random.randint(point1+1,len(binary[0])-1)
    # print(point1,point2)

    # child1 = binary[1][:point1] + binary[0][point1:point2] + binary[1][point2:]
    # child2 = binary[0][:point1] + binary[1][point1:point2] + binary[0][point2:]

    # print(child1,child2)


    # Step 6: Mutation
    def mutate(chromosome):
        chromosome_list = list(chromosome)
        for i in range(len(chromosome_list)):
            if random.random() < mutation_rate: # Or we can simply mutate a specific bit
                if chromosome_list[i] == '0':
                    chromosome_list[i] = '1'
                else:
                    chromosome_list[i] = '0'
        return ''.join(chromosome_list)

    child1 = mutate(child1)
    child2 = mutate(child2)

    chromosomes_with_fitness = list(zip(chromosomes, fitness_values))
    chromosomes_with_fitness.sort(key=lambda x: x[1], reverse=True)
    sorted_chromosomes = []
    for x, y in chromosomes_with_fitness:
        sorted_chromosomes.append(x)
    chromosomes = sorted_chromosomes[:-2] + [child1, child2]

    # Step 1: Convert binary strings to decimal
    # Step 2: Evaluate fitness values
    # Step 3: Find the best chromosome
    # Step 4: Selection
    # Step 5: Crossover
    # Step 6: Mutation



