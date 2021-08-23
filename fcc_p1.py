def arithmetic_arranger(problems, optional = False):
    maxlength = 0
    temp = []
    arranged_problemsTemp = []
    dist = []
    add_sub = []
    answers = []
    numbers = "0123456789"

    class Error(Exception):
        pass
    
    if len(problems) > 5:
        return "Error: Too many problems."
    
    
        
    for item in problems:
        if "*" in item or "/" in item or "//" in item or "%" in item:
            return "Error: Operator must be '+' or '-'."

    for item in problems:
        for num in item:
            if num not in numbers:
                if num != "+":
                    
                    if num != "-":
                        if num != " ":
                            return "Error: Numbers must only contain digits."
                

    for item in problems:
        if "+" in item:
            maxlength = 0
            temp = item.split("+")
            temp[0] = temp[0].rstrip()
            temp[1] = temp[1].lstrip()
            add_sub.append("+")
            answerTemp = int(temp[0]) + int(temp[1])
            answers.append(str(answerTemp))
            for item in temp:
                if len(item) > maxlength:
                    maxlength = len(item)
    
        if "-" in item:
            maxlength = 0
            temp = item.split("-")
            temp[0] = temp[0].rstrip()
            temp[1] = temp[1].lstrip()
            add_sub.append("-")
            answerTemp = int(temp[0]) - int(temp[1])
            answers.append(str(answerTemp))
            for item in temp:
                if len(item) > maxlength:
                    maxlength = len(item)
            
        arranged_problemsTemp.append(temp[0])
        arranged_problemsTemp.append(temp[1])
        dist.append(maxlength+2)
        
    for item in arranged_problemsTemp:
        if len(item) > 4:
            return "Error: Numbers cannot be more than four digits."
            
    
    
    disCount = 0
    part1 = ""
    for num in range(len(arranged_problemsTemp)):
        if num % 2 == 0:
            if num != arranged_problemsTemp[-1] or num != arranged_problemsTemp[-2]:
                part1 += (" "*(dist[disCount]-len(arranged_problemsTemp[num])) + arranged_problemsTemp[num] + "    ")
                disCount += 1
            else:
                part1 += (" "*(dist[disCount]-len(arranged_problemsTemp[num])) + arranged_problemsTemp[num])

        
    count = 0
    part2 = ""
    for num in range(len(arranged_problemsTemp)):
        if num % 2 != 0:
            if num != arranged_problemsTemp[-1] or num != arranged_problemsTemp[-2]:
                part2 += (add_sub[count]+ " "*(dist[count]-len(arranged_problemsTemp[num])-1) + arranged_problemsTemp[num]+"    ")
                count += 1
            else:
                part2 += (add_sub[count]+ " "*(dist[count]-len(arranged_problemsTemp[num])-1) + arranged_problemsTemp[num])

    
    part3 = ""
    for num in range(len(dist)):
        part3 += ("-"*(dist[num]) + "    ")
    

    answersTrue = ""
    for num in range(len(answers)):
        if num != answers[-1]:
            answersTrue += (" "*(dist[num]-len(answers[num]))+answers[num] + "    ")
        else:
            answersTrue += (" "*(dist[num]-len(answers[num]))+answers[num])

    
    if optional == True:
        arranged_problems = part1+'\n'+part2+'\n'+part3+'\n'+answersTrue
    else:
        arranged_problems = part1+'\n'+part2+'\n'+part3
        
    return arranged_problems

print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True))




