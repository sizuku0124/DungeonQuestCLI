class Item:
    def __init__(self, name, level, description):
        self.name = name
        self.level = level
        self.description = description


class Heal_Item(Item):
    def __init__(self, name, level, description, amount):
        super().__init__(name, level, description)
        self.amount = amount


class Buff_Item(Item):
    def __init__(self, name, level, description, status, amount):
        super().__init__(name, level, description)
        self.status = status
        self.amount = amount


class Weapon(Item):
    def __init__(self, name, level, description, amount):
        super().__init__(name, level, description)
        self.amount = amount


class Armor(Item):
    def __init__(self, name, level, description, amount):
        super().__init__(name, level, description)
        self.amount = amount
