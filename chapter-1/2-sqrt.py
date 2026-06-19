# 𝑛𝑒𝑤_𝑔𝑢𝑒𝑠𝑠 = 1/2* (𝑜𝑙𝑑_𝑔𝑢𝑒𝑠𝑠 + 𝑛 / 𝑜𝑙𝑑_𝑔𝑢𝑒𝑠𝑠)

def sqrt(nbr):
    if nbr < 0:
        raise ValueError("The Number passed must be positive")
    
    root = nbr / 2 # initial  guess 
    for i in range(100):
        root = 0.5 * (root + nbr / root)
    return root

print(sqrt(-9))