def solve(x, func):
    if (x.find("-") == 0):
        x = x.replace("-", "F", 1)
        print(x)
    for i in x:  
        if i == "*" and func == "muldiv":
            z = 0
            for j in x[x.index("*")-1::-1]:
                if (j.isdigit() or j == "."):
                    z += 1
                else:                   
                    break           
            number1_lenght = z
            x = x.replace("*", "M", 1)
            y = 1
            for j in x[x.index("M")+1:]:
                if (j.isdigit() or j == "."):
                    y += 1
                else:                   
                    break
            number2_lenght = y
            print(x[x.index("M")-number1_lenght:x.index("M")+number2_lenght])
            summa = str(round(float(x[x.index("M")-number1_lenght:x.index("M")]) * float(x[x.index("M")+1:x.index("M")+number2_lenght]),4))
            print(summa)
            x = x.replace(x[x.index("M")-number1_lenght:x.index("M")+number2_lenght], summa, 1)
            return x    
        
        if i == "/" and func == "muldiv":
            z = 0
            for j in x[x.index("/")-1::-1]:
                if (j.isdigit() or j == "."):
                    z += 1
                else:                   
                    break           
            number1_lenght = z
            x = x.replace("/", "D", 1)
            y = 1
            for j in x[x.index("D")+1:]:
                if (j.isdigit() or j == "."):
                    y += 1
                else:                   
                    break
            number2_lenght = y
            print(x[x.index("D")-number1_lenght:x.index("D")+number2_lenght])
            summa = str(round(float(x[x.index("D")-number1_lenght:x.index("D")]) / float(x[x.index("D")+1:x.index("D")+number2_lenght]),4))
            print(summa)
            x = x.replace(x[x.index("D")-number1_lenght:x.index("D")+number2_lenght], summa, 1)
            return x 
        
        if i == "+" and func == "addsub":
            z = 0
            for j in x[x.index("+")-1::-1]:
                if (j.isdigit() or j == "."):
                    z += 1
                else:                   
                    break           
            number1_lenght = z
            x = x.replace("+", "A", 1)
            y = 1
            for j in x[x.index("A")+1:]:
                if (j.isdigit() or j == "."):
                    y += 1
                else:                   
                    break
            number2_lenght = y
            if (x.find("F") != -1):
                print(x[x.index("A")-number1_lenght:x.index("A")+number2_lenght])
                summa = str(float(x[x.index("A")-number1_lenght:x.index("A")]) - float(x[x.index("A")+1:x.index("A")+number2_lenght]))    
            else:
                print(x[x.index("A")-number1_lenght:x.index("A")+number2_lenght])
                summa = str(float(x[x.index("A")-number1_lenght:x.index("A")]) + float(x[x.index("A")+1:x.index("A")+number2_lenght]))
            print(summa)
            x = x.replace(x[x.index("A")-number1_lenght:x.index("A")+number2_lenght], summa, 1)
            x = x.replace("F", "-", 1)
            return x 
        
        if i == "-" and func == "addsub":
            z = 0
            for j in x[x.index("-")-1::-1]:
                if (j.isdigit() or j == "."):
                    z += 1
                else:                   
                    break           
            number1_lenght = z
            x = x.replace("-", "S", 1)
            y = 1
            for j in x[x.index("S")+1:]:
                if (j.isdigit() or j == "."):
                    y += 1
                else:                   
                    break
            number2_lenght = y
            if (x.find("F") != -1):              
                print(x[x.index("S")-number1_lenght:x.index("S")+number2_lenght])
                summa = str(float(x[x.index("S")-number1_lenght:x.index("S")]) + float(x[x.index("S")+1:x.index("S")+number2_lenght]))           
            else:
                print(x[x.index("S")-number1_lenght:x.index("S")+number2_lenght])
                summa = str(float(x[x.index("S")-number1_lenght:x.index("S")]) - float(x[x.index("S")+1:x.index("S")+number2_lenght]))
            print(summa)
            x = x.replace(x[x.index("S")-number1_lenght:x.index("S")+number2_lenght], summa, 1)         
            x = x.replace("F", "-", 1)           
            return x        

while True:    
    x = input("Input your expression: ")    
    
    x = x.replace(" ", "")
    x = x.replace("=", "") 
    
    if (x == "exit"):
        break;        
        
    while (x.find("*") != -1 or x.find("/") != -1):
        x = solve(x, "muldiv")
        
    while (x.find("+") != -1 or x.find("-",1) != -1):
        x = solve(x, "addsub")       
    
    x = x + " "    
    
    if (x.find(".0 ") != -1):
        x = x.replace(".0 ", "", 1)
        
    print(""); print("Your Answer: " + x)
    print("-------------------------- ")