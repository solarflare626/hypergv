import os
import sys

table = []
isHGV = True
fails = 0
isError = False
def main():
    '''
        open file and transform data to table
    '''
    global isError
    global table
    file = open('data.txt','r')
    for line in file:
        # remove '\n' at the end of line
        line = line.replace(' ','')
        line = line.replace('\n','')
        if(line != ""):
            row = list(eval(line))
            table.append(row)


    file.close()
    
    print("Data: ")
    for row in table:
        print(row)

        
    '''
        Input
    '''

    equation = input("Enter equation: ")
    hold = equation.split('>>')
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("------>Simplifying first part: {}".format(hold[0]))
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    first = simplify(hold[0]);
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("------>Simplifying second part:  {}".format(hold[1]))
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    second = simplify(hold[1]);

    print("\n\n\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("------>Solving {} >> {}".format(first,second))
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n\n\n")
    #print("input: ",eval(hold[0]).union(eval('{5,6}')))
    solve(first,second)


def simplify(data):
    print("------------------------------------------->")
    print("--->Simplifying: ", data)
    print("------------------------------------------->")
    global table
    global isError
    data = str(data)
    temp = None
    try:
        temp = eval(data)
        
        #remove [] if not necessary
        if type(temp) is list:
            temp = str(data)
            temp = temp.replace('[','').replace(']','')
            simplify(temp)

        return temp  
    except :
        if(type(data) is str):
            if '[' in data:
                start = data.find('[')
                index = start+1
                buffer = 0;
                while index < len(data):
                    if(data[index] == '['):
                        buffer+=1
                    elif(data[index] == ']'):
                        if(buffer == 0):
                            substring = data[start+1:index]
                            substring = simplify(substring)

                            data = data[:start] + str(substring) + data[index+1:]
                            return simplify(data)
                        else:
                            buffer -=1
                    index += 1
            elif '(' in data:
                start = data.find('(')
                index = start+1
                buffer = 0;
                while index < len(data):
                    if(data[index] == '('):
                        buffer+=1
                    elif(data[index] == ')'):
                        if(buffer == 0):
                            substring = data[start+1:index]
                            substring = simplify(substring)

                            data = data[:start] + str(substring) + data[index+1:]
                            return simplify(data)
                        else:
                            buffer -=1
                    index += 1
                    
            elif '@' in data:
                first = set()
                hold_set = set()
                temp = data.split("@")
                i = 0
                #print("Temp: ", temp)
                for x in temp:
                    x = eval(x)
                    if(type(x) is not set):
                        x = {x}

                    #print(x)
                    #print("x type: ", type(x))
                    if i ==0:
                        first = x
                        #print("First :", first)
                    else:
                        print("-------------------------------------------")
                        print("Processing {} @ {}".format(first,x))
                        first = list(first)
                        x = list(x)
                        #print(first)
                        for index_first in first:
                            for index_second in x:
                                print("--->")
                                table_set = table[index_first][index_second]
                                print("Set of {} @ {} : {}".format(index_first,index_second,table_set))
                                hold_set = hold_set.union(table_set)
                                print("--->")
                        print("-------------------------------------------")
                        print("------------------------------------------->")
                        first = hold_set
                        print("--->Result of Union: ", hold_set)
                        print("------------------------------------------->")
                        
                    i += 1
                
                return hold_set

        else:
            isError = True
            end()

def check(first,second):
    global isHGV
    global isError
    global fails
    data = table[first][second]
    print("-------------------------------------------")
    print("Checking {} - {}".format(first,second))
    print("Data: {}".format(data))
    
    print("Checking if {0,1} is a subset of data...")
    if({0,1}.issubset(data)):
        print("check passed")
        print("-------------------------------------------")
    else:
        isHGV = False
        print("check failed")
        print("-------------------------------------------")
        fails += 1

def solve(first,second):
    global isError
    if(type(first) is int):
        if(type(second) is int):
            check(first,second)
        elif(type(second) is set):
            for i in second:
                check(first,i)
    elif(type(first) is set):
        if(type(second) is int):
            for i in first:
                check(i,second)
        elif(type(second) is set):
            for i in first:
                for j in second:
                    check(i,j)
    else:
        isError = True
        

    end()
        


def end():
    global isHGV
    global isError
    global fails
    if isError is False:
        print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")
        if(isHGV == False):
            print("Equation is not hypergv with {} fail(s)".format(fails))
        else:
            print("Equation is hypergv")
        print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    else:
        print("Ooops Something went wrong...")
        print("Please check your datas")
    print("\n\n\nend of program")
    sys.exit(1)



if __name__== "__main__" :  
    main()
