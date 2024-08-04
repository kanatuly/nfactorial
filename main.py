class UserManager:
    def __init__(self):
        self.users = {}
        self.names = {}
        self.next_id = 0

    def addUser(self, name):
        id = self.next_id
        self.next_id += 1
        self.users[id] = name
        if name in self.names:
            self.names[name].append(id)
        else:
            self.names[name] = [id]
        return id

    def getUser(self, id):
        return self.users.get(id, None)

    def deleteUser(self, id):
        if id in self.users:
            name = self.users.pop(id)
            self.names[name].remove(id)
            return True
        else:
            return False

    def findUserByName(self, name):
        return self.names.get(name, [])


userManager = UserManager()

id1 = userManager.addUser("Jarasar")
id2 = userManager.addUser("Adil")
id3 = userManager.addUser("Jarasar")

print(userManager.getUser(id1))  # Вернет "Jarasar"
print(userManager.getUser(id2))  # Вернет "Adil"
print(userManager.getUser(999))  # Вернет None

print(userManager.findUserByName("Jarasar"))  # Вернет [id1, id3]
print(userManager.findUserByName("Baha"))  # Вернет []

print(userManager.deleteUser(id2))  # Вернет True
print(userManager.deleteUser(999))  # Вернет False

print(userManager.getUser(id2))  # Вернет None