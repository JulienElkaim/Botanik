import json
from datetime import datetime



#========================================= Functions to operate


def _inputLoadFile(relative_path="", file_name="exemple_ScriptInputFile.json"):
	data_dict = {}
	with open(relative_path + file_name) as json_data:
	    data_dict = json.load(json_data)
	return data_dict

def _strToDate(myString):
	datetime_object = datetime.strptime(myString, '%d-%m-%Y %H:%M:%S +0200')
	return datetime_object

def _switchDictKeysStrToDate(dico):
	new_dict = {}
	for key, elt in dico.items():
		new_dict[strToDate(key)] = elt

	return new_dict

#========================================= Functions END
def LoadInput():

	tasks_input = switchDictKeysStrToDate(inputLoadFile())
	inputer = list(tasks_input.keys())
	inputer.sort()
	now = strToDate("24-05-2019 16:00:00 +0200")

	keys_tasks_to_do =list(filter(lambda x: x <= now, inputer))

	tasks= []
	for key, elt in tasks_input.items():
		if key in keys_tasks_to_do :
			tasks+= list(elt.values())


	return tasks



