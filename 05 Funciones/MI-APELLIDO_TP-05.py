uno = 3
dos = 7
tres = 4

if dos % 2 != 0:
    x = dos * 2
else: 
    x = dos * 3

if x % 2 == 0: 
    t = x + tres 
else: 
    t = x - tres

if t > 10:
    rf = t * uno 
else: 
    rf = t - uno
  
print(rf)