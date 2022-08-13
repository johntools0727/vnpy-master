import os


print(os.getcwd())
os.system("pause")

for i, j, k in os.walk(os.getcwd()):
    print(i)
    os.system("pause")
    print(j)
    os.system("pause")
    print(k)
    os.system("pause")


