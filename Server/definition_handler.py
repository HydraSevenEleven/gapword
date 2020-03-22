import random
import definitions

class DefinitionsHandler:

	def get_set_possibly_answers(self,word):
		""" looking for the definition of a given word under the Definitions enum class """
		for definition in (definitions.Definitions):
			if word in set(definition.value):
				return definition

	def get_multiple_choice(self,right_answer):
		""" returns 3 random sample from definition list """
		possibly_answers = self.get_set_possibly_answers(right_answer)
		# the right answer should not be twice in the list 
		list_possibly_answer = list(possibly_answers.value)
		list_possibly_answer.remove(right_answer)
		false_answers = random.sample(list_possibly_answer,3)
		false_answers.append(right_answer)
		multiple_choice = random.sample(false_answers,4)
		return multiple_choice
			
