def find_solution():
  f = open("day1/input.txt", "r")
  data = f.read()
  txt = data.split()
  results = list(map(int, txt))
  print(results)
  print(len(results))

  for i in range(len(results)):
    for k in range(i+1,len(results)):
      for j in range(k+1,len(results)):
        check = results[i]+results[k]+results[j]
        if check == 2020:
          a = results[i]
          b = results[k]
          c = results[j]
          return [a,b,c]

sol = find_solution()    
print(sol, sol[0]*sol[1]*sol[2])