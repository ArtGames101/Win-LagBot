import sys, os, subprocess

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("\n>>> ").lower().strip()

def main():
    clear_screen()
    print("Zika Trojan\n"
          "===============")
    print("\n"
          "1. Test Msg 1\n"
          "\n"
          "2. Test Msg 2\n"
          "\n"
          "3. Test Msg 3\n"
          "\n"
          "4. Test Sticky Friend\n"
          "\n"
          "5. Run Zika Trojan")
    choice = user_choice()
    if choice == "1":
        os.system("F.vbs")
    if choice == "2":
        os.system("G.vbs")
    if choice == "3":
        os.system("S.vbs")
    if choice == "4":
        os.system("Sticky.vbs")
    if choice == "5":
        clear_screen()
        print("Zika Trojan has Loaded!")
        os.system("M.vbs")

main()
