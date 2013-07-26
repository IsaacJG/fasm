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

	def copy(self):
		hold = self.array[self.loc]
		self.up()
		self.array[self.loc] = hold
		self.down()

	def dump(self):
		return '{0}\n'.format(self.array)

def do_loop(loop, pointer, origin):
	retr = ''
	while pointer.array[origin] > 0:
		for i in loop:
			if type(i) is list:
				retr = do_loop(i, pointer, pointer.loc)
			else:
				retr = do(i, pointer, n)
	return retr or ''

def do(instruction, pointer, n):
	INSTRUCTION_MAP = {
		'>': pointer.up,
		'<': pointer.down,
		'+': pointer.inc,
		'-': pointer.dec,
		'^': pointer.pop,
		'.': pointer.get,
		',': pointer.put,
		'/': pointer.copy,
		'*': pointer.dump
	}
	retr = ''
	try:
		if len(instruction) == 1:
			retr = INSTRUCTION_MAP[instruction]()
		else:
			do_loop(instruction, pointer, pointer.loc)
	except KeyError:
		pass
	except ValueError:
		retr = 'ERROR: tried to print invalid char "{0}" on instruction {1}'.format(pointer.array[pointer.loc], n)
	return retr or ''

def parse(raw):
	instructions = []
	looping = False
	loop = []
	n = 0
	loops = []
	pos = 0
	for c in raw:
		if c in '><+-^.,/*':
			if not looping:
				instructions.append(c)
			else:
				if len(loops) > 0:
					loop[loops[n-1]].append(c)
				else:
					loop.append(c)
		elif c == '[':
			if not looping:
				looping = True
			else:
				loop.append([])
				pos = len(loop)-1
				loops.append(pos)
				n += 1
		elif c == ']':
			if n > 0:
				loops.pop(n-1)
				n -= 1
				if n <= 0:
					loops = []
				else:
					pos = loops[n-1]
			else:
				looping = False
				instructions.append(loop)
				loop = []
	return instructions

if __name__ == '__main__':
	import sys
	instructions = []
	with open(sys.argv[1], 'r') as file:
		instructions = parse(file.read())
	pointer = Pointer([0 for i in range(1024)])
	n = 0
	for instruction in instructions:
		retr = do(instruction, pointer, n)
		if not retr == '':
			print(retr, end='')
		n += 1