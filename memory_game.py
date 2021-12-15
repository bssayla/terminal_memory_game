
import random
import time


def print_table(guesses:list,guessed_or_not:dict)->None:
    for i in range(0,len(guesses)):
        if not i%3:
            print()
        if guessed_or_not[guesses[i]]:
            print(guesses[i], end="\t")
        else:
            print("#", end="\t")
            
    print()
        
    


def coundown()->None:
    for i in range(9,-1,-1):
        print(f"\rstill {i%10} secondes for begin",end="")
        time.sleep(1)
    print()
    print("let' GOOOO")
        


def main()->None:
    guesses = [x for x in range(1,7)]*2
    random.shuffle(guesses)

    guessed_or_not = {j:False for j in guesses}
    #print the sulution for 10 secs
    print("focus and remember the numbers")
    for i in range(0,12,3):
        print(f"\r{(i//3)+1} line elements are : {guesses[i:i+3]}",end="")
        time.sleep(3)
    print()
    coundown()

    while True:
        print_table(guesses,guessed_or_not)
        x = int(input("Enter x beetwen 1 and 12: "))
        y = int(input("Enter y beetween 1 and 12: "))
        #break the programme
        if (not x) or (not y ):
            print("we out!!")
            break
        #check if its a number or not
        while 0>x or x>12 or y<0 or y>12:
            print("y or x is out of the range try again")
            x = int(input("Enter x beetwen 1 and 12: "))
            y = int(input("Enter y beetween 1 and 12: "))
        
        
        
        if guesses[x-1]==guesses[y-1] and y != x:
            guessed_or_not[guesses[x-1]] = True
        else:
            print("try again")


        #end after guessing all 
        if all(guessed_or_not[i]for i in range(1,7)):
            print("Congrats you winn!!!!!")
            break


if __name__ == "__main__":
    main()





