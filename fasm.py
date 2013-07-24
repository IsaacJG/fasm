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

class Board:
	def __init__(self, size):
		self.pointer = 0
		self.size = size
		self.__board__ = [' ' for i in range(size+1)]

	def inc(self):
		self.pointer += 1
		if self.pointer >= self.size:
			self.pointer = 0
	
	def dec(self):
		self.pointer -= 1
		if self.pointer < 0:
			self.pointer = self.size-1
	
	def clear(self):
		self.__board__[self.pointer] = ' '
	
	def get(self):
		return self.__board__[self.pointer]
	
	def pop(self):
		hold = self.get()
		self.clear()
		return hold

	def put(self, char):
		if str(char).isdigit():
			char = int(char)
		self.__board__[self.pointer] = char

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

def do(instruction, peek, board):
	retr = ''
	if instruction == ',':
		retr = board.put(peek)
	else:
		try:
			retr = {
			'': null,
			'>': board.inc,
			'<': board.dec,
			'^': board.pop,
			'.': board.get,
			'+': board.add,
			'-': board.sub,
			'*': board.mult,
			'/': board.div,
			'%': board.mod
			}[instruction]()
		except KeyError:
			print('ERROR: invalid instruction')
	return retr or ''


def interpret():
	board = Board(BOARD_SIZE)
	instruction = ''
	put = False
	while not instruction == 'x':
		i = 0
		while i < len(instruction):
			if instruction[i] == ',' and i + 1 < len(instruction):
				do(instruction[i], instruction[i+1], board)
				i += 2
				continue
			else:
				retr = do(instruction[i], '', board)
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
			board = None
			with open(argv[0], 'r') as file:
				instructions = file.read().split('\n')
				if instructions[0].isdigit():
					board = Board(int(instructions[0]))
					instructions = instructions[1]
				else:
					instructions = instructions[0]
					board = Board(BOARD_SIZE)
			i = 0
			while i < len(instructions):
				if instructions[i] == ',' and i + 1 < len(instructions):
					print(do(instructions[i], instructions[i+1], board), end=',')
					i += 2
					continue
				else:
					print(do(instructions[i], '', board), end=',')
				i += 1
	else:
		interpret()