import time
import random

quotes = [
    "Small progress is still progress.",
    "Consistency beats motivation.",
    "One more hour can change everything.",
    "Discipline > excuses.",
]

study_time = int(input("Enter study time in minutes: "))

print("\nStarting focus session...\n")

for i in range(study_time, 0, -1):
    print(f"{i} minute(s) remaining...")
    time.sleep(60)

print("\nSession Complete.\n")
print(random.choice(quotes))
