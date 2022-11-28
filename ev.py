wr=open('H:\Ev.txt','w')
wr.write(f'ev=[2984, 2348, 2069, 2204, 2418, 2037, 2092, 2495, 2487, 2827, 2305, 2650]\n')

ev= [2984, 2348, 2069, 2204, 2418, 2037, 2092, 2495, 2487, 2827, 2305, 2650]

# ev = False
# hosszu=len(ev)
# if hosszu ==12:
#     ev= True 
#     print(f'ez egy év adatsora')
# else:
#     print(f'ez nem egy év adatsora')
    
# legnagyobb = 0
# legnagyobb = ev[0]
# for maxElem in ev:
#     if maxElem > legnagyobb:
#         legnagyobb = maxElem
# print(legnagyobb)


legnagyobb = ev[0]
legkisebb = ev[0]
össz=0
hanyszor=0
for x in ev:
    össz += x
    if x >legnagyobb:
        legnagyobb= x
    elif x < legkisebb:
        legkisebb = x
    if  x > 2400:
        hanyszor +=1

legkisebb1=min(ev)
legnagyobb1=max(ev)

print(legkisebb1)
print(legnagyobb1)

wr.write(f'{legkisebb1}\n')
wr.write(f'{legnagyobb1}\n')

# legkisebb1szoveg=str(legkisebb1)

# legkisebb1hely=len(legkisebb1szoveg)

# print(legkisebb1hely+1)

# while  !=legkisebb1hely: 

# minszamlalo=0
# for legkisebb1 in ev:
#     minszamlalo=legkisebb1
    
# print(minszamlalo)    

hossz =len(ev)
ker = legnagyobb
i=0
while ev[i] != ker:
    i +=1
print(f'legnagyobb helye: {i+1}')
wr.write(f'legnagyobb helye: {i+1}\n')

hossz=len(ev)
ker = legkisebb
i=0
while ev[i] !=ker:
    i += 1
print(f'legkisebb helye: {i+1}')
wr.write(f'legkisebb helye: {i+1}\n')
wr.close()