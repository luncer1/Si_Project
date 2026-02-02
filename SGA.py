import random


class SGA:
    def __init__(self, a, b, c, population_size, crossover_rate, mutation_rate):
        self.a = a
        self.b = b
        self.c = c
        self.population_size = population_size
        self.crossover_rate = crossover_rate / 100
        self.mutation_rate = mutation_rate / 100

    def objective_function(self, x) -> int:
        return (self.a * x * x) + (self.b * x) + self.c

    def generate_initial_population(self) -> list:
        population = []
        for _ in range(self.population_size):
            population.append(random.randrange(0, 255))
        return population

    def evaluate_population(self, population: list) -> dict:
        fitness_values = dict()
        for item in population:
            fitness_values[item] = self.objective_function(item)

        return fitness_values

    def check_negative_values(self, fitness_values: dict):
        if min(fitness_values.values()) <= 0:
            return min(fitness_values.values()) + 1
        else:
            return False

    @staticmethod
    def calculate_contributions(fitness_values: dict):
        total_fitness = 0
        for key in fitness_values.keys():
            total_fitness += fitness_values[key]

        if total_fitness == 0:
            total_fitness += 1

        for key in fitness_values.keys():
            fitness_values[key] = fitness_values[key] / total_fitness

        return {k: v for k, v in sorted(fitness_values.items(), key=lambda item: item[1])}

    def selection(self, contributions: dict) -> list:
        values = list()
        for index, value in enumerate(contributions.keys()):
            values.append(contributions[value])
            if index - 1 > -1:
                contributions[value] = contributions[value] + values[index - 1]
                values[index] = contributions[value]
        new_population = []
        for _ in range(self.population_size):
            random_number = random.random()
            for key in contributions.keys():
                if random_number < contributions[key]:
                    new_population.append(key)
                    break

        return new_population

    def mutation(self, population: list) -> list:
        new_population = []
        for individual in population:
            individual_binary = lambda x, n: format(x, 'b').zfill(n)
            new_individual = []
            for sign in [*individual_binary(individual, 8)]:
                mutation = random.random()
                if mutation <= self.mutation_rate:
                    if sign == '0':
                        new_individual.append('1')
                    else:
                        new_individual.append('0')
                else:
                    new_individual.append(sign)
            new_population.append(int(''.join(new_individual), 2))
        return new_population

    @staticmethod
    def pair_individuals(population: list) -> list:
        pairs = []
        cnt = 0
        while len(population) > 0:
            if len(population) == 1:
                pairs.append([population[0]])
                population.remove(population[0])
                break
            first = random.randrange(0, len(population), 1)
            second = random.randrange(0, len(population), 1)
            while first == second:
                first = random.randrange(0, len(population), 1)
            pairs.append([population[first], population[second]])
            first_individual = population[first]
            second_individual = population[second]
            population.remove(first_individual)
            population.remove(second_individual)
            cnt += 1
        return pairs

    def crossover(self, pairs: list) -> list:
        population = []
        individual_binary = lambda x, n: format(x, 'b').zfill(n)
        for pair in pairs:
            pair_bin = []
            if len(pair) == 1:
                population.append(pair[0])
                continue
            crossover_check = random.random()
            if crossover_check <= self.crossover_rate:
                for individual in pair:
                    pair_bin.append([*individual_binary(individual, 8)])
                crossover_point = random.randrange(1, len(pair_bin[0]))
                population.append(int(''.join(pair_bin[0][:crossover_point] + pair_bin[1][crossover_point:]), 2))
                population.append(int(''.join(pair_bin[1][:crossover_point] + pair_bin[0][crossover_point:]), 2))
            else:
                for individual in pair:
                    population.append(individual)
        return population





