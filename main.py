import os
import random

number_of_commits = random.randint(1,5)

for _ in range(number_of_commits):
    with open('out.txt','w') as f:
        f.write(str(random.randint(1,100)))

    os.system("git add .")
    os.system('git commit -m "greening the grass"')
    os.system('git push origin main')



