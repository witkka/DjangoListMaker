class Entry:
    """
    Class responsible for obtaining data from json object
    """

    def __init__(self, data, n):
        self.word = data[n].get("word")
        self.phonetic = data[n].get("phonetic")
        self.phonetics = data[n].get("phonetics")
        self.origin = data[n].get("origin")
        self.meanings = data[n].get("meanings")
        self.definitions = self.meanings[0].get("definitions")

    def get_word(self):
        """ Method returns word: str """
        return self.word

    def get_phonetic(self):
        """ Method returns phonetic representation of a given word """
        return self.phonetic

    def get_origin(self):
        """ Method returns information about hte origin of a given word """
        return self.origin

    def get_audio(self):
        """ Method returns link to audio file containing the pronunciation of a given word """
        return self.phonetics[0].get("audio")

    def get_parts_of_speech(self):
        """ Method returns information obout part of speach of a given word """
        return self.meanings[0].get("partOfSpeech")

    def get_definitions(self):
        """ Method returns list of definitions of a given word including text of definition, example, synonyms and
         antonyms """
        return self.definitions

    def get_definition(self, n):
        """Method returns n'th definition from the list of definitions (get_definition) of a given word"""
        return self.definitions[n].get("definition")

    def get_example(self, n):
        """Method returns n'th example from the list of definitions (get_definition) of a given word"""
        return self.definitions[n].get("example")

    def get_synonyms(self, n):
        """Method returns n'th synonym from the list of definitions (get_definition) of a given word"""
        synonym = self.definitions[n].get("synonyms")
        if len(synonym) == 0:
            return None
        else:
            return synonym

    def get_antonyms(self, n):
        """Method returns n'th antonym from the list of definitions (get_definition) of a given word"""
        antonym = self.definitions[n].get("antonyms")
        if len(antonym) == 0:
            return None
        else:
            return antonym
