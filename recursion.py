def sample(x):
    if x == 0 or x == 1:
       return 1 
    else: 
       return sample(x - 1) + sample(x - 2 )

print sample(6)
