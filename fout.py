x = 10
y = 11.4

print(f"{x:<10}|{y:>10}")
print("---------------------")
print(f"{x:<10}|{y:<10}")
print("---------------------")
print(f"{x:>10}|{y:<10}")


data = [
    ['Apple','APL',200],
    ['Google','GOOGL',200],
    ['Microsoft','MSX',200],
    ['Amazon','AMZN',200],
    ['META','FB',200],
    ['Netflix','NF',200],
    ['Apple','APL',200],
    ['Apple','APL',200],
    ['Apple','APL',200],
    
]

for i in data:
    print(f"{i[0]:<12} - {i[1]:<5} : {i[2]:>8}")
