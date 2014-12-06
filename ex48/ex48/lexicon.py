directions = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
verbs = ('go', 'stop', 'kill', 'eat')
stop_words = ('the', 'in', 'of', 'from', 'at', 'it')
nouns = ('door', 'bear', 'princess', 'cabinet')

def scan(input):
	words = input.split()
	sentence = []
	
	for word in words:
		if word in directions:
			sentence.append(('direction', word))
		elif word in verbs:
			sentence.append(('verb', word))
		elif word in stop_words:
			sentence.append(('stop', word))
		elif word in nouns:
			sentence.append(('noun', word))
		else:
			value = convert_number(word)
			if value == None:
				sentence.append(('error', word))
			else:
				sentence.append(('number', value))
				
	return sentence
	
def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None
