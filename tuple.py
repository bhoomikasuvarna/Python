t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
t2 = (11, 13, 15)
a=[]
# a) Print another tuple whose values are even numbers in the given tuple.
for i in t1:
  if i%2==0:
    a.append(i)
t=tuple(a)
print("Tuple of even numbers:",t)


# b) Concatenate a tuple t2={11, 13, 15} with t1.
t3 = t1 + t2
print("Concatenated tuple:", t3)


# c) Return maximum and minimum value from this tuple.
print("Maximum value:", max(t3))
print("Minimum value:", min(t3))
