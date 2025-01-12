![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg) 

# PDF HackMe J5

![Script](https://github.com/evilfeonix/PDF-HackMe-J5/blog/main/img/banner.jpg)


A python based-injector or should i say embedding script that enable malicious actor to simply craft his/her malicious JavaScript payload into a PDF file, by prepending (`app.`) to the javascript payload. This what enables the javascript execution in vulnerable applications.

PDF-HackMe J5 is design to modify user javascript payload by prepending (`app.`) to the payload. Then finally embedded the modified javascript payload into PDF file using a python library known as pyPDF2.

## How Malicious PDF File Attack Works
1. A malicious actor manage to craft and inject a malicious javascript payload into PDF file and send it to his/her victims.
2. If the victims open the malicious PDF file on a vulnerable web or other application (app that allow javascript execution)
3. The vulnerable application will execute the evil javascript payload, which will then download a malicious file (eg. trojan, keylogger, or rootkit) to the target machine, allowing those malicious actors to gain access to the target machine.

## PDF HackMe J5 Features
1. Prepend (`app.`) to the javascript payload which enables the javascript to execute in vulnerable applications
2. Enable embedding of javascript payload into PDF file using a python library known as pyPDF2.
3. Simple and easy-to-use command-line interface (CLI).
4. Enable documents encryption.
5. No need for internet connection.

## PDF HackMe J5 Requirements
- Python 3.X
- PyPDF2 and Colorama Library
- Grant Access to Android Storage

## PDF HackMe J5 Installations
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
git clone https://github.com/evilfeonix/PDF-HackMe-J5.git
```
```
cd PDF-HackMe-J5
```
```
pip install -r requirements.txt
```
```
python3 hackme.py 
```

## PDF HackMe J5 Usage
1. You gotta firstly configure the `PAYLOAD` file, which contain the malicious javascript code to inject to the PDF file
```js
var author = "EvilFeonix";
var tool = "PDF-HackMe-J5";
alert("Welcome To "+tool+", Created by "+author+"!");
alert("this is a python based-embedding script that allows you to simply craft your own malicious JavaScript payload to a PDF file");
console.log(author);
console.log(tool);
```

2. Then finally run the tool.
```
python3 hackme.py
```
This command runs the default payload file which we firstly configure. But if you have a custom javascript file, you can use it as you payload. All you gotta do is to run the tool by passing the path to your javascript file.
```
python3 hackme.py --payload <path-to-javascript-file>
```


## PDF HackMe J5 Example
- Input javascript payload file (`script.js`)
```js
function Message(name){
    var msg = "PDF HackMe J5!, was created by "+name;
    console.log(msg);
    alert(msg);
}
Message("evilfeonix");
```
- Run the Script by passing the payload file:
``` 
python3 hackme.py --payload script.js
[*] Enter Path To PDF [/storage/emulated/0/]: Documents/mydocs.pdf
[*] Enter Name for New PDF: embedded_js.pdf
[*] Will You Like Encrypting Your New PDF [Yes/oN]: Yes
[*] Enter Password for Opening New PDF: user1234 
[*] Enter Password for Modifying New PDF: admin1234

[*] Creating New PDF File... 
[*] Injecting JavaScript Payload... 
[*] JavaScript Payload Successfully Injected!
[*] Encrypting New PDF File...
[*] New PDF Successfully Encrypted! 
[*] New PDF Successfully Created!
[*] Path To New PDF File: /storage/emulated/0/PDF-HackMe-J5/embedded_js.pdf
```

- The modified javascript payload while be:
```js
function Message(name){
    var msg = "PDF HackMe J5!, was created by "+name;
    app.console.log(msg);
    app.alert(msg);
}
app.Message("evilfeonix");
```
# Screen Shot
![Screen Shot](https://github.com/evilfeonix/PDF-HackMe-J5/blog/main/img/example.jpg)

# Important Note

> **Make sure you fucking have necessary permission to access the `/storage/emulated/0/` directory. If you are running Termux as non-root user, you gonna need to use the `termux-setup-storage` command in order to grant access to the storage directory.**

> **The PDF files created by this tool are store and saved in `/storage/emulated/0/PDF-HackMe-J5/` directory. And if PDF file name you entered exists in the destination path, this tool will over-write the file.**

> **Variables like  Title,Author,Application, in your payload are modified by add_metadata, just add (s) eg. Titles,Authors,Applications, in order to avoid the modification**

> **Note that the creators of this tool are not responsible for any misuse or damage caused by its usage.**


# License

_**PDF HackMe J5** is released under the MIT License. See License for details_ 

#  Follow Us
<!-- website: https://www.evilfeonix.com

web-blog: https://www.evilfeonix.com/blog -->

linkedin: https://www.linkedin.com/in/evilfeonix

youtube: https://www.youtube.com/@3V1LF30N1X
