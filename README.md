![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg) 

<div align="center">


# PDF HackMe

![Script](https://github.com/evilfeonix/PDF-HackMe/blog/main/img/banner.jpg)

</div>

Our all in one PDF hacking script! created by evilfeonix.\
this our PDF hacking script allow user to encrypt their PDF as well as to decrypt them, crack encrypted PDF, change PDF metadata, inject malicious JavaScript code into PDF file, check if a pdf file is infected with malicious javascript code

<!-- A python based-injector or should i say embedding script that enable malicious actor to simply craft his/her malicious JavaScript payload into a PDF file, by prepending (`app.`) to the javascript payload. This what enables the javascript execution in vulnerable applications. -->

<!-- 
PDF-HackMe J5 is design to modify user javascript payload by prepending (`app.`) to the payload. Then finally embedded the modified javascript payload into PDF file using a python library known as pyPDF2. -->

<!-- # How Malicious PDF File Attack Works
1. A malicious actor manage to craft and inject a malicious javascript payload into PDF file and send it to his/her victims.
2. If the victims open the malicious PDF file on a vulnerable web or other application (app that allow javascript execution)
3. The vulnerable application will execute the evil javascript payload, which will then download a malicious file (eg. trojan, keylogger, or rootkit) to the target machine, allowing those malicious actors to gain access to the target machine. -->

# Tested
1. Termux
2. Window
3. Kali Linux

# Features
1. Encrypt and decrypt PDF file
1. Allow Cracking encrypted PDF file
1. Allow changing metadata of a PDF file
2. Allow embedding of javascript code into PDF file.
2. Allow Chacking if javascript code was embedded to PDF file.
3. Simple and easy-to-use command-line interface (CLI).
5. No need for internet connection.

# Requirements
- Python 3.X
- PyPDF2 and Colorama Library
- Grant Access to Android Storage

# Installations
### In Termux:
Download and install termux app from their official webpage, launch ther termux app and enter the below commands.
```
termux-setup-storage
```
```
apt update && apt upgrade
```
```
apt install git
```
```
apt install python3
```
```
git clone https://github.com/evilfeonix/PDF-HackMe.git
```
```
cd PDF-HackMe
```
```
pip install -r requirements.txt
```
```
python3 hackme.py 
```

### In Kali Linux:
Download and install Kali from their official webpage, in the kali terminal, enter the below commands.
```
git clone https://github.com/evilfeonix/PDF-HackMe.git
```
```
cd PDF-HackMe
```
```
pip install -r requirements.txt
```
```
python3 hackme.py 
```
 
# Watch full Video
![Screen Shot](https://github.com/evilfeonix/PDF-HackMe/blog/main/img/example.jpg)

# Important Note

> **Make sure you fucking have necessary permission to access the `/storage/emulated/0/` directory. If you are running Termux as non-root user, you gonna need to use the `termux-setup-storage` command in order to grant access to the storage directory.**

> **Note that the creators of this tool are not responsible for any misuse or damage caused by its usage.**


# License

_**PDF HackMe** is released under the MIT License. See License for details_ 

#  Follow Us
github: https://github.com/evilfeonix \
website: https://evilfeonix.github.io \
web-blog: https://evilfeonix.github.io/blog \
youtube: https://www.youtube.com/@evilfeonix \
linkedin: https://www.linkedin.com/in/evilfeonix \

<div align="center" >
    Happy PDF Hacking!
</div>
