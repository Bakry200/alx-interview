#!/usr/bin/python3
import sys
import signal

def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    print_stats(total_size, status_codes)
    sys.exit(0)

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) < 7:
            continue
        
        file_size = int(parts[-1])
        status_code = int(parts[-2])
        
        total_size += file_size
        
        if status_code in status_codes:
            status_codes[status_code] += 1
        
        line_count += 1
        
        if line_count % 10 == 0:
            print_stats(total_size, status_codes)
    
    except (IndexError, ValueError):
        continue

print_stats(total_size, status_codes)
