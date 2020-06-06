#   Programa en Python3 para crear una cadena objetivo, 
#   a partir de una cadena aleatoria usando Algoritmos Genéticos 

import random 

# Número de individuos en cada generación (Población) 
POPULATION_SIZE = 100

# Genes Válidos 
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP 
QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

# Cadena objetivo a generar   
TARGET = "Inteligencia Artificial Trabajo Final"

class Individual(object): 
	''' 
	Clase que nos permite describir a cada individuo dentro de la población
	'''
	def __init__(self, chromosome): 
		self.chromosome = chromosome 
		self.fitness = self.cal_fitness() 

	@classmethod
	def mutated_genes(self): 
		''' 
		Se crean aleatoriamente los genes para llevar a cabo la mutación 
		'''
		global GENES 
		gene = random.choice(GENES) 
		return gene 

	@classmethod
	def create_gnome(self): 
		''' 
		Se crean los cromosomas(las cadenas de genes)  
		'''
		global TARGET 
		gnome_len = len(TARGET) 
		return [self.mutated_genes() for _ in range(gnome_len)] 

	def mate(self, par2): 
		''' 
		Se realiza el apareamiento y se producen nuevas crías (Mutación y Selección) 
		'''

		# Cromosomas para las Descendencias  
		child_chromosome = [] 
		for gp1, gp2 in zip(self.chromosome, par2.chromosome):	 

			# Probabilidad Aletoria 
			prob = random.random() 

			# Si la probabilidad es menor a 0.45, se insertará un gen 
			# de la descendencia 1 
			if prob < 0.45: 
				child_chromosome.append(gp1) 

			# Si la probabilidad esta entre 0.45 y 0.90, se insertará 
			# un gen la descendencia 2 
			elif prob < 0.90: 
				child_chromosome.append(gp2) 

			# Si no es asi se insertará un gen(Mutado) aleatorio , 
			# para mantener la diversidad 
			else: 
				child_chromosome.append(self.mutated_genes()) 

		# Se crean nuevo Individuos(Descendencia) usando 
		# cromosomas generados para la misma Descendencia
		return Individual(child_chromosome) 

	def cal_fitness(self): 
		''' 
		Calcula el fittness score, que es el número de 
        carácteres que difieren de la cadena 
		objetivo. 
		'''
		global TARGET 
		fitness = 0
		for gs, gt in zip(self.chromosome, TARGET): 
			if gs != gt: fitness+= 1
		return fitness 

# Código piloto 
def main(): 
	global POPULATION_SIZE 

	# Generación actual
	generation = 1

	found = False
	population = [] 

	# Creación de la población inicial 
	for _ in range(POPULATION_SIZE): 
				gnome = Individual.create_gnome() 
				population.append(Individual(gnome)) 

	while not found: 

        # clasificación de la población en orden ascendente de fitness score 
		population = sorted(population, key = lambda x:x.fitness) 

		# Si el individuo tiene un fitness score por debajo de 0
        # entonces se alcanzo el objetivo y rompemos el loop
		if population[0].fitness <= 0: 
			found = True
			break

		# Si no es así seguimos generando nuevas descendencias para 
        # las nuevas generaciones 
		new_generation = [] 

		# Al realizar la selección, significa que el 10% de la poblacion
        # es mejor(Apta) para la nueva generación
		s = int((10*POPULATION_SIZE)/100) 
		new_generation.extend(population[:s]) 

		# A partir de la seleccion en un 50% de la población, 
        # los individuos se aparearán para producir descendencia 

		s = int((90*POPULATION_SIZE)/100) 
		for _ in range(s): 
			parent1 = random.choice(population[:50]) 
			parent2 = random.choice(population[:50]) 
			child = parent1.mate(parent2) 
			new_generation.append(child) 

		population = new_generation 

		print("Generation: {}\tString: {}\tFitness: {}".
			format(generation, 
			"".join(population[0].chromosome), 
			population[0].fitness)) 

		generation += 1

	
	print("Generation: {}\tString: {}\tFitness: {}".
		format(generation, 
		"".join(population[0].chromosome), 
		population[0].fitness)) 

if __name__ == '__main__': 
	main() 
