import subprocess, re
from datetime import datetime

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


subprocess.call(["git", "push", "-f"])