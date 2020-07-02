import os 
import time 

k = ("""
██╗░░░██╗██████╗░██████╗░░█████╗░████████╗███████╗
██║░░░██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██║░░░██║██████╔╝██║░░██║███████║░░░██║░░░█████╗░░
██║░░░██║██╔═══╝░██║░░██║██╔══██║░░░██║░░░██╔══╝░░
╚██████╔╝██║░░░░░██████╔╝██║░░██║░░░██║░░░███████╗
░╚═════╝░╚═╝░░░░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝
""")

def update():
  os.system("clear")
  print(k)
  print("[$] Update Tool Wite . . . ")
  os.system("rm security-phone.py -rif")
  os.system("wget https://hostservervip.000webhostapp.com/security-phone.py")
  os.system("python3 security-phone.py")
  if os.path.exists("security-phone.py"):
    print("[√] Found Tool . . .")
  else:
    print("[×] Not Found security-phone.py ?")
    os.system("clear")
    time.sleep(1)
    os.system("wget https://hostservervip.000webhostapp.com/security-phone.py")
    os.system("python3 update-Auto.py")
  
  
  
update()