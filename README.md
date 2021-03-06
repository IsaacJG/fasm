Fasm
====
# Fasm is an esoteric language inspired by [BF](https://en.wikipedia.org/wiki/Brainfuck)
This is essentially a BF clone, with some minor differences (I think, don't actually know BF so yeah), and some major additions.

### How to use

`python fasm.py file`

### Hello World!
**Here is an annotated example of a hello world program**
```
++++++++++ set counter to 10
[
	d 		> ++++++++++	set the d slot to 100
	e		> ++++++++++	initialize the e slot with 100
	h		> ++++++++++	initialize the h slot with 100
	l		> +++++++++++	initialize the l slot with 110
	o		> +++++++++++	initialize the o slot with 110
	r		> +++++++++++	initialize the r slot with 110
	w		> ++++++++++++	initialize the w slot with 120
	space 	> +++			initialize the space slot with 30
 	<<<<<<<< -				decrement counter
]
>>	+		set e slot to 101
>	++++	set h slot to 104
>	--		set l slot to 108
>	+		set o slot to 111
>	++++	set r slot to 114
>	-		set w slot to 119
>	++		set space slot to 32
<<<<<.	print "h"
<.		print "e"
>>..	print "ll"
>.		print "o"
>>>.	print " "
<.		print "w"
<<.		print "o"
>.		print "r"
<<.		print "l"
<<<.	print "d"
```
This example uses a loop to get ballpark values for the characters, then goes through and makes any changes necessary to the values, then goes to the various slots to print each letter at the desired time. Since all characters that are not part of the instruction set (See the [Reference](#reference) section) are ignored, this can be minified into the following program:
```
++++++++++[>++++++++++>++++++++++>++++++++++>+++++++++++>+++++++++++>+++++++++++>++++++++++++>+++<<<<<<<<-]>>+>++++>-->+>++++>->++<<<<<.<.>>..>.>>>.<.<<.>.<<.<<<.
```
Exact same thing, just much harder to read.

### Reference
See the [official Fasm language spec](https://github.com/IsaacJG/fasm-spec#fasm-specification)

Good luck have fun!

### Implementation Issues
* Only supports 2 nested loops

### License
[GPLv3](LICENSE)
