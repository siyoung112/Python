#IP address 192.168.108.11
a1,a2,a3,a4=bin(192),bin(168),bin(108),bin(11)
print(a1,a2,a3,a4,sep='.')

print('binary print{:b}'.format(192))
print('binary print{:b}'.format(168))
print('binary print{:b}'.format(108))
print('binary print{:b}'.format(11))
print('{:08b}.{:08b}.{:08b}.{:08b}'.format(192,168,108,11))
#11000000.10101000.1101100.1011

print('{4}{5}{1}{1}{2}{3}'.format('The','famine','was','servere','in','Samaria'))