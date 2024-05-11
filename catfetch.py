from termcolor import cprint
import platform
import psutil
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
    return {
        "Operating System": os_info,
        "Processor": processor,
        "Total Memory": total_memory,
        "Available Memory": available_memory
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

  
                         
 
    

