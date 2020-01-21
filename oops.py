class Company:

    company = "ABC"

    def __init__(self, pid, price):
        print("self:", self)
        self.pid = pid
        self.price = price

pref = Company(101, 2000)
pref.rating = 4
print("pref", pref)                     #same hash code as that of self (of same object)