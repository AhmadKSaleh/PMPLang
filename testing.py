import time

counter = 1
result = ""

while counter < 10000000:
    result = str((counter**2)-1)
    if '0' in result and '1' not in result and '2' not in result and '3' not in result and '4' not in result and '5' not in result and '6' not in result and '7' in result and '8' not in result and '9' not in result:
        print(int(result)+1, counter)
        time.sleep(10)
        counter += 1
        continue
    print("Failure", counter)
    counter += 1 