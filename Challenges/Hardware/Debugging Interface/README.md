# Debugging Interface
## Challenge Description: 
We accessed the embedded device's asynchronous serial debugging interface while it was operational and captured some messages that were being transmitted over it. Can you decode them?

## STEPS
Download zip file. Extract it and write the password "hackthebox" . Open the extracted file in terminal.

### ![ab](https://github.com/user-attachments/assets/daa93491-a69d-49da-a283-0ef1cdfc54b0) 
### ![ab](https://github.com/user-attachments/assets/ef31e7e1-074a-427c-b468-cb9346b8f803)
### ![ab](https://github.com/user-attachments/assets/c168a4e0-7c08-481c-bc92-0083adbe338e)
### ![ab](https://github.com/user-attachments/assets/aba40fb5-564b-4096-bbc2-b680e951841b) - The 'strings' command in Linux is used to extract readable strings from a binary file.
### ![ab](https://github.com/user-attachments/assets/b730e62b-e7d2-44bf-9103-8b0fae794e8f) - First word we saw "saleae". Google it.
### ![ab](https://github.com/user-attachments/assets/8f7da1c7-1bfb-4d00-bb39-70e00af3d7d2) - Download the Linux version of "Saleae"
### ![ab](https://github.com/user-attachments/assets/2afb0dde-848d-485f-8eb3-8914b434a7cf)
### ![ab](https://github.com/user-attachments/assets/706911aa-6683-4b5d-bf3a-cd32e76439ea)
### ![ab](https://github.com/user-attachments/assets/864ed12b-62b8-4e84-a3d2-ef43cac6f481)
### ![ab](https://github.com/user-attachments/assets/115f3508-72a4-48e9-bdb0-6d7c74d2b6d3) - CLick on Open and select the required file. You can see the data blocks.
### ![ab](https://github.com/user-attachments/assets/8908025c-e297-4e1a-818f-45e91fb74354) - zoom the blocks in microseconds.
### ![ab](https://github.com/user-attachments/assets/5c0d4f53-8844-44c6-bcd4-31c1f7941bc9) - You can see the Async serial option on the right side. You can make the changes accordingly.
### ![ab](https://github.com/user-attachments/assets/8839a0c4-1e28-44ba-8470-484d9d64cf8f) - Again Goto Async Serial options. Click on 'Ascii'. We didn't get the flag.  
### ![ab](https://github.com/user-attachments/assets/dea6dd84-e931-40c0-89a6-f8184097e685) - Again Edit 'Async Serial'.
### ![ab](https://github.com/user-attachments/assets/cd743c2a-1faa-4bec-aafc-10f3b62caffa) - After making the changes you got the flag.
