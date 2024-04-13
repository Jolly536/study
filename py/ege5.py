results = []
for n in range (1, 1000):
    n_bin = bin(n)[2:]
    if(n % 2 == 0):
        n_bin = '1' + n_bin + '00'
    else: 
        n_int = int(n_bin)
        n_int = n_int + n_int
        n_bin2 = bin(n_int)[2:]
        n_bin += n_bin2
    r = int(n_bin, 2)
    if(r > 190):
        results.append(n)
print(results)