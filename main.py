def check_sym(string):
    n=len(string)
    flag=0
    if n%2:
        mid=n//2+1
    else:
        mid= n//2
    start=0
    end= mid
    while(start <mid and end<n):
        if(string[start]== string[end]):
            start= start+1
            end= end+1
        else:
            flag=1
            break
    if flag==0:
        print("symmetrical")
    else:
        print("not symmetrical")


s=input('Please enter a number: ')
check_sym(s)

