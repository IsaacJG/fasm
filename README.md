Fasm
====
# Fasm is an esoteric language inspired by the [Funges](https://en.wikipedia.org/wiki/Funge#Funges)
I guess this could be called a fungeoid(?)

### How to use

* To start the interpreter: `python fasm.py`
  * If you want a larger board (array) to work with, specify the size: `python fasm.py 128`
* To run a Fasm file: `python fasm.py file`

**Note:** if you are running a file, the first line can be used to specify the board size

### Hello World!
**Here are two variations of a hello world program**
```
11
,h>,e>,l>,l>,o>, >,w>,o>,r>,l>,d<<<<<<<<<<.>.>.>.>.>.>.>.>.>.>.
,d>,l>,r>,o>,w>, >,o>,l>,l>,e>,h.<.<.<.<.<.<.<.<.<.<.
```
The first example puts all characters in "hello world" into the array, goes back to the first slot, and then progressively prints each slot.
The second example puts all characters in "hello world" into the array **in reverse**, and then regressively prints each slot

### Reference
* > go to next slot
* < go to previous slot
* ^ pop the current slot
* . return the content of the current slot
* , put the character following this instruction into the current slot

**Note:** all arithmetic instructions (+, -, *, /, %) pop the next two slots, do the operation, and put the result in the current slot (as well as prints the result)

Good luck have fun!

### License
[GPLv3](LICENSE)
