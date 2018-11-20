#!/usr/bin/env python3

import base64

def main():

	base64_string = input("\nEnter a base64 string: ")
	print("\nYou Entered: " + base64_string)
	ascii_string = base64.b64decode(base64_string)
	print("Byte-wise it's: " + str(ascii_string))
	ascii_string = bytes.decode(ascii_string, encoding="utf-8", errors="strict")
	print("\nYour string is: " + ascii_string + "\n")
	
if __name__ == "__main__":
	main()