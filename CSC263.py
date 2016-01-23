# These go through all possible dice combinations and keep track of which combinations 
#of how many combinations the defender wins in and divides it by all possible combinations 
# When 2 armies are at stake in 1 combination in 2 vs 2 and 3 vs 2, each win is worth 0.5
# since you could lose 2 armies or just 1 or even none. This is different than 1 vs 1, 1 vs 2 etc... 
# where there is one possible win for every combination
#attacker- 1 vs defender -1
def calcrisk():
	dwin = 0
	awin = 0
	for d in range(0,6):
		for a in range (0,6): 
			if a > d:
				awin = awin + 1
			else: 
				dwin = dwin + 1
	return dwin/36
# This program goes through the 36 possible combinations and counts who would
# win in each case. 36 possibilities because 6 possibilities for first dice and
# 6 possibilities for the second dice so each number on the first dice has 6 possible 
# partners (6*6 = 36). Probability is 58.33%

# attacker -2 vs defender -1
def calcrisk2():
	dwin = 0
	awin = 0
	for d in range(0,6):
		for a in range (0,6): 
			for a1 in range (0,6): 
				if a > d:
					awin = awin + 1
				elif a1 > d: 
					awin = awin + 1
				else: 
					dwin = dwin + 1
	return dwin/216	
# This program goes through the 216 possible combinations and counts who would
# win in each case. 216 possibilities because 6 possibilities for first dice,
# 6 possibilities for the second dice and 6 possibilities for the third so each number on the first dice has 6 possible 
# partners which have another 6 possible partner (6*6*6 = 216), which is 216. 
# Probability is 42.13%

# attacker -3 vs defender -1 
def calcrisk3():
	dwin = 0
	awin = 0
	for d in range(0,6):
		for a in range (0,6): 
			for a1 in range (0,6): 
				for a2 in range (0,6): 
					if a > d:
						awin = awin + 1
					elif a1 > d: 
						awin = awin + 1
					elif a2 > d:
						awin = awin + 1
					else: 
						dwin = dwin + 1
	return dwin/1296
# This program goes through the 1296 possible combinations and counts who would
# win in each case. 1296 possibilities because 6 possibilities for first dice,
# 6 possibilities for the second dice, 6 possibilities for the third and 6 possibilities for the fourth
# so each number on the first dice has 6 possible 
# partners which have another 6 possible partner which have enough 5 so (6*6*6*6 = 1296), which is 1296. 
# Probability is 34.03%

#attacker -1 vs defender -2
def calcrisk4():
	dwin = 0
	awin = 0 
	for d in range (0,6): 
		for d1 in range (0,6): 
			if d > d1: 
				for a in range(0,6):
					if a > d:
						awin = awin + 1
					else:
						dwin = dwin + 1
			else: 
				for a in range(0,6):
					if a > d1: 
						awin = awin + 1
					else: 
						dwin = dwin + 1			
	return dwin/216
# This program goes through the 216 possible combinations and counts who would
# win in each case. 216 possibilities because 6 possibilities for first dice,
# 6 possibilities for the second dice and 6 possibilities for the third so each number on the first dice has 6 possible 
# partners which have another 6 possible partner (6*6*6 = 216), which is 216. 
# Probability 74.54%

#attacker -2 vs defender -2
def calcrisk5():
	dwin = 0
	# roll defender die
	for d1 in range(0,6):
		for d2 in range (0,6): 
			# d1 is bigger than d2
			if d1 > d2: 
				#roll attacker die
				for a1 in range (0,6): 
					for a2 in range (0,6): 
						#a1 > a2
						if a1 > a2:
							#compare d1 and a1
							if d1 > a1 or d1 ==a1: 
								dwin = dwin + 0.5 
							#compare d2 and a2	
							if d2 > a2 or d2 == a2: 
								dwin = dwin + 0.5
						#a2 >= a1
						else: 
							#compare d1 and a2
							if d1 > a2 or d1 == a2: 
								dwin = dwin + 0.5

							if d2 > a1 or d2 == a1:
								dwin = dwin + 0.5
			#d2 >= d1
			else: 
				#roll attacker die
				for a1 in range (0,6): 
					for a2 in range (0,6): 
						#a1 > a2
						if a1 > a2:
							#compare d2 and a1
							if d2 > a1 or d2 ==a1: 
								dwin = dwin + 0.5
							#compare d1 and a2
							if d1 > a2 or d1 == a2: 
									dwin = dwin + 0.5
						#a2 >=a1
						else:
							#compare d2 and a2
							if d2 > a2 or d2 == a2: 
								dwin = dwin + 0.5
							#compare d1 and a1	
							if d1 > a1 or d1 ==a1:
								dwin = dwin + 0.5									
	return dwin/1296
# This program goes through the 1296 possible combinations and counts who would
# win in each case. 1296 possibilities because 6 possibilities for first dice,
# 6 possibilities for the second dice, 6 possibilities for the third and 6 possibilities for the fourth
# so each number on the first dice has 6 possible 
# partners which have another 6 possible partner which have enough 5 so (6*6*6*6 = 1296), which is 1296. 
# Probability is 61.03%

# attacker -3 vs defender-2

def calcrisk6():
	dwin = 0
	#roll defender die
	for d1 in range(0,6):
		for d2 in range (0,6): 	
			for a1 in range (0,6): 
				for a2 in range (0,6): 
					for a3 in range(0,6):
						list1, list2 = [d1,d2], [a1,a2,a3]
						if max(list1) >= max(list2):
							dwin = dwin + 0.5
						list1.remove(max(list1))
						list2.remove(max(list2))
						if max(list1) >= max(list2):
							dwin = dwin + 0.5						
						
	return dwin/7776
# This program goes through the 7776 possible combinations and counts who would
# win in each case. 777k possibilities because 6 possibilities for first dice,
# 6 possibilities for the second dice, 6 possibilities for the third and 6 possibilities for the fourth
# and 6 for the fifth. 
# so each number on the first dice has 6 possible 
# partners which have another 6 possible partner which have enough 5 so (6*6*6*6*6 = 7776). 
# Probability is 46.05%
		
			
	
