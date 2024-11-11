# Proxy Speedtest

This program allows you to test the internet speed of multiple proxies and logs the results, including download speed, upload speed, and ping.

## Features
- Tests the speed of multiple proxies from a given list.
- Measures download speed, upload speed, and ping for each proxy.
- Logs the results to a file for easy analysis.
- Continues to the next proxy even if one fails.

## Requirements
- Python 3.x
- `speedtest-cli` package
- Install dependencies:
- Navigate to the proxy-speedtest folder: cd x86/proxy-speedtest
  
install module: pip install speedtest-cli

Usage
Prepare your proxy list:

Create a file named proxy.txt in the same directory.
Add proxy in the format: ip:port:user:pass, one per line.
run program by: python main.py or run start.bat
Check the results:
The results will be saved in result.txt in the following format: 
ip:port:user:pass|dow:xx.xxMbps|up:xx.xxMbps|ping:xx.xxms

Example proxy.txt
16.103.5.135:6715:username:password
11.124.25.232:6121:username:password
121.111.11.234:6632:username:password



## Installation
1. **Clone the repository**:
   ```bash
   git clone [https://github.com/X86-TN/proxy-speedtest.git]
