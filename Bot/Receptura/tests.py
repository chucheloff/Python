from time import sleep
import time

with open('C:/Users/Tom/Documents/Python/Bot/Receptura/deputy_wait_queue.txt','w') as f:
    f.write('empty')

'''
with open('deputy_wait_queue.txt','w') as f:
    f.write('548993 ')
    f.write(str(time.time())+'\n')
    sleep(2)
    f.write('548993 ')
    f.write(str(time.time())+'\n')
    sleep(2)
    f.write('358893 ')
    f.write(str(time.time())+'\n')


with open('deputy_wait_queue.txt','r') as f:
    queue = f.read().split('\n')
wait_list = []
for item in queue:
    wait_list.append(item.split(' '))


sleep(3)
then = time.time()
difference = int(then-now)
print(difference)
'''