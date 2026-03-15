import os
import time

directory = "/data/logs" # Specify the directory to clean up

days = 1 # Number of days to keep files
threshold = time.time() - (days * 24 * 60 * 60)  # Seconds to hours

if os.path.exists(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.getmtime(file_path) < threshold: # Check if the file is older than the threshold
            os.remove(file_path)
            print(f"The old file has been deleted: {filename}")
else:
    print(f"The directory does not exist")