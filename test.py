n = int(input())

while n> 0:
  num_a = str(input())
  num_b = str(input())
  N = 0-len(num_b)
  for b in range(0, len(num_b)):
    if num_a[N] != num_b[N]:
        print("nao encaixa")
        b = len(num_b)
    elif b == len(num_b)-1:
        print("encaixa")
        b = len(num_b)
    
    N+=1

  n-=1