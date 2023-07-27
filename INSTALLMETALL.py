import os
from colorama import Fore, Style

def install_metasploit():
    os.system('pkg update')
    os.system('pkg install git -y')
    os.system('git clone https://github.com/rapid7/metasploit-framework.git')
    os.chdir('metasploit-framework')
    os.system('bundle install')
    print(Fore.GREEN + "Metasploit has been installed successfully.")
    print(Fore.YELLOW + "cd metasploit-framework")
    print("bundle install")
    
def install_dependencies():
    os.system('pkg update')
    os.system('pkg install git curl wget ruby -y')
    os.system('pkg install libffi libffi-dev make clang -y')
    os.system('gem install nokogiri -v 1.12.5 -- --use-system-libraries')
    os.system('gem install bundler')
    os.system('gem install pg -v 1.2.3 -- --use-system-libraries')
    os.system('gem install grpc -v 1.42.0 -- --use-system-libraries')
    os.system('gem install sqlite3 -v 1.4.2 -- --use-system-libraries')
    os.system('gem install rex-bin_tools')
    os.system('gem install activerecord -v 6.1.4.1 -- --use-system-libraries')
    os.system('')
    import os
from colorama import Fore, Style

def install_metasploit():
    os.system('pkg update')
    os.system('pkg install git -y')
    os.system('git clone https://github.com/rapid7/metasploit-framework.git')
    os.chdir('metasploit-framework')
    os.system('bundle install')
    print(Fore.GREEN + "Metasploit has been installed successfully.")
    print(Fore.YELLOW + "cd metasploit-framework")
    print("bundle install")
    
def install_dependencies():
    os.system('pkg update')
    os.system('pkg install git curl wget ruby -y')
    os.system('pkg install libffi libffi-dev make clang -y')
    os.system('gem install nokogiri -v 1.12.5 -- --use-system-libraries')
    os.system('gem install bundler')
    os.system('gem install pg -v 1.2.3 -- --use-system-libraries')
    os.system('gem install grpc -v 1.42.0 -- --use-system-libraries')
    os.system('gem install sqlite3 -v 1.4.2 -- --use-system-libraries')
    os.system('gem install rex-bin_tools')
    os.system('gem install activerecord -v 6.1.4.1 -- --use-system-libraries')
    print(Fore.GREEN + "All required packages have been downloaded successfully.")
    print(Style.RESET_ALL)

def main_menu():
    os.system('clear')
    banner = f"""
{Fore.CYAN}
 █████  ██████  ██████   ██████  ██    ██ ██████   ██████   ██████  
██   ██ ██   ██ ██   ██ ██    ██ ██    ██      ██ ██  ████ ██  ████ 
███████ ██████  ██   ██ ██    ██ ██    ██  █████  ██ ██ ██ ██ ██ ██ 
██   ██ ██   ██ ██   ██ ██    ██ ██    ██ ██      ████  ██ ████  ██ 
██   ██ ██████  ██████   ██████   ██████  ███████  ██████   ██████  
                                                                    
{Style.RESET_ALL}"""
    print(banner)
    print(f"{Fore.MAGENTA}+_+_+_+_+_+_+_By Abdou200+_+_+_+_+_+_+_+{Style.RESET_ALL}")

    while True:
        print("\nChoose your option:")
        print(f"{Fore.YELLOW}1- Start the installation process")
        print("2- Download all required packages")
        print("3- Exit{Style.RESET_ALL}")
        choice = input(">> ")

        if choice == "1":
            install_metasploit()
            break
        elif choice == "2":
            install_dependencies()
        elif choice == "3":
            print(f"{Fore.RED}Exiting the program.{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Please select a valid option.{Style.RESET_ALL}")

if __name__ == "__main__":
    main_menu()

    
    print(Fore.GREEN + "All required packages have been downloaded successfully.")
    print(Style.RESET_ALL)

def main_menu():
    os.system('clear')
    banner = f"""
{Fore.CYAN}
 █████  ██████  ██████   ██████  ██    ██ ██████   ██████   ██████  
██   ██ ██   ██ ██   ██ ██    ██ ██    ██      ██ ██  ████ ██  ████ 
███████ ██████  ██   ██ ██    ██ ██    ██  █████  ██ ██ ██ ██ ██ ██ 
██   ██ ██   ██ ██   ██ ██    ██ ██    ██ ██      ████  ██ ████  ██ 
██   ██ ██████  ██████   ██████   ██████  ███████  ██████   ██████  
                                                                    
{Style.RESET_ALL}"""
    print(banner)
    print(f"{Fore.MAGENTA}+_+_+_+_+_+_+_By Abdou200+_+_+_+_+_+_+_+{Style.RESET_ALL}")

    while True:
        print("\nChoose your option:")
        print(f"{Fore.YELLOW}1- Start the installation process")
        print("2- Download all required packages")
        print("3- Exit{Style.RESET_ALL}")
        choice = input(">> ")

        if choice == "1":
            install_metasploit()
            break
        elif choice == "2":
            install_dependencies()
        elif choice == "3":
            print(f"{Fore.RED}Exiting the program.{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Please select a valid option.{Style.RESET_ALL}")

if __name__ == "__main__":
    main_menu()
