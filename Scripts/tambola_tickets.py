""" Program for Printing Tambola Tickets """

# pylint: disable=C0325

import random
import sys

def numbers_per_ticket():
	"""
	Shortlists Numbers Per Ticket
	"""
	shuffled, ticket_nums = [], []
	sublists = [[j for j in (range(i+1, i+10) if i == 0 else range(i, i+10 if i != 80 else i+11))]
	            for i in range(0, 90, 10)]
	
	for sublist in sublists:
		random.shuffle(sublist)
		_ = [shuffled.append(j) for j in sublist]
		
	for i in range(6):
		ticket_nums.append([shuffled[j+i] for j in range(0, 90, 6)])
	
	random.shuffle(ticket_nums)
	
	return ticket_nums

def numbers_per_row(full_set):
	"""
	Divides Numbers Per Row in Ticket
	"""
	lines = []
	for set_ in full_set:
		threes = []
		set_.sort()
		
		for i in range(1, 6):
			sublist = set_[(i-1)*3: i*3]
			
			_ = [threes.append(s) for s in sublist]
			
		for i in range(3):
			lines.append(tuple([threes[j+i] for j in range(0, 15, 3)]))
	
	return lines

def positioning(lines):
	"""
	Fixes Position of Each Number on Ticket/Row
	"""
	ticket = []
	for row in lines:
		line = [False for i in range(9)]
		for cell in row:
			if not cell in (89, 90):
				line[(cell//10)] = cell
			else:
				line[8] = cell
		ticket.append(tuple(line))
		
	return ticket

def ticket_agent(total):
	"""
	Puts the Numbers and Postions Together
	"""
	tickets = list()
	cycles = total // 6
	extras = total % 6
	
	for _ in range(cycles):
		lines = numbers_per_row(numbers_per_ticket())
		
		for j in range(0, 6):
			tickets.append(positioning(lines[j*3 : (j+1)*3]))
		
	if extras != 0:
		lines = numbers_per_row(numbers_per_ticket())
			
		for j in range(0, extras):
			tickets.append(positioning(lines[j*3 : (j+1)*3]))
			
	return tickets

def main():
	"""
	Prints the Tambola Ticket
	"""
	tickets = list()
	if len(sys.argv) > 1:
		tickets = ticket_agent(int(sys.argv[1]))
	else:
		tickets = ticket_agent(1)
		
	for ticket in tickets:
		for row in ticket:
			for cell in row:
				print(cell, end='\t')
			print()
		print('\n')

if __name__ == '__main__':
	main()
