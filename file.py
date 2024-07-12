from tkinter import filedialog 
import pickle, os, time
from termcolor import colored
from colorama import init


def start() -> int:
    global directory
   
   
    command = 0
    
    start = [
        "\n       Select file -> 1",
        "       Run selected file(s) -> 2",
        "       View selected file -> 3",
        "       exit -> 4\n"
    ]
    
    for index in start:
        print(colored(index ,color="green"))
        colored('',no_color=True)
        
    if os.path.exists(f"{os.getcwd()}/data.onopen"): 
        with open(f"{os.getcwd()}/data.onopen", mode="rb") as file:
            directory = pickle.load(file)
            
    else:
        directory = {}
        directory.clear()

        
              
    try:

        command = int(input(':'))
        os.system("cls")

    except:
        pass
    
    return command

def main():
    init()
    
    load = [
        '/',
        '|',
        '\\'
    ]
    
    
    while True:  
     
        command = start()
            
        if command==1:
            try:
                file_number = int(input("Enter the bots number: "))
            
                directory.clear()
                
                for select in range(file_number):
                    files = filedialog.askopenfilename()
                    directory[f"{select}"] = files
                    
       
                for value in list(directory.values()):
                    if value in [None, '', [], {}, False, 0]:
                        directory.clear()
    
                with open(f"{os.getcwd()}/data.onopen", mode="wb") as file:
                    pickle.dump(directory, file)                 
                    
                    
                os.system("cls")    
            
            
            except:
                print(colored("\nerror wrong type \n",color="red"))
                colored('',no_color=True)   
        
        elif command==2:
            try:
                if not directory:
                    print(colored("No data available",color="red"))
                    colored('',no_color=True)
                else:
                    for content in directory.values():
                        for loading in load:
                            time.sleep(0.1)
                            print(f"\rloading {loading}\r", end='') 
                            
                        
                        os.startfile(content)                  
                    os.system("cls")
                    
                
            except:
                print(colored("No data available",color="red"))
                colored('',no_color=True)
                
        elif command==3:
            try:
                if not directory:
                    print(colored("No data available",color="red"))
                    colored('',no_color=True)
                    
                else:
                    for content in directory.values():
                        print(colored(content ,color="blue"))
                        colored('',no_color=True)
                    
                
            except:
                print(colored("No data available",color="red"))
                colored('',no_color=True)
                
            
        elif command==4:
            quit()
            
        else:
            os.system("cls")
            print(colored("Value Error",color="red"))
            colored('',no_color=True)
       
       
if __name__ == "__main__":
     main()