import subprocess, re, os
from datetime import datetime

if os.environ.get('DISABLE_AUTO_SAVE', None) == 'TRUE':
    exit(0)

last_commit_message = subprocess.check_output(["git", "log", "--pretty=format:%s", "HEAD^..HEAD"]).decode('utf-8')
print("Last commit:", last_commit_message)

now = datetime.now()
new_commit_message = "DEV " + now.strftime("%H:%M:%S %d-%m-%y")

print("New commit: ", new_commit_message)

subprocess.call(["git", "add", "."])

# Pattern: DEV HH:MM:SS dd-mm-YY
pattern = re.compile(r"DEV ([0-2][0-9]:[0-5][0-9]:[0-5][0-9]) ([0-3][0-9]-[0-1][0-9]-[0-9][0-9])")
match = pattern.match(last_commit_message)

if match:
    # Previous commit was a DEV commit -> ammend DEV commit

    # previous_time = match.group(1)
    # previous_date = match.group(2)

    subprocess.call(["git", "commit", "--amend", "-m", new_commit_message])


else:
    # Previous commit was a regular commit -> create new DEV commit

    subprocess.call(["git", "commit", "-m", new_commit_message])

# Update intermediate repo
subprocess.call(["git", "push", "-f"])

# Reset local changes to be reflected as satged if last commit was a dev commit
if os.environ.get('AUTO_RESET', None) == 'TRUE':
    subprocess.call(["git", "reset", "--soft", "HEAD~1"])