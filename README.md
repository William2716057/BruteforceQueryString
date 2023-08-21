# BruteforceQueryString

# Capture The Flag (CTF) Challenge Script

This Python script is intended for educational purposes and for use in Capture The Flag (CTF) challenges. 
It's designed to help participants automate the process of searching for specific content or flags on web pages by sending HTTP GET requests to a series of URLs.

## Usage

1. Edit the `base_url` variable in the script to specify the target URL. Replace `<IP>`, `<page>`, and `<parameter>` with the appropriate values.

2. Modify the range in the `for` loop to suit your needs. The script will construct URLs by appending numbers from the specified range to the `base_url`.

3. Set the condition in the `if` statement to match the content or flag you're searching for. By default, it looks for the word "flag" in the response text.

4. Run the script to start searching for the content or flag.

Disclaimer
This script is meant for educational purposes and CTF challenges. Please use it responsibly and only on systems and websites that you have permission to access and test.
