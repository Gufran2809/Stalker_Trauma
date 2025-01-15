import os
import random

repo_dir = '/home/gufran/Desktop/Stalker_Trauma'

os.chdir(repo_dir)

number_of_commits = random.randint(1, 5)


for _ in range(number_of_commits):
    with open('/home/gufran/Desktop/Stalker_Trauma/out.txt', 'w') as f:
        f.write(str(random.randint(1, 100)))

    os.system("git add .")
    os.system('git commit -m "greening the grass"')
    os.system('git push origin main')

