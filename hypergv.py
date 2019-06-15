import os
import sys

table = []
isHGV = True
fails = 0
isError = False
dimension = 0
def main():
    '''
        open file and transform data to table
    '''
    global isError
    global table
    global dimension
    file = open('data.txt','r')
    for line in file:
        # remove '\n' at the end of line
        line = line.replace(' ','')
        line = line.replace('\n','')
        if(line != ""):
            row = list(eval(line))
            table.append(row)


    file.close()
    dimension = len(table)
    
    print("Data: ")
    for row in table:
        print(row)

    print('''
Dimension: {} x {}
'''.format(dimension,dimension))
    '''
        Input
    '''

    '''equation = input("Enter equation: ")
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
    solve(first,second)'''
    #hgv1()
    #hgv2()
    #hgv3()
    #hgv4()
    hgv5()
    end()

def hgv1():
    global table
    global dimension
    global isHGV
    global isError

    print('''
Solving HGV1: x >> x
''')
    for x in range(dimension):
        print('   If x = {}: '.format(x))
        equation = '{a} >> {a}'.format(a=x)
        hold = equation.split('>>')
        first = simplify(hold[0])
        second = simplify(hold[1])
        data = simplify('{a} @ {a}'.format(a=x))
        print('      {a} @ {a} => {data}'.format(a=x,data=data))
        if({0,1}.issubset(data)):
            print('      Check Pass')
        else:
            print('      Check Failed')
            isHGV = False
            isError = False
            end()
    
def hgv2():
    global table
    global dimension
    global isHGV
    global isError

    print('''
Solving HGV2: x >> [0 @ (0 @ x)]
''')
    for x in range(dimension):
        print('   If x =',x,': ')
        equation = '{x} >> [0 @ (0 @ {x})]'.format(x=x)
        hold = equation.split('>>')
        first = simplify(hold[0])
        second = simplify(hold[1])
        
        print('      => {x} >> {y}'.format(x=x,y=second))
        print('      Check:')
        check = False
        for n in second:
            data = simplify('{a} @ {b}'.format(a=x,b=n))
            print('         Checking {x} @ {y} = {data}'.format(x=first,y=n,data=data))
            if({0,1}.issubset(data)):
                print('         Check Pass')
                check = True
                break
            else:
                print('         Check Failed')
        if(check == False):
            isHGV = False
            isError = False
            end()

def hgv3():
    global table
    global dimension
    global isHGV
    global isError

    print('''
Solving HGV3: x >> x @ 1
''')
    for x in range(dimension):
        print('   If x =',x,': ')
        equation = '{x} >> {x} @ 1'.format(x=x)
        hold = equation.split('>>')
        first = simplify(hold[0])
        second = simplify(hold[1])
        #data = simplify('{a} @ {b}'.format(a=first,b=second))
        print('      => {x} >> {y}'.format(x=first,y=second))
        print('      Check:')
        check = False
        for n in second:
            data = simplify('{a} @ {b}'.format(a=first,b=n))
            print('         Checking {x} @ {y} = {data}'.format(x=first,y=n,data=data))
            if({0,1}.issubset(data)):
                print('         Check Pass')
                check = True
                break
            else:
                print('         Check Failed')
        if(check == False):
            isHGV = False
            isError = False
            end()
def hgv4():
    global table
    global dimension
    global isHGV
    global isError
    print('''
Solving HGV4: (x @ y) @ x == [x @ ( y @ x )] @ x
''')
    for x in range(dimension):
        for y in range(dimension):
            print('\n   If x = {} and y = {}:'.format(x,y))
            first = simplify('({x} @ {y}) @ {x}'.format(x=x,y=y))
            second = simplify('[{x} @ ( {y} @ {x} )] @ {x}'.format(x=x,y=y))
            truth_value = first == second
            print('      {} == {}: {}'.format(first,second,truth_value))
            if(truth_value):
                print('      Check Pass')
            else:
                print('      Check Failed')
                isHGV = False
                isError = False
                end()
                
            
def hgv5():
    global table
    global dimension
    global isHGV
    global isError

    print('''
Solving HGV5: (x @ z) @ (x @ y) >> z @ y
''')
    for x in range(dimension):
        for y in range(dimension):
            for z in range(dimension):
                print('\n   If x = {} and y = {} and z = {}:'.format(x,y,z))
                equation = '({x} @ {z}) @ ({x} @ {y}) >> {z} @ {y}'.format(x=x,y=y,z=z)
                hold = equation.split('>>')
                first = simplify(hold[0])
                second = simplify(hold[1])
                data = simplify('{a} @ {b}'.format(a=first,b=second))
                print('      => ({x} @ {z}) @ ({x} @ {y}) >> {z} @ {y}'.format(x=x,y=y,z=z))
                print('      => {x} >> {y}'.format(x=first,y=second))
                print('      Check:')
                for a in first:
                    check = False
                    for b in second:
                        data = simplify('{a} @ {b}'.format(a=a,b=b))
                        print('         Checking {x} @ {y} = {data}'.format(x=a,y=b,data=data))
                        if({0,1}.issubset(data)):
                            print('         Check Pass')
                            check = True
                            break
                        else:
                            print('         Check Failed')
                    if(check == False):
                        isHGV = False
                        isError = False
                        end()

def simplify(data):
    #print("------------------------------------------->")
    #print("--->Simplifying: ", data)
    #print("------------------------------------------->")
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
                        #print("-------------------------------------------")
                        #print("Processing {} @ {}".format(first,x))
                        first = list(first)
                        x = list(x)
                        #print(first)
                        for index_first in first:
                            for index_second in x:
                                #print("--->")
                                table_set = table[index_first][index_second]
                                #print("Set of {} @ {} : {}".format(index_first,index_second,table_set))
                                hold_set = hold_set.union(table_set)
                                #print("--->")
                        #print("-------------------------------------------")
                        #print("------------------------------------------->")
                        first = hold_set
                        #print("--->Result of Union: ", hold_set)
                        #print("------------------------------------------->")
                        
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
        
    
    #end()
        


def end():
    global isHGV
    global isError
    global fails
    if isError is False:
        print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")
        if(isHGV == False):
            print("\tDatais not hypergv")
        else:
            print("\tData is hypergv")
        print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    else:
        print("Ooops Something went wrong...")
        print("Please check your datas")
    print("\n\n\nend of program")
    sys.exit(1)



if __name__== "__main__" :  
    main()
