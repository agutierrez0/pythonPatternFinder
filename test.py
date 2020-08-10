import sys

def doSomething(blob, pattern):
    # write your code here
    output = []
    sum = 0
    for i in range(0, len(blob)):
        times = 0
        while (blob[i].find(pattern) != -1 and pattern != ''):
            if (len(pattern) > 1):
                blob[i] = blob[i].replace(pattern, pattern[0], 1)
            else:
                blob[i] = blob[i].replace(pattern[0], '', 1)
            times += 1
        output.append(times)
        sum = sum + times

    for i in range(0, len(output)):
        if (output[i] == -1):
            output[i] = 0
    
    outputString = ""
    for thing in output:
        if (outputString == ""):
            outputString = str(thing)
        else:
            outputString = outputString + "|" + str(thing)
    outputString = outputString + "|" + str(sum)
    return outputString

for line in sys.stdin:
    splitted_input = line.split(';')
    pattern = splitted_input[0]
    blobs = splitted_input[1].split('|')

    result = doSomething(blobs, pattern)
    print(result)