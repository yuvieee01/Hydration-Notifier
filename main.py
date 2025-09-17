# MacOS only:-
import os
import time

while True:
    print("Please sip some water!")
    os.system("""
    osascript -e 'display notification "You need to drink some water 💧" with title "Hydration Reminder"'
    """)
    time.sleep(60*60)