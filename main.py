import sys

sys.stdin = open("io/input.txt", "r")
sys.stdout = open("io/output.txt", "w")
sys.stderr = open("io/error.txt", "w")

# from here, each call to `input()` will return the next line from `input.txt`
# each print statement will write to `output.txt`
# errors are written to `output.txt`

if __name__ == "__main__":
    pass