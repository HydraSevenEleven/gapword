import random
import json
from definition_handler import DefinitionsHandler as def_hdl


class QuizLoader:

	def __init__(self,db_file,num_sentences):
		self.db_file = db_file
		self.num_sentences = num_sentences
		self.hdl = def_hdl()

	def get_sentences(self):
		""" returns a list with the sentences from the defined database file """
		file = open(self.db_file).readlines()
		content = [x.strip("\n\t") for x in file]
		return content

	def get_random_sentences(self):
		""" get random sentences from the database as a list """	
		return random.sample(self.get_sentences(),self.num_sentences)
	
	def set_questions(self):
		""" set the questions """
		my_json_string=[]
		list_of_random_sentences = self.get_random_sentences()
		for sentence in list_of_random_sentences:
			splitted_sentence = sentence.split('|')
			possibly_answer_list = self.hdl.get_multiple_choice(splitted_sentence[1])
			item = {'sentence':splitted_sentence[0],'choice':possibly_answer_list}
			my_json_string.append(item)
		jsonData = json.dumps(my_json_string, ensure_ascii=False)
		print(jsonData)

if __name__ == "__main__":
	x = QuizLoader("database",2)
	x.set_questions()	
	
	
