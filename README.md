# Log Cleaner Utility

A simple Python script for automatically cleaning up old logs. 

## Features
* Scans the specified directory.
* Deletes files older than the specified time limit.
* Logs the deletion process.

## How to Run via Docker

1. **Build the image:**
   ```bash
   docker build -t log-cleaner .
