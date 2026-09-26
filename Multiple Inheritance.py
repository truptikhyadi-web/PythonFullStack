class Parent1():
    def assign_string_one(self, str1):
        self.str1=str1
    def show_string_one(self):
        return self.str1
class Parent2():
    def assign_string_two(self, str2):
        self.str2=str2
    def show_string_two(self):
        return self.str2
class Derived(Parent1, Parent2):
    def assign_string_three(self,str3):
        self.str3=str3
    def show_string_three(self):
        return self.str3
    
d1=Derived()
d1.assign_string_one("one")
d1.assign_string_two("two")
d1.assign_string_three("three")

print(d1.show_string_one())
print(d1.show_string_two())
print(d1.show_string_three())
