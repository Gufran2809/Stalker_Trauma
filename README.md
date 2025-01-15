# Stalker_Trauma

This is basically a hack which makes your commits chart green with no effort, all you have to do is clone this repo give necessary permissions and then type on terminal 

```bash 
crontab -e
```

enter below text in whatever editor is opened

```bash
PATH=/usr/bin:/bin:/usr/sbin:/sbin
HOME=/home/gufran
* 18 * * * /bin/bash /home/gufran/Desktop/Stalker_Trauma/run.sh
```

This will make the script to run exactly at 6:00 P.M. given your machine is active.

Based on the special `crond` service provided by linux systems