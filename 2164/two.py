n=int(input())
highest_bit=1<<(n.bit_length()-1)
print(highest_bit)

r=n-highest_bit
if n==1 or r==0:
    print(n)
else:
    print(r*2)

