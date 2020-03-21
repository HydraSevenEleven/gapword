import random
import definitions
import definition_handler

class QuizLoader:

	def __init__(self,db_file,num_sentences):
		self.db_file = db_file
		self.num_sentences = num_sentences

	def get_sentences(self):
		""" returns a list with the sentences from the defined database file """
		file = open(self.db_file).readlines()
		content = [x.strip("\n\t") for x in file]
		return content

	def get_random_sentences(self):
		""" get random sentences from the database as a list """	
		return random.sample(self.get_sentences(),self.num_sentences)



if __name__ == "__main__":
	x = QuizLoader("database",2)
	print(x.get_random_sentences())	
	
	y = definition_handler.DefinitionsHandler() 	
	wd = y.get_word_definition("der")
	print(wd)
	y.get_elements_from_word_definitions(wd)
	
