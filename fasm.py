'''
Fasm - A fungeoid language, implemented in Python
Copyright © 2013 Isaac Grant

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
'''
BOARD_SIZE = 16

class Pointer:
	def __init__(self, array):
		self.loc = 0
		self.length = len(array)
		self.array = array

	def inc(self):
		self.loc += 1
		if self.loc >= self.length:
			self.loc = 0

	def dec(self):
		self.loc -= 1
		if self.loc < 0:
			self.loc = self.length-1

	def clear(self):
		self.array[self.loc] = ' '

	def get(self):
		return self.array[self.loc]

	def pop(self):
		hold = self.get()
		self.clear()
		return hold

	def put(self, char):
		if str(char).isdigit():
			char = int(char)
		self.array[self.loc] = char

	def arithmetic(self, operator):
		first = self.pop()
		self.inc()
		second = self.pop()
		self.dec()
		result = {
		'+': first + second,
		'-': first - second,
		'*': first * second,
		'/': first / second,
		'%': first % second
		}[operator]
		self.put(result)
		return result

	def add(self):
		return self.arithmetic('+')

	def sub(self):
		return self.arithmetic('-')

	def mult(self):
		return self.arithmetic('*')

	def div(self):
		return self.arithmetic('/')

	def mod(self):
		return self.arithmetic('%')

def null():
	pass

def do(instruction, peek, pointer):
	retr = ''
	if instruction == ',':
		retr = pointer.put(peek)
	else:
		try:
			retr = {
			'': null,
			'>': pointer.inc,
			'<': pointer.dec,
			'^': pointer.pop,
			'.': pointer.get,
			'+': pointer.add,
			'-': pointer.sub,
			'*': pointer.mult,
			'/': pointer.div,
			'%': pointer.mod
			}[instruction]()
		except KeyError:
			print('ERROR: invalid instruction')
	return retr or ''


def interpret():
	pointer = Pointer([' ' for i in range(BOARD_SIZE)])
	instruction = ''
	put = False
	while not instruction == 'x':
		i = 0
		while i < len(instruction):
			if instruction[i] == ',' and i + 1 < len(instruction):
				do(instruction[i], instruction[i+1], pointer)
				i += 2
				continue
			else:
				retr = do(instruction[i], '', pointer)
			i += 1
			if not retr == '':
				print(retr, end='')
		print()
		instruction = input(':')

if __name__ == '__main__':
	from sys import argv
	argv = argv[1:]
	if len(argv) == 1:
		if argv[0].isdigit():
			BOARD_SIZE = int(argv[0])
			interpret()
		else:
			instructions = ''
			pointer = None
			with open(argv[0], 'r') as file:
				instructions = file.read().split('\n')
				if instructions[0].isdigit():
					pointer = Pointer([' ' for i in range(int(instructions[0]))])
					instructions = instructions[1]
				else:
					instructions = instructions[0]
					pointer = Pointer([' ' for i in range(BOARD_SIZE)])
			i = 0
			while i < len(instructions):
				if instructions[i] == ',' and i + 1 < len(instructions):
					print(do(instructions[i], instructions[i+1], pointer), end=',')
					i += 2
					continue
				else:
					print(do(instructions[i], '', pointer), end=',')
				i += 1
	else:
		interpret()