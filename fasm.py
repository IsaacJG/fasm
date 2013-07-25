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
		return chr(hold)

	def get(self):
		return self.array[self.loc]

	def put(self):
		char = input(',:')
		self.array[self.loc] = int(char) if str(char).isdigit() else ord(char)

	def left_loop(self):
		self.loop_left = self.loc
		self.looping = True

	def right_loop(self):
		self.loop_right = self.loc

def do(instruction, pointer):
	INSTRUCTION_MAP = {
		'>': pointer.up,
		'<': pointer.down,
		'+': pointer.inc,
		'-': pointer.dec,
		'^': pointer.pop,
		'.': pointer.get,
		',': pointer.put,
		'[': pointer.left_loop,
		']': pointer.right_loop
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
	for instruction in instructions:
		retr = do(instruction, pointer)
		if not retr == '':
			print(retr)