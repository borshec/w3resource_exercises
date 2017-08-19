import os
hw = os.uname().machine
if hw.find("64") == -1:
    print("32")
else:
    print("64")
