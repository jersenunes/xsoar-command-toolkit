import sys
from configs.settings import *
from src.orchestrator import orchestrator


def main():
    if not sys.argv:
        print(USAGE_MESSAGE)
        sys.exit(1)

    orchestrator(input=sys.argv)
    

if __name__ == "__main__":
    main()
