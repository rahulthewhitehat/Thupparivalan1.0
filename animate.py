import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def print_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def bill():
    clear()
    print("\033[37m")
    animation_frames = [
        r""" 
    ███████╗██╗  ██╗██╗   ██╗██████╗ ██████╗  █████╗ ██████╗ ██╗██╗   ██╗ █████╗  █████╗ ██╗      █████╗ ███╗   ██╗
      """,
        r""" 
    ███████╗██╗  ██╗██╗   ██╗██████╗ ██████╗  █████╗ ██████╗ ██╗██╗   ██╗ █████╗  █████╗ ██╗      █████╗ ███╗   ██╗
   ╚══██╔══╝██║  ██║██║   ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║██║   ██║██╔══██╗██╔══██╗██║     ██╔══██╗████╗  ██║
      """,
      r"""
    ███████╗██╗  ██╗██╗   ██╗██████╗ ██████╗  █████╗ ██████╗ ██╗██╗   ██╗ █████╗  █████╗ ██╗      █████╗ ███╗   ██╗
   ╚══██╔══╝██║  ██║██║   ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║██║   ██║██╔══██╗██╔══██╗██║     ██╔══██╗████╗  ██║
      ██║   ███████║██║   ██║██████╔╝██████╔╝███████║██████╔╝██║██║   ██║███████║███████║██║     ███████║██╔██╗ ██║
     """,
     r"""
    ███████╗██╗  ██╗██╗   ██╗██████╗ ██████╗  █████╗ ██████╗ ██╗██╗   ██╗ █████╗  █████╗ ██╗      █████╗ ███╗   ██╗
   ╚══██╔══╝██║  ██║██║   ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║██║   ██║██╔══██╗██╔══██╗██║     ██╔══██╗████╗  ██║
      ██║   ███████║██║   ██║██████╔╝██████╔╝███████║██████╔╝██║██║   ██║███████║███████║██║     ███████║██╔██╗ ██║
      ██║   ██╔══██║██║   ██║██╔═══╝ ██╔═══╝ ██╔══██║██╔══██╗██║╚██╗ ██╔╝██╔══██║██╔══██║██║     ██╔══██║██║╚██╗██║
      """,
      r"""
    ███████╗██╗  ██╗██╗   ██╗██████╗ ██████╗  █████╗ ██████╗ ██╗██╗   ██╗ █████╗  █████╗ ██╗      █████╗ ███╗   ██╗
   ╚══██╔══╝██║  ██║██║   ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║██║   ██║██╔══██╗██╔══██╗██║     ██╔══██╗████╗  ██║
      ██║   ███████║██║   ██║██████╔╝██████╔╝███████║██████╔╝██║██║   ██║███████║███████║██║     ███████║██╔██╗ ██║
      ██║   ██╔══██║██║   ██║██╔═══╝ ██╔═══╝ ██╔══██║██╔══██╗██║╚██╗ ██╔╝██╔══██║██╔══██║██║     ██╔══██║██║╚██╗██║
      ██║   ██║  ██║╚██████╔╝██║     ██║     ██║  ██║██║  ██║██║ ╚████╔╝ ██║  ██║██║  ██║███████╗██║  ██║██║ ╚████║
       """,
       r"""
     ███████╗██╗  ██╗██╗   ██╗██████╗ ██████╗  █████╗ ██████╗ ██╗██╗   ██╗ █████╗  █████╗ ██╗      █████╗ ███╗   ██╗
    ╚══██╔══╝██║  ██║██║   ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║██║   ██║██╔══██╗██╔══██╗██║     ██╔══██╗████╗  ██║
       ██║   ███████║██║   ██║██████╔╝██████╔╝███████║██████╔╝██║██║   ██║███████║███████║██║     ███████║██╔██╗ ██║
       ██║   ██╔══██║██║   ██║██╔═══╝ ██╔═══╝ ██╔══██║██╔══██╗██║╚██╗ ██╔╝██╔══██║██╔══██║██║     ██╔══██║██║╚██╗██║
       ██║   ██║  ██║╚██████╔╝██║     ██║     ██║  ██║██║  ██║██║ ╚████╔╝ ██║  ██║██║  ██║███████╗██║  ██║██║ ╚████║
       ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝
       """
    ]
    
    colors = ['91', '92', '93', '94', '95', '96']  # Different colors for text
    
    for i, frame in enumerate(animation_frames):
        clear()
        color_code = colors[i % len(colors)]
        print_color(frame, color_code)
        time.sleep(0.12)      
    
    print("\033[91m\t\t\t\t\t\t\t Version - 1.0")    
    print()
    print("\033[93m Proudly Designed by @RahulTheWhiteHat using Open Source Tools")
    print("\033[93m Contact: @rahulthewhitehat (GitHub/LinkedIn/Instagram)\n")
    