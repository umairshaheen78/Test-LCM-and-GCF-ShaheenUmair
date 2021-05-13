import time

def compute_lcm(x, y):

   # choose the greater number
	if x > y:
		greater = x
	else:
		greater = y

	while(True):
		if((greater % x == 0) and (greater % y == 0)):
			lcm = greater
			break
		greater += 1

	return lcm

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print("The L.C.M. is", compute_lcm(num1, num2))
print("Next Game!\n")
time.sleep(1)

def compute_gcf(x,y):
    if x > y:
        x = int(input("Enter a number so I can find the GCF: "))
        y = int(input("Enter another number so I can find the GCF: "))
    while x > 1:
        if x % x == 0 and y % x == 0:
            break
        x -= 1
    print ("The GCF is" ,str(x))

compute_gcf(8, 22)