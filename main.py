import re

def arithmetic_arranger(array,display):

    if display==True:
        x=0
        firstnumstatement=""
        operatorstatement=""
        secondnumstatement=""
        totalstatement=""
        dashesstatement =""


        size = len (array)
        print ("Number of problems:",size)
        if size>5:
            return "Error: Too many problems."

        while x<size:
            iter = (array[x])
            split=(re.split("\s",iter))
            firstnum =int(split[0])
            operator = split[1]
            secondnum = int(split[2])

            if operator =="+":
                total = firstnum+secondnum
            elif operator =="-":
                total =firstnum-secondnum
            else:
                return ("Operator must be '+' or '-'.`")


            strFirstnum = str(firstnum)
            strOperator = str(operator)
            strSecondNum= str(secondnum)
            secondline = strOperator+strSecondNum
            strTotal = str(total)

            firstnumstatement = firstnumstatement+strFirstnum.rjust(6)+"  "
            secondnumstatement=secondnumstatement.rjust(1) +secondline.rjust(6)+ "  "
            totalstatement = totalstatement+strTotal.rjust(7)+" "



            if len(strFirstnum)>len(strSecondNum):
                largest = len(strFirstnum)
            else:
                largest = len (strSecondNum)

            dashesstatement = dashesstatement+ ("-"*(largest+1)).rjust(7)+" "

            x=x+1





        return " "+firstnumstatement+'\n'+secondnumstatement+'\n'+dashesstatement+'\n'+totalstatement
    else:
        return " "


print (arithmetic_arranger(["3 + 2","45 - 130","1299 + 121","456 + 56","67 - 67"],True))
