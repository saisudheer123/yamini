def isPowerOfTwo (x):
  return (x and (not(x & (x - 1))) )
n=int(input())
if(isPowerOfTwo(n)):
    print("Yes")
else:
    print("no")
