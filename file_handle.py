import emp, pickle

f = open('emp.dat', 'wb')

n = int(input("Enter no of employees:"))

for i in range(n):
    e_id = int(input("Enter id:"))
    name = input("Enter name:")
    e = emp.Emp(e_id, name)
    pickle.dump(e, f)

f.close()
