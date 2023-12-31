n = int(input("Enter the number of rows"))
m = n*3
pat = 3
for i in range(n):
  if i == (n // 2):
    for j in range(m):
      if (j==(m // 2)-3):
        print("WELCOME",end="")
      if(j>(m // 2)-3 and j<(m // 2)+5):
        continue
      else:
        print("-",end="")
    print("")
  elif i< (n//2):
    for j in range(m):
      dash = (m - pat) / 2
      if (j < dash or j >= dash + pat):
        print("-", end="")
      elif(j==dash):
        for k in range(pat//3):
          print(".|.", end="")
      else:
          continue
    pat = pat + (2 * 3)
    print("")
  else:
    pat -= 6
    for j in range(m):
        dash = (m - pat) // 2
        if (j < dash) or (j >= dash + pat):
            print("-", end="")
        elif j == dash:
            for k in range(pat // 3):
                print(".|.", end="")
            dash += (pat // 3) * 2
        else:
            continue
    print("")

