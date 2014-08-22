Program to demonstrate students randomly selecting a station to visit

In a random order, students choose a station they haven't visited yet.
If all such stations are full, the student checks if any student at any
of those stations can swap to another station.  If not, the program
bails out and prints the ending state. (Students do not attempt swaps
of length greater than one.)

Tentative result: the last round usually (if not always) ends up with
a student unable to visit their last station.

Inspired by a real classroom planning activity; trying to figure out 
whether this activity would end badly (difficulty with who visits 
which station in the last couple rounds). So far, it looks like random
station selection usually ends in disaster.

Simple workaround: rotate stations clockwise. But that's not nearly 
as computationally interesting. ;-)
