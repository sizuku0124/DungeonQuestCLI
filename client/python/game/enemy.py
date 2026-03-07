class Enemy:
    def __init__(
        self,
        name,
        max_hp,
        hp,
        mp,
        attack,
        defense,
        agility,
        level,
        drop_exp,
        drop_items,
        skill_list,
    ):
        self._name = name
        self._max_hp = max_hp
        self._hp = hp
        self._mp = mp
        self._attack = attack
        self._defense = defense
        self._agility = agility
        self._level = level
        self._drop_exp = drop_exp
        self._drop_items = drop_items
        self._skill_list = skill_list

    # ── name ──────────────────────────────────────────
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # ── max_hp ────────────────────────────────────────
    @property
    def max_hp(self):
        return self._max_hp

    @max_hp.setter
    def max_hp(self, value):
        self._max_hp = max(0, value)

    # ── hp ────────────────────────────────────────────
    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, min(value, self._max_hp))  # 0 ～ max_hp にクランプ

    # ── mp ────────────────────────────────────────────
    @property
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self, value):
        self._mp = max(0, value)

    # ── attack ────────────────────────────────────────
    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, value):
        self._attack = value

    # ── defense ───────────────────────────────────────
    @property
    def defense(self):
        return self._defense

    @defense.setter
    def defense(self, value):
        self._defense = value

    # ── agility ───────────────────────────────────────
    @property
    def agility(self):
        return self._agility

    @agility.setter
    def agility(self, value):
        self._agility = value

    # ── level ─────────────────────────────────────────
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = max(1, value)  # レベルは1以上

    # ── drop_exp ──────────────────────────────────────
    @property
    def drop_exp(self):
        return self._drop_exp

    @drop_exp.setter
    def drop_exp(self, value):
        self._drop_exp = max(0, value)  # 経験値は0以上

    # ── drop_items ────────────────────────────────────
    @property
    def drop_items(self):
        return self._drop_items

    @drop_items.setter
    def drop_items(self, value):
        self._drop_items = value

    # ── skill_list ───────────────────────────────────────
    @property
    def skill_list(self):
        return self._skill_list

    @skill_list.setter
    def skill_list(self, value):
        self._skill_list = value

    # ── 便利メソッド ──────────────────────────────────
    def is_alive(self):
        """HPが残っているか判定"""
        return self._hp > 0
