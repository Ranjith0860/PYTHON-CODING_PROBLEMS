class MyFamily:

    def FamilyNames(self, n):
        self.members = []

        for i in range(n):
            name = input("Enter name: ")
            age = input("Enter age: ")
            self.members.append([name, age])

        print("Family Members: ")
        print(self.members)
        for name, age in self.members:
            print(name, age)



my = MyFamily()
k=int(input("enter family members count: "))
my.FamilyNames(k)
