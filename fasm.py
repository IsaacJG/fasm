'''
Fasm - A language inspired by Brainfuck, implemented in Python

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

class Pointer:
	def __init__(self, array):
		self.loc = 0
		self.length = len(array)
		self.array = array
		self.looping = False
		self.looper = []
		self.loop_left = 'unset'
		self.loop_right = 'unset'

	def up(self):
		self.loc += 1
		if self.loc >= self.length:
			self.loc = 0

	def down(self):
		self.loc -= 1
		if self.loc < 0:
			self.loc = self.length-1

	def inc(self):
		self.array[self.loc] += 1

	def dec(self):
		self.array[self.loc] -= 1

	def pop(self):
		hold = self.array[self.loc]
		self.array[self.loc] = 0
		return '{0}\n'.format(hold)

	def get(self):
		return chr(self.array[self.loc])

	def put(self):
		char = input(',:')
		self.array[self.loc] = int(char) if str(char).isdigit() else ord(char)

	def left_loop(self):
		self.loop_left = self.loc
		self.looping = True

	def right_loop(self):
		self.loop_right = self.loc

	def copy(self):
		val = self.array[self.loc]
		self.array[self.loc+1] = val

def do(instruction, pointer, n):
	INSTRUCTION_MAP = {
		'>': pointer.up,
		'<': pointer.down,
		'+': pointer.inc,
		'-': pointer.dec,
		'^': pointer.pop,
		'.': pointer.get,
		',': pointer.put,
		'[': pointer.left_loop,
		']': pointer.right_loop,
		'/': pointer.copy
	}
	retr = ''
	try:
		if len(instruction) == 1:
			retr = INSTRUCTION_MAP[instruction]()
		else:
			origin = pointer.loc
			while pointer.array[origin] > 0:
				for i in instruction:
					INSTRUCTION_MAP[i]()
	except KeyError:
		pass
	except ValueError:
		retr = 'ERROR: tried to print invalid char "{0}" on instruction {1}'.format(pointer.array[pointer.loc], n)
	return retr or ''

def parse(raw):
	parsed_instructions = []
	looping = False
	loop = []
	for c in raw:
		if c in '><+-^.,':
			if not looping:
				parsed_instructions.append(c)
			if looping:
				loop.append(c)
		elif c == '[':
			looping = True
		elif c == ']':
			looping = False
			parsed_instructions.append(loop)
			loop = []
	return parsed_instructions


if __name__ == '__main__':
	import sys
	instructions = []
	with open(sys.argv[1], 'r') as file:
		instructions = parse(file.read())
	pointer = Pointer([0 for i in range(128)])
	n = 0
	for instruction in instructions:
		retr = do(instruction, pointer, n)
		if not retr == '':
			print(retr, end='')
		n += 1