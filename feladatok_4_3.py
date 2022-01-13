szo = input('írj be valamit: ')

# 0 1 2 3
# z o l i

# 3 2 1 0
# i l o z

# len = 4
# 0 1 2 3
for i in range(len(szo)):
    print(szo[len(szo) - 1 - i], end='\0')
print('\n----------')

for i in range(len(szo) -1, -1, -1):
    print(szo[i], end='\0')
print('\n----------')

ki = len(szo) - 1
for x in range(len(szo)):
    print(szo[ki], end='\0')
    ki -= 1