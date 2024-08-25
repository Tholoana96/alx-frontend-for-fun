#!/usr/bin/python3
import sys
import os

<<<<<<< HEAD
if __name__ == "__main__":
=======
def main():
>>>>>>> 51464e9c6078f522e02aabba615c1fb4ddbd149b
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
<<<<<<< HEAD
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)
    
    sys.exit(0)
=======
        print("Missing {}".format(input_file), file=sys.stderr)
        sys.exit(1)

    # If the script reaches here, it means everything is fine
    sys.exit(0)

if __name__ == "__main__":
    main()

>>>>>>> 51464e9c6078f522e02aabba615c1fb4ddbd149b
