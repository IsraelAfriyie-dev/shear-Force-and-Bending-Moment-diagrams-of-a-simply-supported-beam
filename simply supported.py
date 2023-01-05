
load_type = input('UDL or Point_load: ')
if  load_type == 'Point_load':
     load_applied = int(input('Enter the force applied: '))
     AO=int(input('Enter Distance AO: '))
     OB=int(input('Enter Distance OB: '))
     AB = AO+OB
     VB= (load_applied*AO)/AB
     VA=load_applied-VB
     print('Vertical force B=',str(VB)+'KN')
     print('Vertical force A=',str(VA)+'KN')
     import matplotlib.pyplot as plt
     x=[0,OB,OB,AB]
     y=[VA,VA,-VB,-VB]
     plt.plot(x,y,'--')
     import matplotlib.pyplot as plot
     X=[0,AB/2,AB]
     Y=[0,(load_applied*AB/4),0]
     plot.plot(X,Y)
     import matplotlib.pyplot as plt
     x = [0,AB]
     Y = [0,0]
     plt.plot(x,Y)
     import matplotlib.pyplot as plt
     x =[0,0]
     y=[VA,0]
     plt.plot(x,y,'--')
     import matplotlib.pyplot as plt
     x = [AB,AB]
     y=[0,-VB]
     plt.plot(x,y, '--')
else:
      load_applied = int(input('Enter the force applied: '))
      AB = int(input('Enter the distance AB: '))
      VB = (load_applied * AB*(AB/2)) / AB
      VA = (load_applied *AB) - VB
      print('Vertical force B=', str(VB) + 'KN')
      print('Vertical force A=', str(VA) + 'KN')


