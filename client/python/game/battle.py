import random

from client.python.game.item import Buff_Item, Heal_Item
from client.python.utils.input import selecter


class battle:
    def __init__(self, character, enemy):
        self.character = character
        self.enemy = enemy
        self.turn = 1

    def next_turn(self):
        self.turn = self.turn + 1

    def agility_judge(self):
        return self.character.agility >= self.enemy.agility

    def player_turn(self):
        return self.sellect_command(-1, self.character, self.enemy)

    def enemy_turn(self):
        return self.sellect_command(random.randint(0, 0), self.enemy, self.character)

    @staticmethod
    def attack(owner, target):
        damage = round(
            (max(owner.attack - target.defense, 0)) * random.uniform(0.8, 1.2)
        )
        target.hp = max(0, target.hp - damage)
        print(f"{target.name}に{damage}ダメージ")
        return 0

    @staticmethod
    def cast(owner, target):
        i = 0
        print("スキルを選択")
        for skill in owner.skill_list:
            print(
                f"{i} {skill['name']} MP:{skill['mp']}\n{skill['status']}:{skill['amount']}"
            )
            i = i + 1

        num = selecter("", "", len(owner.skill_list) - 1)
        cast_skill = owner.skill_list[num]
        if cast_skill["mp"] > owner.mp:
            print("mpが足りない!")
            return 1

        if cast_skill["status"] == "attack":
            owner.attack = owner.attack + cast_skill["amount"]
        elif cast_skill["status"] == "defense":
            owner.defense = owner.defense + cast_skill["amount"]
        elif cast_skill["status"] == "agility":
            owner.agility = owner.agility + cast_skill["amount"]
        elif cast_skill["status"] == "damage":
            damage = round(
                (max(cast_skill["amount"] - target.defense, 0))
                * random.uniform(0.8, 1.2)
            )
            target.hp = max(0, target.hp - damage)

        elif cast_skill["status"] == "heal":
            owner.hp = owner.hp + cast_skill["amount"]
        owner.mp = owner.mp - cast_skill["mp"]
        return 0

    @staticmethod
    def items(owner, target):

        def item_judgement(item):
            item = isinstance(item, Heal_Item) or isinstance(item, Buff_Item)
            return item

        i = 0
        items = list(filter(item_judgement, owner.inventory))
        print("アイテム一覧")
        for item in items:
            print(f"{i} {item.name} ×{item.quantity}\n{item.description}")
            i = i + 1
        num = selecter("", "", len(items) - 1)
        items[num].use(owner)
        if items[num].getQuantity() == 0:
            owner.inventory.remove(items[num])
        return 0

    @staticmethod
    def escape(owner, target):
        num = random.randint(1, round(owner.agility / 2) + target.agility)
        if 1 <= num <= round(owner.agility / 2):
            return 2
        return 0

    def sellect_command(self, num, owner, target):
        number = -1
        if num == -1:
            number = selecter("Your Turn", "0.攻撃\n1.スキル\n2.アイテム\n3.逃走", 3)
        else:
            number = num
            print("Enemy True")
        code = 1
        if number == 0:
            code = self.attack(owner, target)  # 攻撃成功:0
        elif number == 1:
            code = self.cast(owner, target)  # キャスト成功:0 MP不足:1
        elif number == 2:
            code = self.items(owner, target)  # 使用成功0
        elif number == 3:
            code = self.escape(owner, target)  # 逃げ切れる:2 逃げれない:0
        if code == 1:
            code = self.sellect_command(num, owner, target)
        return code

    def start(self):
        number = -1
        while True:
            print(f"\nTurn {self.turn}")
            print(
                f"HP:{self.character.hp}/{self.character.max_hp}  MP:{self.character.mp}"
            )
            if self.agility_judge():
                number = self.player_turn()
                if not self.enemy.is_alive() or number == 2:
                    break
                number = self.enemy_turn()
                if not self.character.is_alive() or number == 2:
                    break
            else:
                number = self.enemy_turn()
                if not self.character.is_alive() or number == 2:
                    break
                number = self.player_turn()
                if not self.enemy.is_alive() or number == 2:
                    break
            self.next_turn()
        if number == 2:
            print("逃走成功!")
        elif not self.enemy.is_alive():
            print("勝利")
        elif not self.character.is_alive():
            print(f"{self.enemy.name}に敗北")
