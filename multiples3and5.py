
def multiples3and5(number):
    total = 0
    for i in range(number):
       if i%3 == 0 or i%5 == 0:
           total+=i
    return total

print(multiples3and5(19564))