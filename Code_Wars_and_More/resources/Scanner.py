from enum import Enum

class Token:
	def __init__(self, kind, lexme):
		self.kind = kind
		self.lexme = lexme

class DFA:
	acceptingStates: (str) =\
	(
		"AL", "AMID", "AMIDO", "AMIN", "AMINO", "AN", "ARSIN", "ARSINO",
		"BENZ", "BROMO", "BUT", 
		"CARBON",  "CARBOXY", "CARBOXYLIC_ACID", "CHLORO", "CYCLO",
		"DEC", "DECA", "DI", "DO",
		"E", "EN", "ETH", "ETHER", 
		"FLUORO", "FORM",
		"HEPT", "HEPTA", "HEX", "HEXA", "HYDR",
		"IMIN", "IMINO", "IODO",
		"MERCAPTO", "METH",
		"NON", "NONA",
		"OATE", "OCT", "OCTA", "OIC_ACID", "OL", "ON", "OXO", "OXY", "OYL",
		"PENT", "PENTA", "PHEN", "PHOSPHIN", "PHOSPHINO", "PROP",
		"TETRA", "THIOL", "TRI",
		"UN",
		"YL", "YN",
		"WHITESPACE", "COMMA", "LBRACK", "RBRACK", "NUM", "DASH"
	)

	startingState: str = "START"
	transitions: {dict} =\
	{ 
		"START":
		{ 
			"a":"A", "b":"B", "c":"C", "d":"D", "e":"E", "f":"F",
			"h":"H", "i":"I", "m":"M", "n":"N", "o":"O","p":"P", 
			"t":"T", "u":"U", "y":"Y", " ":"WHITESPACE", "-":"DASH",
			 ",":"COMMA", "[":"LBRACK", "]":"RBRACK", "0":"NUM", "1":"NUM",
			"2":"NUM", "3":"NUM", "4":"NUM", "5":"NUM", "6":"NUM", "7":"NUM",
			"8":"NUM", "9":"NUM"  
		},

		"NUM": 
		{ 
			"0":"NUM", "1":"NUM", "2":"NUM", "3":"NUM", "4":"NUM", 
			"5":"NUM", "6":"NUM", "7":"NUM", "8":"NUM", "9":"NUM"
		},
		
		"WHITESPACE": {" ":"WHITESPACE"},

		"A": { "l":"AL", "m":"AM", "n":"AN", "r":"AR" },

		"AM": { "i": "AMI" },

		"AMI": { "d": "AMID", "n":"AMIN" },

		"AMID": { "o": "AMIDO" },

		"AMIN": { "o": "AMINO" },

		"AR": { "s": "ARS" },

		"ARS": { "i": "ARSI" },

		"ARSI": { "n": "ARSIN" },

		"ARSIN": { "o": "ARSINO" },

		"B": { "e":"BE", "r":"BR", "u":"BU" },

		"BE": { "n":"BEN" },
		
		"BEN": { "z":"BENZ" },
		
		"BR": { "o":"BRO" },
		
		"BRO": { "m":"BROM" },
		
		"BROM": { "o":"BROMO" },
		
		"BU": { "t":"BUT" },
		
		"C": { "a":"CA", "h":"CH", "y":"CY" },
		
		"CA": { "r": "CAR" },
		
		"CAR": { "b" : "CARB" },
		
		"CARB": { "o" : "CARBO" },
		
		"CARBO": { "n" : "CARBON", "x":"CARBOX" },
		
		"CARBOX": { "y":"CARBOXY" },
		
		"CARBOXY": { "l":"CARBOXYL" },
		
		"CARBOXYL": { "i":"CARBOXYLI" },
		
		"CARBOXYLI": { "c":"CARBOXYLIC" },
		
		"CARBOXYLIC": { " ":"CARBOXYLIC_" },
		
		"CARBOXYLIC_": { "a":"CARBOXYLIC_A" },
		
		"CARBOXYLIC_A": { "c":"CARBOXYLIC_AC" },
		
		"CARBOXYLIC_AC": { "i":"CARBOXYLIC_ACI" },
		
		"CARBOXYLIC_ACI": { "d":"CARBOXYLIC_ACID" },
		
		"CH": { "l" : "CHL" },
		
		"CHL": { "o" : "CHLO" },
		
		"CHLO": { "r" : "CHLOR" },
		
		"CHLOR": { "o" : "CHLORO" },
		
		"CY": { "c" : "CYC" },
		
		"CYC": { "l" : "CYCL" },
		
		"CYCL": { "o" : "CYCLO" },
		
		"D": { "e":"DE", "i":"DI", "o":"DO" },
		
		"DE" : { "c": "DEC" },
		
		"DEC" : { "a" : "DECA" },
		
		"E": { "n":"EN", "t":"ET" },
		
		"ET": { "h" : "ETH" },
		
		"ETH": { "e" : "ETHE" },
		
		"ETHE": { "r" : "ETHER" },
		
		"F": { "l":"FL", "o":"FO" },
		
		"FL": { "u" : "FLU" },
		
		"FLU": { "o" : "FLUO" },
		
		"FLUO": { "r" : "FLUOR" },
		
		"FLUOR": { "o" : "FLUORO" },
		
		"FO": { "r" : "FOR" },
		
		"FOR": { "m" : "FORM" },
		
		"H": { "e":"HE", "y":"HY" },
		
		"HE": { "x":"HEX", "P":"HEP" },
		
		"HEX": { "a":"HEXA"},
		
		"HEP": { "t":"HEPT"},
		
		"HEPT": { "a":"HEPTA"},
		
		"HY":{"d":"HYD"},
		
		"HYD":{"r":"HYDR"},
		
		"I": { "m":"IM", "o":"IO" },
		
		"IM":{"i":"IMI"},
		
		"IMI":{"n":"IMIN"},
		
		"IMIN":{"o":"IMINO"},
		
		"IO":{"d":"IOD"},
		
		"IOD":{"o":"IODO"},
		
		"M": { "e":"ME"},
		
		"ME": { "r":"MER", "t":"MET"},
		
		"MER": { "c":"MERC"},
		
		"MERC": { "a":"MERCA"},
		
		"MERCA": { "p":"MERCAP"},
		
		"MERCAP": { "t":"MERCAPT"},
		
		"MERCAPT": { "o":"MERCAPTO"},
		
		"MET": { "h":"METH"},
		
		"N": { "o":"NO" },
		
		"NO": { "n":"NON" },
		
		"NON": { "a":"NONA" },
		
		"O": { "a":"OA", "c":"OC", "i":"OI", "l":"OL", "n":"ON", "x":"OX", "y":"OY" },
		
		"OA":{ "t":"OAT" },
		
		"OAT":{ "e":"OATE" },
		
		"OC":{ "t":"OCT" },
		
		"OCT":{ "a":"OCTA" },
		
		"OI":{"c":"OIC"},
		
		"OIC":{" ":"OIC_"},
		
		"OIC_":{"a":"OIC_A"},
		
		"OIC_A":{"c":"OIC_AC"},
		
		"OIC_AC":{"i":"OIC_ACI"},
		
		"OIC_ACI":{"d":"OIC_ACID"},
		
		"OX":{"y":"OXY", "o":"OXO"},
		
		"OY":{"l":"OYL"},
		
		"P": { "e":"PE", "h":"PH", "R":"PR" },
		
		"PE": { "n":"PEN" },
		
		"PEN": { "t":"PENT" },
		
		"PENT": { "a":"PENTA" },
		
		"PH": { "e":"PHE", "o":"PHO" },
		
		"PHE": { "n":"PHEN"},
		
		"PHO": { "s":"PHOS"},
		
		"PHOS": { "p":"PHOSP"},
		
		"PHOSP": { "h":"PHOSPH"},
		
		"PHOSPH": { "i":"PHOSPHI"},
		
		"PHOSPHI": { "n":"PHOSPHIN"},
		
		"PHOSPHIN": { "o":"PHOSPHINO"},
		
		"PR":{"o":"PRO"},
		
		"PRO":{"p":"PROP"},
		
		"T": { "e":"TE", "h":"TH", "r":"TR" },
		
		"TR":{"i":"TRI"},
		
		"TE":{"t":"TET"},
		
		"TET":{"r":"TETR"},
		
		"TETR":{"a":"TETRA"},
		
		"TH":{"I":"THI"},
		
		"THI":{"o":"THIO"},
		
		"THIO":{"l":"THIOL"},
		
		"U": { "n":"UN" },
		
		"Y": { "l":"YL", "n":"YN" }
					
	}


	def maximalMunch(self, input):
		i = 1
		result = []
		stack = []
		stack.append(("", i))
		while (True):
			pastStart = False
			numPast = 0
			q = self.startingState
			inputRead = ""

			while (i <= len(input) and q in self.transitions and input[i-1] in self.transitions[q]):
				#if (q in self.acceptingStates):
				#	stack = []
				stack.append((q,i,inputRead))
				inputRead += input[i-1]
				q = self.transitions[q][input[i-1]]
				i += 1

			while (q not in self.acceptingStates):
				q, i, inputRead = stack.pop()
				if (pastStart):
					numPast += 1
				if (q == ""):
					print("fatal error")
					return result
				elif (q == "START"):
					pastStart = True

			result = result[:-numPast or None]
			result.append((q, inputRead))
			if (i >= len(input)): return result



class Scanner(object):
	def filterTokens(self, input):
		if input[0] in ['WHITESPACE', 'COMMA', 'DASH']:
			return False
		else:
			return True

	def scan(self, input):
		dfa = DFA()
		tokenlist = dfa.maximalMunch(input)
		return list(filter(self.filterTokens, tokenlist))

print(Scanner().scan("3-[2-mercapto]ethylpentane-1,4-diol"))



