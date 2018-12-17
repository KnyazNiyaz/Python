def main():
    loopNum = int(input('How many time would you like to loop?\n'))
    counter = 1
    recurr(loopNum, counter)

def recurr(loopNum, counter):
    if loopNum > 0:
        print('This is loop iteration - ', counter)
        recurr(loopNum - 1, counter + 1)
    else:
        print('The loop has completed')

main()