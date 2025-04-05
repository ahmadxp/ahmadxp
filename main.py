import os
import time
import random
from datetime import datetime
from colorama import Fore, init

init(autoreset=True)

# Configuration
REPO_PATH = os.path.expanduser("~/path/to/your/repository")  # Change with your local repository path
FILE_TO_MODIFY = "stamp.txt"  # File will be modified for commit

# List random commit messages
RANDOM_COMMIT_MESSAGES = [
    "Update data: {}".format(datetime.now().strftime("%Y-%m-%d")),
    "Code maintenance",
    "Scheduled update",
    "Regular maintenance commit",
    "Automatic code backup",
    "Daily sync: {}".format(datetime.now().strftime("%H:%M")),
    "Project update"
]

def get_random_commit_message():
    return random.choice(RANDOM_COMMIT_MESSAGES)

def perform_commit():
    try:
        # Change to repo path
        os.chdir(REPO_PATH)
    
        # Generate random commit message
        commit_message = get_random_commit_message()
    
        # Modification file (add timestamp)
        with open(FILE_TO_MODIFY, "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{commit_message} - {timestamp}\n")

        print("\n")
    
        # Git commands
        print(Fore.YELLOW + "‣ Starting git add...")
        os.system("git add .")
        time.sleep(2)

        print(Fore.YELLOW + "‣ Starting git commit...")
        os.system(f'git commit -m "{commit_message}"')
        time.sleep(2)

        print(Fore.YELLOW + "‣ Start git push...")
        push_result = os.system("git push origin main") # Change "main" branch with your branch name
        time.sleep(2)
    
        if push_result == 0:
            print(f"\n✅ {Fore.GREEN}Committed at {timestamp} - Message: {commit_message}")
        else:
            print(f"❌ {Fore.RED}Push failed")

    except Exception as e:
        print(f"Error: {str(e)}")        

def main():
    print("Starting daily auto-commit script (15:00 only)")
    print(f"Repostitory path: {REPO_PATH}")
    
    last_commit_day = None

    while True:
        now = datetime.now()
        
        if last_commit_day:
            print(f"Last commit was on day: {last_commit_day} (Today is day: {now.day})", end='\r')
        else:
            print("No commit has been made yet", end='\r')

        # Check if now is 15:00
        if now.hour == 15 and now.minute == 0 and last_commit_day != now.day:
            perform_commit()
            last_commit_day = now.day
            # Wait 1 minute to avoid multiple commits at the same time
            time.sleep(60)

            if last_commit_day:
                print(f"Last commit was on day: {last_commit_day}")
        
        # Check every 30 seconds for efficiency
        time.sleep(30)

if __name__ == "__main__":
    main()
