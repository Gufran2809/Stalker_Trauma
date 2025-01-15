import os
import random
import time


# no_of_commits = random.randint(1,5)
no_of_commits = 10


for _ in range(no_of_commits):
    with open('out.txt','w') as f:
        f.write(str(random.randint(1,10)))
    time.sleep(1)




