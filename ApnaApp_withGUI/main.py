ans=input('\n\nDo you want age specific conversation?: ')

if ans=='y':
    print('Understood, you want age specific questions')
    ch = input("Enter Age: ")
    if int(ch)>=10 and int(ch)<20:
      with open('App_1.py', 'r') as file:
          s1 = file.read()
      exec(s1)
    elif int(ch)>=20 and int(ch)<40:
      with open('App_2.py', 'r') as file:
           s2 = file.read()
      exec(s2)
    elif int(ch)>=40 and int(ch)<60:
        with open('App_3.py', 'r') as file:
            s3 = file.read()
        exec(s3)
else:
    print('Understood, you want common questions')
    with open('App.py', 'r') as file:
        s4 = file.read()
    exec(s4)
    
          
