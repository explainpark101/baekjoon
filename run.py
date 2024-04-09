import sys, os


def main():
    q_number = sys.argv[1]
    os.system(f"python {q_number}/main.py > {q_number}/res.txt")

main()