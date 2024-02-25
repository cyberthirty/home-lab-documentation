import os

while True:
    currentDir = os.getcwd()
    print(f"Current Directory: {currentDir}")
    print("Directories:")
    dirs = [d for d in os.listdir(currentDir) if os.path.isdir(d)]
    
    for i, d in enumerate(dirs):
        print(f"{i + 1}. {d}")

    print(f"{(len(dirs)+1)}. help\n")
    choice = input("Enter directory number: ")
    if choice.lower() == 'q':
        break

    elif choice.isdigit() and int(choice) <= len(dirs):
        os.chdir(dirs[int(choice) - 1])

    elif int(choice) == (len(dirs) + 2):
        os.chdir("..")

    elif int(choice) == (len(dirs) + 1):
        print(f"\nType `help' to see this list.\n {(len(dirs) + 2)}. Change back \n q. Quit\n")

    else:
        print("Try again...")
