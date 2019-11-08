# Bot is made so to notify with a message all users 
# about deputy and prosecutor leaving or arriving for work
# You can also put any message in arrive log called moves_info.txt
# so that it will be pushed by bot to all users

# for test purposes using moves_info_test.txt

message = input("Что доложить?\n")
words = message.lower().split(' ')
if words[0] == 'что':
    words = words[1:]
message = ''
for word in words :
    message += word + ' '
message = message[:len(message)-1]
message = message.capitalize()
f = open('C:/Users/Tom/Documents/Python/Bot/Receptura/Recept/Recept/bin/Release/moves_info.txt','w', encoding='UTF-8')
f.write(message+'\n')
f.close()
input("\nБудет доложено с минуты на минуту\n\n\nPress Enter to exit...\n")