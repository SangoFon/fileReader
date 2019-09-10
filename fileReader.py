#this statement helps to open the file split and and strip line
fname = input('Enter File: ')
if len(fname) < 1: fname ='romeo.txt'
hdl = open(fname)
di = dict()
for line in hdl:
    line = line.rstrip()
    wds = line.split()
    print(wds)
    # this is how to split the words
    for element in wds:
        if element in di:
            di[element] = di[element] +1
        else:
            di[element] = 1
            print('**New**')
        print(element, di[element])
print(di)
