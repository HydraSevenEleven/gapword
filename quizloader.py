import random
from enum import Enum

class QuizLoader:

	def __init__(self,db_file,num_sentences):
		self.db_file = db_file
		self.num_sentences = num_sentences

	def get_sentences(self):
		file = open(self.db_file).readlines()
		content = [x.strip('\n') for x in file]
		return content

	def get_random_sentences(self):
		list = self.get_sentences()
		list_of_random_sentences = random.sample(list,self.num_sentences)
		print(list_of_random_sentences)

	def get_word_definition(self,word):
		for definition in (Definitions):
			if word in set(definition.value):
				return definition

	def get_elements_from_word_definitions(self,word_def):
		print(random.sample(word_def.value,3))
		print(word_def)

class Definitions(Enum):
	DEFINED_ARTICLE		= ("der","die","das","den","dem")
	UNDEFINED_ARTICLE 	= ("ein","einen","eine","einem","einer","eines")

if __name__ == "__main__":
	x = QuizLoader("database",2)
	x.get_random_sentences()	
	wd = x.get_word_definition("der")
	print(wd)
	x.get_elements_from_word_definitions(wd)
	
