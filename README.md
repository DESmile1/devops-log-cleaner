# Log Cleaner Utility

A simple Python script for automatically cleaning up old logs. 

## Features
* Scans the specified directory.
* Deletes files older than the specified time limit.
* Logs the deletion process.

## How to Run via Docker
1. **Clone the repository:**
   ```bash
   git clone https://github.com/DESmile1/Devops-Log-Cleaner
   cd Devops-Log-Cleaner

2. **Build the image:**
   ```bash
   docker build -t log-cleaner .

3. **Start cleanup:**
   ```bash
   docker run -v $(pwd)/logs:/data/logs Devops-Log-Cleaner