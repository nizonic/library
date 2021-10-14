#You are completely free to change this variables to check your algorithm.
num1 = 6 
num2 = 28

#Function to check whether two numbers are friendly pairs or not.
def isFriendlyPair():
    if num1 == num2 or type(num1) != int or type(num2) != int or num1 <= 0 or num2 <= 0:
        return "Invalid"
    
    sumdiv1 = 0
    sumdiv2 = 0
    for x in range(1,num1 + 1):
        if num1 % x == 0:
            sumdiv1 += x
    for x in range(1,num2 + 1):
        if num2 % x == 0:
            sumdiv2 += x
    #You need to complete this function.
    #You need to return a boolean variable . If num1 and num2 are friendly pairs return True. 
    #If they are not return False. 
    #The numbers must be valid according to description before determining friendly parity situations. 
    #Return "Invalid" if they are not valid.
    return sumdiv1/num1 == sumdiv2/num2

#This line prints your method's return so that you can check your output.
print(isFriendlyPair())