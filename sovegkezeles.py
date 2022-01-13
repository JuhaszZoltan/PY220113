szoveg = 'cipőfűző'

for c in szoveg:
    print(c, end=' ')
print('\n-------------')
for c in szoveg:
    print(c)
print('\n-------------')
szo = input('írj be valamit: ')

#            0123456
kisbetuk  = 'abcdefghijklmnopqrstuvwxyz'
nagybetuk = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 0 1 2 3
#'c i c a' len = 4
# i = 4

for c in szo:
    i = 0
    while i < len(kisbetuk) and c != kisbetuk[i]:
        i += 1
    if i < len(kisbetuk):
        print(nagybetuk[i], end='\0')
    else: print('#', end ='\0')
