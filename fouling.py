from random import randint
import statistics
import csv

LEAD = 3				#current lead
TIME = 10				#time left

FT_PCT = 78.36			#your free throw percentage
OPP_FT_PCT = 78.36		#opponent's free throw percentage

FG_PCT = 37.5			#your field goal percentage

THREE_PT_PCT = 35		#your three point percentage
OPP_THREE_PT_PCT = 35	#opponent's three point percentage

OPP_TWO_PT_PCT = 40		#opponent's two point percentage

OPP_TWO_PT_PROB = 90	#probability opponent takes two point shot when down 1 or 2

DEF_REB = 74.9			#probability of defensive rebound on a missed shot
OPP_OFF_REB = 25.1		#probability of offensive rebound on a missed shot
DEF_REB_FT = 88.5		#probability of defensive rebound on a missed free throw
OPP_OFF_REB_FT = 11.5	#probability of offensive rebound on a missed free throw

TIME_OPP_FOUL = 1		#time it takes for opponent to foul you
TIME_TO_FOUL = 1.5		#time it takes for you to foul opponent

def foulOpponent(leadIn, timeIn):
	lead = leadIn
	time = timeIn
	#take off time for fouling opponent depending on time left
	if time > 4:
		time = time/2
	else:	
		time = 0

	#shoot free throws and determine who gets possesion on a miss	
	if randint(1,100) <= OPP_FT_PCT:
		lead = lead - 1
	if randint(1,100) <= OPP_FT_PCT:
		lead = lead - 1
		time = time - TIME_OPP_FOUL
		if time > 0:
			if randint(1,100) <= FT_PCT:
				lead = lead + 1
			if randint(1,100) <= FT_PCT:
				lead = lead + 1
		else:
			if time > 0:
				if randint(1,100) <= DEF_REB_FT:
					time = time - TIME_OPP_FOUL
					if randint(1,100) <= FT_PCT:
						lead = lead + 1
					if randint(1,100) <= FT_PCT:
						lead = lead + 1
	
	return {'lead':lead, 'time':time}

def noFoul(leadIn, timeIn):
	lead = leadIn
	time = timeIn
	if time > 4:
		time = time/2
	else:
		time = 0
	if time > 0:
		if randint(1,100) <= OPP_THREE_PT_PCT:
			lead = lead - 3
			if randint(1,100) <= FG_PCT:
				lead = lead + 2
			time = 0
		else:
			if randint(1,100) <= DEF_REB:
				time = time - TIME_OPP_FOUL
				if randint(1,100) <= FT_PCT:
					lead = lead + 1
				if randint(1,100) <= FT_PCT:
					lead = lead + 1
	return {'lead':lead, 'time':time}

def bigLead(leadIn, timeIn):
	lead = leadIn
	time = timeIn
	if randint(1,100) <= OPP_THREE_PT_PCT:
		lead = lead - 3
		if time > 2:
			time = time/2
		else:
			time = 0
		if time > 0:
			time = time - TIME_OPP_FOUL
			if randint(1,100) <= FT_PCT:
				lead = lead + 1
			if randint(1,100) <= FT_PCT:
				lead = lead + 1
	else:
		if randint(1,100) <= DEF_REB:
			time = time - TIME_OPP_FOUL
			if randint(1,100) <= FT_PCT:
				lead = lead + 1
			if randint(1,100) <= FT_PCT:
				lead = lead + 1
	return {'lead':lead, 'time':time}

def smallLead(leadIn, timeIn):
	lead = leadIn
	time = timeIn
	if time > 2:
		time = time/2
	else:
		time = 0
	if time > 0:
		if randint(1,100) <= OPP_TWO_PT_PROB:
			if randint(1,100) <= OPP_TWO_PT_PCT:
				lead = lead - 2
				if randint(1,100) <= FG_PCT:
					lead = lead + 2
				if time > 2:
					time = time/2
				else:
					time = 0
			else:
				if randint(1,100) <= DEF_REB:
					time = time - TIME_OPP_FOUL
					if randint(1,100) <= FT_PCT:
						lead = lead + 1
					if randint(1,100) <= FT_PCT:
						lead = lead + 1
		else:
			if randint(1,100) <= OPP_THREE_PT_PCT:
				lead = lead - 3
				if randint(1,100) <= FG_PCT:
					lead = lead + 2
				if time > 2:
					time = time/2
				else:
					time = 0
			else:
				if randint(1,100) <= DEF_REB:
					time = time - TIME_OPP_FOUL
					if randint(1,100) <= FT_PCT:
						lead = lead + 1
					if randint(1,100) <= FT_PCT:
						lead = lead + 1
	return {'lead':lead, 'time':time}

def tieGame(leadIn, timeIn):
	lead = leadIn
	time = timeIn
	if randint(1,100) <= OPP_TWO_PT_PROB:
		if randint(1,100) <= OPP_TWO_PT_PCT:
			lead = lead - 2
	else:
		if randint(1,100) <= OPP_THREE_PT_PCT:
			lead = lead - 3
	time = 0
	return {'lead':lead, 'time':time}

def main(foul):
	lead = LEAD							#current lead
	time = TIME							#time left

	ftPct = FT_PCT						#your free throw percentage
	oppFtPct = OPP_FT_PCT				#opponent's free throw percentage
	
	fgPct = FG_PCT 						#your field goal percentage with less than 10 seconds left

	threePtPct = THREE_PT_PCT			#your three point percentage
	oppThreePtPct = OPP_THREE_PT_PCT	#opponent's three point percentage

	oppTwoPtPct = OPP_TWO_PT_PCT		#opponent's two point percentage

	oppTwoPointProb = OPP_TWO_PT_PROB	#probability opponent takes two point shot when down 1 or 2

	defReb = DEF_REB					#probability of defensive rebound on a missed shot
	oppOffReb = OPP_OFF_REB				#probability of offensive rebound on a missed shot
	defRebFt = DEF_REB_FT				#probability of defensive rebound on a missed free throw
	oppOffRebFt = OPP_OFF_REB_FT		#probability of offensive rebound on a missed free throw

	timeOppFoul = TIME_OPP_FOUL			#time it takes for opponent to foul you
	timeToFoul = TIME_TO_FOUL			#time it takes for you to foul opponent

	while time > 0:
		if lead == 3:
			if foul == True: #Foul!
				game = foulOpponent(lead, time)
				lead = game.get('lead')
				time = game.get('time')
			else: #Don't foul!
				#Take time off
				game = noFoul(lead, time)
				lead = game.get('lead')
				time = game.get('time')
		elif lead > 3:
			game = bigLead(lead, time)	
			lead = game.get('lead')
			time = game.get('time')
		elif lead < 0:
			return False
		elif lead == 0:
			game = tieGame(lead, time)
			lead = game.get('lead')
			time = game.get('time')	
		elif lead < 3:
			game = smallLead(lead, time)
			lead = game.get('lead')
			time = game.get('time')
		
	if lead > 0:
		return True
	elif lead < 0:
		return False
	else: #Overtime
		if randint(1,100) <= 50:
			return True
		else:
			return False

def writeToFile():
	o = open("test123.csv", "w")
	output = csv.writer(o, delimiter=',')
	
	trials = 10000
	winPctFoul = []
	num = 0
	pct = 0
	wins = 0
	losses = 0

	while num < trials:
		if main(True) == True:
			wins = wins + 1
		else:
			losses = losses + 1
		#winPctFoul.append([pct, 1])
		num = num + 1
	pct = wins/trials
	print(pct)

	winPctNoFoul = []
	num = 0
	pct = 0
	wins = 0
	losses = 0

	while num < trials:
		if main(False) == True:
			wins = wins + 1
		else:
			losses = losses + 1
		#winPctNoFoul.append([pct, 0])
		num = num + 1
	pct = wins/trials
	print(pct)

	#write to csv
	#output.writerows([winPctFoul])
	#output.writerows([winPctNoFoul])

writeToFile()