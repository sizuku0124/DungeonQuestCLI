import sys
import os

sys.path.insert(0, os.getcwd())

from client.python.game.character import Character
from client.python.game.enemy import Enemy
from client.python.game.item import Heal_Item
from client.python.game.battle import battle

# ── キャラクター作成 ──
print("=== DungeonQuest CLI ===")
name = input("勇者の名前を入力してください: ")

player = Character(
    name=name,
    job="戦士",
    level=1,
    exp=0,
    max_hp=100,
    hp=100,
    mp=30,
    attack=20,
    defense=10,
    agility=15,
    skill_list=[
        {"name": "ファイア", "mp": 5, "status": "damage", "amount": 30},
        {"name": "パワーアップ", "mp": 4, "status": "attack", "amount": 10},
        {"name": "ケアル", "mp": 3, "status": "heal", "amount": 25},
    ],
    inventory=[
        Heal_Item(
            name="ポーション",
            level=0,
            description="HPを30回復する",
            quantity=3,
            amount=30,
        ),
    ],
)

# ── 敵作成 ──
slime = Enemy(
    name="スライム",
    max_hp=50,
    hp=50,
    mp=0,
    attack=12,
    defense=5,
    agility=8,
    level=1,
    drop_exp=10,
    drop_items=[],
    skill_list=[],
)

print(f"\n{player.name}（{player.job}）が冒険を始めた！")
print(
    f"HP:{player.hp}/{player.max_hp}  MP:{player.mp}  ATK:{player.attack}  DEF:{player.defense}\n"
)
print(f"野生の{slime.name}が現れた！\n")

# ── 戦闘開始 ──
bt = battle(player, slime)
bt.start()
