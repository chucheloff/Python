# Bot is made so to notify with a message all users 
# about deputy and prosecutor leaving or arriving for work
# You can also put any message in arrive log called moves_info.txt
# so that it will be pushed by bot to all users

# for test purposes using moves_info_test.txt

message = input("Что доложить?\n")
with open('C:/Users/Tom/Documents/Python/Bot/Receptura/Recept/Recept/bin/Release/moves_info.txt',
          'a+', encoding='UTF-8') as f:
    f.write('\n'+message+'\n')
print('\a')
input("\nБудет доложено с минуты на минуту\n\n\nPress Enter to exit...\n")