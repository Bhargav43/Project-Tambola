import random
import sys

def numbersPerTicket():
	shuffled, ticket_nums = [], []
	sublists = [range(1,10)] + [range(s*10, (s+1)*10) for s in range(1,8)] + [range(80,91)]
	for i in range(len(sublists)):
		sublists[i] = [i for i in sublists[i]]
		random.shuffle(sublists[i])
		[shuffled.append(j) for j in sublists[i]]
		
	for i in range(6):
		ticket_nums.append([shuffled[j+i] for j in range(0,90,6)])
	
	random.shuffle(ticket_nums)
	
	return ticket_nums

def numbersPerRow(setsOf15):
	
	setsOfLines = []
	for aSet in setsOf15:
		setsOf3 = []
		aSet.sort()
		
		for i in range(1,6):
			sublist = aSet[(i-1)*3: i*3]
			
			[setsOf3.append(s) for s in sublist]
			
		for i in range(3):
			setsOfLines.append(tuple([setsOf3[j+i] for j in range(0,15,3)]))
	
	return setsOfLines

def positioning(lines):
	
	ticket= []
	for row in lines:
		line = [False for i in range(9)]
		for cell in row:
			if not cell in (89, 90):
				line[(cell//10)] = cell
			else:
				line[8] = cell
		ticket.append(tuple(line))
		
	return ticket

def ticketAgent(total):
	tickets = list()
	cycles = total // 6
	extras = total % 6
	
	for i in range(cycles):
		lines = numbersPerRow(numbersPerTicket())
		
		for j in range(0, 6):
			tickets.append(positioning(lines[j*3 : (j+1)*3]))
		
	if extras!=0:
		lines = numbersPerRow(numbersPerTicket())
			
		for j in range(0, extras):
			tickets.append(positioning(lines[j*3 : (j+1)*3]))
	return tickets

def main():
	tickets = list()
	if len(sys.argv)>1:
		tickets = ticketAgent(int(sys.argv[1]))
	else:
		tickets = ticketAgent(1)
	
	for ticket in tickets:
		for row in ticket:
			for cell in row:
				print(cell, end='\t')
			print()
		print('\n')

if __name__ == '__main__':
	main()
