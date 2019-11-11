from time import sleep

def deputy_alone():   
    deputy_on_duty = False
    deputy_alone = False

    while not deputy_alone:
        f = open('C://Users/Tom/Documents/Python/Bot/Receptura/Recept/Recept/bin/Release/recept_info.txt', 'r', encoding= 'UTF-8')
        s = []
        s = f.read().split('\n')
        f.close()
        # print(s)
        if s[1] == '+':
            deputy_on_duty = True
        else:
            deputy_on_duty = False
        deputy_count = int(s[2])
        if deputy_on_duty and deputy_count == 0:
            deputy_alone = True
        else:
            sleep(10)
    print('deputy is alone and well\n')

# getting names into local variables form recept_info
def prosecutor_alone():
    prosecutor_on_duty = False
    prosecutor_alone = False
    while not prosecutor_alone:
        f = open('C://Users/Tom/Documents/Python/Bot/Receptura/Recept/Recept/bin/Release/recept_info.txt', 'r', encoding= 'UTF-8')
        s = []
        s = f.read().split('\n')
        f.close()
        i=0
        while s[i] != 'шеф':
            i += 1
        if s[i+1] == '+':
            prosecutor_on_duty = True
        else:
            prosecutor_on_duty = False
        prosecutor_count = int(s[i+2])
        if prosecutor_on_duty and prosecutor_count == 0:
            prosecutor_alone = True
        else:
            sleep(10)
    print('prosecutor is alone and well\n')

def main():
    deputy_alone()
    prosecutor_alone()
    input('\nPress enter to exit...')

if __name__ == "__main__":
    main()