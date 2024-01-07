num=27
flag=false
if num==1
 print(num,"is not a prime number")
elif num>1 
    for(i in range(2,num))
        if(num%i==0)
            flag=True
            break
        if flag:
            print("{0} is not a prime number".format(num))
        else:
            print("{0} is a prime number".format(num))
	
		
