import emp,pickle

f = open('emp.dat', 'rb')

while True:
    try:
        obj = pickle.load(f)
        obj.display()
    except EOFError:
        print("End of File occured!")
        break

f.close()
