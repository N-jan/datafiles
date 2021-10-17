#!/bin/bash
ssh-keygen -t rsa -b 4096 -C "niru.tm@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa    

git remote -v   # Verify remote if not correct set it
git remote set-url origin git@github.com:N-jan/datafiles.git
echo"-----------------------------------"
echo "copy below to github sshkey"
cat ~/.ssh/id_rsa.pub
