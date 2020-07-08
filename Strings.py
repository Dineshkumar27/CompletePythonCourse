
string=input("Enter your string: ")
length=len(string)
a=0
end=length
string2=''
while a<length:
    if a==0:
        string2+=string[0].upper()
        a+=1
    elif(string[a]=='' and string[a+1]!=''):
        string2+=string[a]
        string2+=string[a+1].upper()
        a+=2
    else:
        string2+=string[a]
        a+=1
print("Actual String",string)
print("Captilalized String",string2)
'''
string="good morning have a nice day"
string2=string[0].capitalize()+string[1:]
print(string2)
'''
