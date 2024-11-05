#print function
print("Hello world")


print("Hello world."+" "+"This is Prayag.")
#OR
print("Hello world."+" This is Prayag.")
#OR
print("Hello world. "+"This is Prayag.")


#typecasting
age=20
print("Your age is "+ str(age))   #Two different datatypes cannot be concatinated, 
                                 #so integer a is typecaasted to string type.
#OR
print(f"Your age is {age}")



#typechecking: by using type() function
a=str(20)
b=30
c=float(40)
d="Prayag"
e='5'
f=int(6.33)

print(a,b,c,d,e,f)
print(type(a), type(b), type(c), type(d), type(e),type(f))



#round() function
a=50.554455445544
print(a, round(a,3), round(a,1), round(a))  #round function with no number specified 
                                            #rounds to nearest integer

    
#input() function
a=input("what is your name?")
print('I love you '+a +'!!')
print('Hello Mr.'+ input("what is your name?"))





#NOTE:
b=6
c=5
print(b/c, b//c)  # '//' is used if we want only integer
print(b%c)        #prints remainder

