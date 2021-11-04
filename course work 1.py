method=str(input("please choose the method you want bbs , file , trn :"))
#true number generator with time
if method=="trn":
    import time
    seconds = time.time()
    def seedBBS(initVal):
     global rand
     rand = initVal
    def bbs():
     p = 45503
     q = 17387
     m = p*q
     global rand
     rand = (rand**2) % m
     return rand
    seedBBS(seconds)
    z=int((input("enter the number of outputs needed ")))
    for i in range(z):
     print(int(bbs()))
elif method=="bbs":
#pseudo number generator with the user input 
    def seedBBS(initVal):
     global rand
     rand = initVal
    def bbs():
     p = 45503
     q = 17387
     m = p*q
     global rand
     rand = (rand**2) % m
     return rand
    seedBBS(int(input(" enter a starting value ")))
    z=int((input("enter the number of outputs needed ")))
    for i in range(z):
     print(int(bbs()))
elif method=="file":
#true number generator with the input taken from another file
    file_name =str(input("please enter your file name with the file extension:"))
    seed=0
    def file_window():
     global file_name
     file_name=seed.askopenfilename() 
    def seedBBS(initVal):
     global rand
     rand = initVal
    def bbs():
     p = 45503
     q = 17387
     m = p*q
     global rand
     rand = (rand**2) % m
     return rand
    with open(file_name,"r")as file:
     seedBBS(int(file.readline()))
    z=int((input("enter the number of outputs needed ")))
    for i in range(z):
     print(int(bbs()))
else:
    print("try again ")

    

