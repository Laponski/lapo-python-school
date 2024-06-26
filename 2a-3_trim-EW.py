menu = """
1 - String Indexing
2 - String Slicing
3 - List Ccreation
4 - List analysis
E - Exit
"""
def voce1():
    ans = input("give me a string --> ")
   
    try:
        ans1 = int(input("give me an integer number --> "))
    except ValueError:
        while True:
            try:
                ans1 = int(input("give me an integer number --> "))
                break
            except ValueError:
                print("please give me an integer number")
                continue
   
    if ans1 < len(ans):
        print("the character at position", ans1, "of", ans, "is:", ans[ans1])
    else:
        print("index is out o range try again")    
def voce2():
    ans = input("give me a string --> ")
    try:
        ans1 = int(input("give me the first index for slicing --> "))
    except ValueError:
        while True:
            try:
                ans1 = int(input("give me the first index for slicing --> "))
                break
            except ValueError:
                print("please give me an integer number")
                continue
    try:
        ans2 = int(input("give me the last index for slicing (if index is out of range it will get the last)--> "))
    except ValueError:
        while True:
            try:
                ans2 = int(input("give me the last index for slicing --> "))
                break
            except ValueError:
                print("please give me an integer number")
                continue
    if ans1 > ans2:
        print("the last index must be bigger than the fist one, try again in the menù")
    else:
        print("The slicing of the numbers you have given is:", ans[ans1:ans2 + 1])
def ListAnalysisA(k):
   
    x = input("give me a character --> ")
    s = []
   
    for i in k:
        if x in i:
            s.append(i)
        else:
            pass
    print(s)


while True:
    print(menu)
    ans = input("choose from the menù -->")
    while ans.upper() != "E":
       
        if ans == "1":
            voce1()
            break
        if ans == "2":
            voce2()
            break
        if ans == "3":
            u = []
            y = ""
   
            while y.upper() != "STOP":
                y = input("give me a word to be put in a list--> ")
                if y.upper() == "STOP":
                    break
                else:
                    u.append(y)
            print(u)
            break
        if ans == "4":
            try:
                ListAnalysisA(u)
            except NameError:
                print("you should run before voice 3")
            break
        else:
            print("! try again with a valid input !")
            break
    if ans.upper() == "E":
        break