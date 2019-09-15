#Jinyuan Piao
##This will help you to find equation for Eigenvalues for 3 by 3 matrices in a differential equation.
#It only works for intergers.
print("Hello, name the INTERGERS same as shown here and the type the intergets.")
print("(c1,c2,c3")
print("c4,c5,c6")
print("c7,c8,c9)")
print("After typing in all the numbers, it will give you a third power equation for finding Eigenvalues.")
CA=int(input("What is your C1?"))
CB=int(input("What is your C2?"))
CC=int(input("What is your C3?"))
CD=int(input("What is your C4?"))
CE=int(input("What is your C5?"))
CF=int(input("What is your C6?"))
CG=int(input("What is your C7?"))
CH=int(input("What is your C8?"))
CI=int(input("What is your C9?"))
TRACE=CA+CE+CI
C11=CE*CI-CH*CF
C22=CA*CI-CG*CC
C33=CA*CE-CD*CB
DET=CA*CE*CI-CA*CF*CH-CB*CD*CI+CB*CF*CG+CC*CD*CH-CC*CG*CE
print("If you see two subtract sign, treat them as a add sign please.")
print("If you see a add sign and subtract sign together, treat them as a subtract sign.")
print("The equation for finding Eigenvalues is:")
print("x^3-",TRACE,"X^2""+",C11+C22+C33,"X","-",DET)
