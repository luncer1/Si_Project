import SGA
import logging

DEBUG = True

def setup_logger():
    l = logging.getLogger('sga_logger')
    l.setLevel(logging.DEBUG)
    fh = logging.FileHandler('sga_debug.log')
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    l.addHandler(fh)
    return l

logger = setup_logger()

def debug_log(message):
    if DEBUG:
        logger.debug(message)
if __name__ == '__main__':
    crossover_rate = 60
    mutation_rate = 5
    population_size = 30
    generations = int(150 / population_size)
    statistical_trials = []
    with open("results.txt", 'w', encoding='utf-8') as f:
        for i in range(40):
            sga = SGA.SGA(11, 1, 6, population_size, crossover_rate, mutation_rate)
            population = sga.generate_initial_population()
            debug_log(f"Generation {i} - Population: {population}")
            for i in range(generations):
                fitness_values = sga.evaluate_population(population)
                negative_check = sga.check_negative_values(fitness_values)
                if negative_check is not False:
                    for key in fitness_values.keys():
                        fitness_values[key] = fitness_values[key] + (negative_check * (-1))
                contributions = sga.calculate_contributions(fitness_values)
                debug_log(f"Contributions: {contributions}")
                
                population = sga.selection(contributions)
                debug_log(f"Population after selection: {population}")
                population = sga.mutation(population)
                debug_log(f"Population after mutation: {population}")
                pairs = sga.pair_individuals(population)
                debug_log(f"Population - after pairing: {pairs}")
                population = sga.crossover(pairs)
                debug_log(f"Population - end: {population}")
            final_generation = sga.evaluate_population(population)
            best_individual = list(final_generation.keys())[0]
            for key in final_generation.keys():
                if final_generation[key] > sga.objective_function(best_individual):
                    best_individual = key
            debug_log(f"Best individual: {best_individual}")
            
            
            f.write(f"{sga.objective_function(best_individual)} {best_individual}\n")
            statistical_trials.append(best_individual)
            
        debug_log(f"Average best individual over trials: {sum(statistical_trials) / len(statistical_trials)}")