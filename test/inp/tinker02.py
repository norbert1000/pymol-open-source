# python

# minimization test

from chempy import io
from chempy import tinker
from chempy import protein
from chempy.tinker.state import State
from chempy import feedback

import os

feedback['atoms'] = 1

m = io.pdb.fromFile("dat/pept.pdb")

m = protein.generate(m)

s = State()

s.echo = 0

s.load_model(m)

print " test: atom 0 position:",m.atom[0].coord
s.minimize(gradient=1.0,max_iter=100)

print " test: energy is ->",s.energy

for a in s.summary:
   print a
   
print " test: atom 0 position:",m.atom[0].coord

os.system("touch .no_fail tinker_*")
os.system("/bin/rm .no_fail tinker_*")

