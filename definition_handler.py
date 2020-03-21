import random
import definitions

class DefinitionsHandler:

	def get_word_definition(self,word):
		""" looking for the definition of a given word under the Definitions enum class """
		for definition in (definitions.Definitions):
			if word in set(definition.value):
				return definition

	def get_elements_from_word_definitions(self,word_def):
		""" returns 3 random sample from definition list """
		return random.sample(word_def.value,3)
