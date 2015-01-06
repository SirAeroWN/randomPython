#program to automatically generate english vocab quizes and grade them

import random

class Word:
	def __init__(self, wordStr = '', partOfSpeech = '', definition = '', synonyms = [], antonyms = ['none']):
		self.word = wordStr
		self.part = partOfSpeech
		self.definition = definition
		self.syns = synonyms
		self.ants = antonyms
		return

class Question:
	def __init__(self, Qtype, wordChoices, usedWords, number):
		self.word = self.generateWord(wordChoices, usedWords)
		used.append(self.word)
		self.right = False
		numStr = str(number) + ') '
		print(numStr, end = '')
		if Qtype == 'd':
			leQStr = 'Define ' + self.word.word + ' (do not just give a one word definition/synonym): '
			response = input(leQStr)
			promptForAnswer = 'The definition was: ' + self.word.definition + '\n\tDid you get it right? [y/n] '
			correct = input(promptForAnswer)
			if correct == 'y':
				self.right = True
		elif Qtype == 'sw':
			leQStr = 'Give a synonym of ' + self.word.word + ': '
			response = input(leQStr)
			if self.isIn(response, self.word.syns):
				self.right = True
			else:
				print('Possible synonyms are:')
				for syn in self.word.syns:
					print(syn, end = '\n')
		elif Qtype == 'p':
			leQStr = 'What part of speech is ' + self.word.word + ': '
			response = input(leQStr)
			if response == self.word.part:
				self.right = True
			else:
				print(self.word.part)
		elif Qtype == 's':
			leQStr = '"' + self.word.syns[random.randint(0,len(self.word.syns) - 1)] + '" is a synonym for what word? '
			response = input(leQStr)
			if response == self.word.word:
				self.right = True
			else:
				print(self.word.word)
		elif Qtype == 'aw':
			leQStr = 'Give a antonym of ' + self.word.word + ': '
			response = input(leQStr)
			if self.isIn(response, self.word.ants):
				self.right = True
			else:
				print('Possible antonyms are:')
				for ant in self.word.ants:
					print(ant, end = '\n')
		elif Qtype == 'a':
			anto = self.word.ants[random.randint(0,len(self.word.ants) - 1)]
			if anto == 'none':
				anto = self.word.word + 'is the answer'
			leQStr = '"' + anto + '" is a antonym for what word? '
			response = input(leQStr)
			if response == self.word.word:
				self.right = True
			else:
				print(self.word.word)

	def generateWord(self, avail, notAvail):
		newWord = avail[random.randint(0,35)]
		if self.isIn(newWord, notAvail):
			good = False
			while not good:
				newWord = avail[random.randint(0,35)]
				if self.isIn(newWord, notAvail):
					good = False
				else:
					good = True
		return newWord

	def isIn(self, leWord, allUsedUp):
		for thingy in allUsedUp:
			if leWord == thingy:
				return True
		return False


words = [Word('impugn', 'v', 'dispute the truth, validity, or honesty of, to call into question', ['challenge', 'question', 'dispute', 'query'], ['prove', 'validate']),
		Word('filch', 'v', 'to steal, especially in a sneaky way and in petty amounts', ['pilfer', 'purloin', 'swipe']),
		Word('implicit', 'adj', 'capable of being understood from something else though unexpressed', ['implied', 'tacit', 'unexpressed'], ['explicit', 'stated', 'expressed']),
		Word('denizen', 'n', 'a person, animal, or plant that lives in or often is found in a particular place or region', ['resident', 'dweller'], ['alien', 'outsider', 'stranger', 'foreigner']),
		Word('adamant', 'adj', 'firm in purpose or opinion', ['unyeilding', 'obdurate', 'implacable', 'inflexible'], ['yeilding', 'flexible', 'pliable']),
		Word('thwart', 'adj', 'prevent (someone) from accomplishing something; oppose (a plan) successfully', ['baffle', 'balk', 'beat', 'checkmate', 'discomfit'], ['facilitate']),
		Word('inscrutable', 'adj', 'incapable of being understood; impossible to see through physically', ['impenetrable', 'enigmatic', 'incomprehensible'], ['comprehensible', 'intelligible', 'penetrable']),
		Word('inauspicious', 'adj', 'not cunductive to success; unpromising', ['unpromising', 'unfavorable', 'unfortunate'], ['promising', 'lucky', 'fortunate']),
		Word('provincial', 'adj', 'of or concerning a province of a country or empire', ['rural', 'rustic']),
		Word('facetious', 'adj', 'treating serious issues with deliberately inappropriate humor', ['flippant', 'flip', 'glib', 'frivolous', 'tongue in cheek'], ['serious']),
		Word('transient', 'adj', 'lasting only for a short time; impermenent', ['transitory', 'temporary', 'short lived', 'short term'], ['permenent']),
		Word('gratuituos', 'adj', 'freely given; not called for by circumstances, unwarrented', ['voluntary','unjustified'], ['justified', 'warrented']),
		Word('supplicate', 'v', 'to make a humble entreaty; to pray to god', ['entreat', 'beg', 'implore']),
		Word('disconcert', 'v', 'to disturb the composure of; unsettle', ['upset', 'rattle', 'ruffle', 'faze', 'peturb'], ['relax', 'calm']),
		Word('bedlam', 'n', 'a state or scene of uproar and confusion', ['commotion', 'pandemonium', 'chaos', 'anarchy'], ['order', 'tranquility', 'peace']),
		Word('infringe', 'v', 'to violate, tresspass, go beyond recognized bounds', ['encroach', 'impinge', 'intrude', 'poach'], ['obey']),
		Word('gossamer', 'adj', 'used to refer to something very light, thin, and insubstantial or delicate', ['flimy', 'diaphamous', 'sheer', 'airy', 'feathery', 'gauzy'], ['thick', 'dense', 'solid', 'massive']),
		Word('desecrate', 'v', 'to damage a holy place or object; to treat a holy place or object with disrespect', ['profane', 'defile', 'violate'], ['revere', 'honor', 'venerate', 'consecrate']),
		Word('axiomatic', 'adj', 'self evident, obviously true', ['unquestionable'], ['questionable', 'dubious', 'controversial']),
		Word('prosaic', 'adj', 'of a person or thing: unpoetic, unromantic; dull, flat, unexiting, commonplace, mundane', ['ordinary', 'commonplace'], ['interesting', 'imaginative']),
		Word('satiate', 'v', 'to satisfy completely; to fill to excess', ['gratify', 'cloy', 'surfeit', 'gorge'], ['starve']),
		Word('profligate', 'adj', 'recklessly extravagent especcially with money; wasteful', ['extravagent', 'prodigal'], ['conserving', 'economical']),
		Word('evanescent', 'adj', 'vanishing, soon passing away, light and airy', ['ephemeral', 'transient', 'transitory'], ['everlasting', 'immortal', 'imperishable']),
		Word('efficacious', 'adj', 'having the power to produce a desired result or effect', ['effectual', 'efficient', 'potent', 'powerful'], ['ineffective', 'worthless', 'useless']),
		Word('blatant', 'adj', 'very obvious and offensive', ['flagrant', 'glaring', 'egregious'], ['inconsiquential', 'trifling', 'piddling', 'patty']),
		Word('tangential', 'adj', 'touching lightly; of little relevance', ['incidental', 'peripheral'], ['relevent']),
		Word('imperious', 'adj', 'having or showing the proud and unpleasant attitude of someone who gives orders and expects others to obey them', ['authoritarian', 'authoritative', 'autocratic'], ['humble', 'lowly', 'modest']),
		Word('debase', 'v', 'to lower the value or reputation of (someone or something), to make less respected', ['cheapen', 'corrupt', 'demean', 'depricate'], ['elevate', 'uplift', 'improve', 'enhance']),
		Word('salient', 'adj', 'moving by leaps or springs; something most notable or important', ['striking', 'notable', 'protrusive', 'obvious'], ['starve', 'deprive entirely of']),
		Word('curtail', 'v', 'to make less by or as if by cutting off or away some part', ['limit', 'abreviate', 'abridge', 'contract'], ['protract', 'extend']),
		Word('erudite', 'adj', 'having or showing or knowledge that is gained by studying', ['well read', 'scholarly', 'knowledgeable'], ['ignorant', 'uneducated', 'illiterate']),
		Word('tenuous', 'adj', 'thin, slender, not dense; lacking clarity or sharpness; of slight importance or signifigance', ['slight', 'insubstantial'], ['convincing', 'strong']),
		Word('stalwart', 'adj', 'loyal, reliable, and hardworking', ['staunch', 'loyal', 'faithful', 'committed'], ['disloyal', 'unfaithful', 'unreliable']),
		Word('impromptu', 'adj', 'done without being planned, organised, or rehearsed', ['unrehearsed', 'unprepaired', 'unscripted'], ['prepared', 'rehearsed']),
		Word('florid', 'adj', 'highly colored, reddish; excessively ornate, showy', ['flushed', 'ruddy', 'flowery', 'frily', 'flamboyent'], ['pale', 'ashen', 'pallid', 'sallow', 'austere', 'stark']),
		Word('inadvertant', 'adj', 'resulting from ar marked by lack of attention; unintentional, accidental', ['accidental', 'unconsidered'], ['deliberate', 'intentional', 'premeditated'])]

torture = True

while torture:
	used = []

	TypeOfQs = ['s', 'sw', 'a', 'aw', 'd', 'p']

	Qs = [Question(TypeOfQs[random.randint(0,5)], words, used, 1),
		Question(TypeOfQs[random.randint(0,5)], words, used, 2),
		Question(TypeOfQs[random.randint(0,5)], words, used, 3),
		Question(TypeOfQs[random.randint(0,5)], words, used, 4),
		Question(TypeOfQs[random.randint(0,5)], words, used, 5),
		Question(TypeOfQs[random.randint(0,5)], words, used, 6),
		Question(TypeOfQs[random.randint(0,5)], words, used, 7),
		Question(TypeOfQs[random.randint(0,5)], words, used, 8),
		Question(TypeOfQs[random.randint(0,5)], words, used, 9),
		Question(TypeOfQs[random.randint(0,5)], words, used, 10)]

	r = 0
	for q in Qs:
		if q.right:
			r += 1
	pstr = str(r) + '/10'
	print(pstr)
	if input('Take another quiz? [y/n]') == 'n':
		torture = False