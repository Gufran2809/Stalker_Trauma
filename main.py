#!/usr/bin/python3

import os
import random

number_of_commits = random.randint(1,5)

print(number_of_commits)

for _ in range(number_of_commits):
    with open('/home/gufran/Desktop/Stalker_Trauma/out.txt','w') as f:
        f.write(str(random.randint(1,100)))
    os.system("cd /home/gufran/Desktop/Stalker_Trauma")
    os.system("git add .")
    os.system('git commit -m "greening the grass"')
    os.system('git push origin main')



