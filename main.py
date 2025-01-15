import os
import random


with open('out.txt','w') as f:
    os.system("git add .")
    os.system('git commit -m "greening the grass"')
    os.system('git push origin main')
    f.write(str(random.randint(1,100)))




