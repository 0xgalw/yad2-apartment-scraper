#!/bin/bash

cd /home/<user>/yad2-scraper
# Wait for a random duration between 0 and 60 seconds
sleep $((RANDOM % 60))

# Your original script commands go here
# For example:

echo "Running script at $(date)" >> logs.txt
# Add your actual script commands below

python3 main.py >> logs.txt

echo "-------------" >> logs.txt