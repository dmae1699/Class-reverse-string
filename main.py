class reverse_string:
    def __init__(self,s):
        self.s=s
    def reverse (self):
        return self.s[::-1]
r=reverse_string("Avleen")
print(r.reverse())