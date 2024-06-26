from termcolor import cprint
import platform
import psutil
import cpuinfo
import pwd
import os
# nfetch 
# ascii art
# catpfetch
def ascii():
    # os infos
    os_info = platform.platform()

    # prozessinformationen
    processor = platform.processor()

    # Speicherinformationen
    memory_info = psutil.virtual_memory()
    total_memory = memory_info.total
    available_memory = memory_info.available
    # cpu
    cpu_info = cpuinfo.get_cpu_info()

    # Shell
    shell_user = os.getlogin()
    shell_info = pwd.getpwnam(shell_user)
    user_shell = shell_info.pw_shell

    
    # Prozessornamen
    processor_name = cpu_info['brand_raw']
    return {
        "Operating System": os_info,
        "Processor": processor,
        "Total Memory": total_memory,
        "Available Memory": available_memory,
        "CPU": processor_name,
        "User": shell_user,
        "Shell": user_shell
    }
cat = """
      
      *-.                   
        )  _`-.             
       .  : `. .                
       : _   '  \\               
       ; *` _.   `*-._          
       `-.-'          `-.       
         ;       `       `.     
         :.       .        \\    
         . \\  .   :   .-'   .   
         '  `+.;  ;  '      :   
         :  '  |    ;       ;-. 
         ; '   : :`-:     _.`* 
       .*' /  .*' ; .*`- +'  `*
      `*-*   `*-*  `*-*'   
      """
print(cat)
def main():
    system_info = ascii()
    for key,value in system_info.items():
        print(f"{key}: {value}")
if __name__ == "__main__":
    main()

  
                         
 
    

