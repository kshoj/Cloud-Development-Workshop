while True:
  request = int(input("for adding a student enter 1 \nfor searching for a student enter 2 \nfor aborting enter 3: \n"))
  L=[['john', 50], ['tim', 54], ['marie', 58]]
  if request==1:
    name = str(input("enter the student's name: "))
    grade = int(input("enter the student's grade: "))
    status= [name, grade]
    L.append (status)
    print (L)

  if request==2:
    name2 = str(input("enter the student's name: "))
    for i in L:
      if name2 in i:
        print (i)

  if request==3:
    break

  if not(request in range (1,4)):
    print('invalid input')
