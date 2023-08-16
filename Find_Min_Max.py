largest=0
smallest=0
while True:
    lel=input('Number only:')
    if lel=='done':
        break
    try:
        if float(lel)>=float(largest):
            largest=lel
        if smallest >=float(lel):
                 smallest=lel
    except:
        print('wrong input')
        continue

print('The largest number is',largest)
print('The smallest number is', smallest)
#Already have the way to find the maximum but idk what can i put in smallest to be replaced by the minimum
