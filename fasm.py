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

global cout

class Cursor:
	def __init__(self, array):
		self.loc = 0
		self.array = array

def up(cursor):
	cursor.loc += 1
	if cursor.loc >= len(cursor.array):
		cursor.loc = 0

def down(cursor):
	cursor.loc -= 1
	if cursor.loc < 0:
		cursor.loc = len(cursor.array)-1

def inc(cursor):
	cursor.array[cursor.loc] += 1

def dec(cursor):
	cursor.array[cursor.loc] -= 1

def pop(cursor):
	hold = cursor.array[cursor.loc]
	cursor.array[cursor.loc] = 0
	return '{0}\n'.format(hold)

def get(cursor):
	return chr(cursor.array[cursor.loc]) if cout else cursor.array[cursor.loc]

def put(cursor):
	char = input(',:')
	cursor.array[cursor.loc] = int(char) if str(char).isdigit() else ord(char)

def copyup(cursor):
	hold = cursor.array[cursor.loc]
	up(cursor)
	cursor.array[cursor.loc] = hold
	down(cursor)

def copydown(cursor):
	hold = cursor.array[cursor.loc]
	down(cursor)
	cursor.array[cursor.loc] = hold
	up(cursor)

def dump(cursor):
	return '{0}\n'.format(cursor.array)

def togglecout():
	cout = not cout

def do_loop(loop, cursor, origin):
	retr = ''
	while cursor.array[origin] > 0:
		for i in loop:
			if type(i) is list:
				retr = do_loop(i, cursor, cursor.loc)
			else:
				retr = do(i, cursor, n)
	return retr or ''

def do(instruction, cursor, n):
	INSTRUCTION_MAP = {
		'>': up,
		'<': down,
		'+': inc,
		'-': dec,
		'^': pop,
		'.': get,
		',': put,
		'/': copyup,
		'\\': copydown,
		'*': dump,
		'~': togglecout
	}
	retr = ''
	try:
		if len(instruction) == 1:
			retr = INSTRUCTION_MAP[instruction](cursor)
		else:
			do_loop(instruction, cursor, cursor.loc)
	except KeyError:
		pass
	except ValueError:
		retr = 'ERROR: tried to print invalid char "{0}" on instruction {1}'.format(cursor.array[cursor.loc], n)
	return retr or ''

def parse(raw):
	instructions = list(raw)
	i = 0
	while i < len(instructions):
		if instructions[i] not in '><+-^.,/\\*~[]':
			instructions.pop(i)
		else:
			instructions[i] = '\'{0}\''.format(instructions[i])
			if '[' in instructions[i] or ']' in instructions[i]:
				instructions[i] = instructions[i].replace('\'', '')
			i += 1
	instructions = ''.join(instructions).replace('\'\'', '\',\'').replace('\'[\'', '\', [\'').replace('\']\'', '\'], \'')
	instructions = instructions.replace('\'[', '\', [').replace(']\'', '], \'')
	instructions = '[{0}]'.format(instructions)
	return eval(instructions)

if __name__ == '__main__':
	import sys
	with open(sys.argv[1], 'r') as file:
		raw = file.read()
		instructions = parse(raw)
	cursor = Cursor([0 for i in range(1024)])
	cout = True
	n = 0
	for instruction in instructions:
		retr = do(instruction, cursor, n)
		if not retr == '':
			print(retr, end='')
		n += 1