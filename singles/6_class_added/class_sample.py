class Game():
    def __init__(self, name, price, genre=None):
        self.name = name
        self.price = price
        self.genre = genre

g1 = Game("Minecraft", 9.99, "Sandbox")
g2 = Game("GTA", 89.99, "Action-adventure")
g3 = Game("Forza", 99.99 , "Racing")
g4 = Game("Apex Legends", 0, "First-person shooter")
g5 = Game("Rocket League", 0)
print(g4.genre)
print(g5.genre)

# class Laptop():
#     def __init__(self, brand, ram, cpu, price, os_='windows 10'):
#         self.brand = brand
#         self.ram = ram
#         self.cpu = cpu
#         self.price = price
#         self.os_ = os_

#     def get_info(self):
#         return f"Brand: {self.brand:15}Ram:{self.ram:10}CPU: {self.cpu:5}Price: {self.price:<10} Tooman OS: {self.os_}"

#     # def __str__(self):
#         # return f"Brand: {self.brand:15}Ram:{self.ram:10}CPU: {self.cpu:5}Price: {self.price:<10} Tooman OS: {self.os_}"

# laptop1 = Laptop('Lenovo', '8 Gig', 'i5', 32000000)
# laptop2 = Laptop('Macbook Air-B', '8 Gig', 'm2', 56000000, "Apple Mac OS Sonoma")
# # print(laptop1.price, laptop1.os_)
# # print(laptop2.price, laptop2.os_)
# print(laptop1.get_info())
# print(laptop2.get_info())
# # print(laptop1)
# # print(laptop2)
