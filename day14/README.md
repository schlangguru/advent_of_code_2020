# Part 01:

Bitmask to overwrite with 1s:
mask: 0011
val: 1010

---

or: 1011

Keep the 1s and change all 0s and Xs to 0s

Bitmask to overwrite with 0s:
mask: 0011
val: 1010

---

and: 0010

Keep the 0s and change all 1s and Xs to 1s

# Part 02:

Bitmask to 0s unchanged and 1s overwrite:
mask 0011
val: 1010

---

or: 1011

Bitmask to 'float'
mask 00
mask 01
mask 10
mask 11
val: 00

---

xor: 00
xor: 01
xor: 10
xor: 11

Create mask for every combination of 01s in X. -> XOR with val.
