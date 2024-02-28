import os
import subprocess

def execute_command(command):
    try:
        # Capture the output of the command as well as the error message if any
        result = subprocess.run(command, shell=True, text=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("\033[31m" + f"Error executing command: {e}" + "\033[0m")
        print(e.stderr)

while True:
    currentDir = os.getcwd()
    # Flag to decide whether to show directories or not
    showDirectories = True

    if showDirectories:
        print("\033[32m" + f"\nDirectories of {currentDir}" + "\033[0m")
        dirs = [d for d in os.listdir(currentDir) if os.path.isdir(d)]
        
        for i, d in enumerate(dirs):
            print(f"drwxr-xr-x  1 {i + 1} {d}")

        if len(dirs) == 0:
            print("\n .\n ..")

    choice = input("\033[34m" + f"\n{currentDir}:~$ " + "\033[0m")

    if choice.lower() == "q":
        break
    elif choice.lower() == "cd ..":
        os.chdir("..")
    elif choice.lower().startswith("cd "):
        path = choice.split(maxsplit=1)[1]
        try:
            os.chdir(path)
        except Exception as e:
            print("\033[31m" + f"\nError: {e}" + "\033[0m")
    else:
        showDirectories = False  
        execute_command(choice)

print("\033[0m" + "\nThanks for using our service." + "\033[0m")
