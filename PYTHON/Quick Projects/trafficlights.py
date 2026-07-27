import time

def main():

    while True:

        print("\n🔴\n")

        for i in range (30, 0, -1):
            time.sleep(1)

        print("\n🟢\n")
        
        for i in range (30, 0, -1):
            time.sleep(1)

        print("\n🟡\n")

        for i in range (3, 0, -1):
            time.sleep(1)

if __name__ == "__main__":
    main()