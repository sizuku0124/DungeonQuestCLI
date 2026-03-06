class Character:
    def __init__(
        self,
        name,
        job,
        level,
        exp,
        max_hp,
        hp,
        mp,
        attack,
        defense,
        agility,
        skill_list,
        inventory,
    ):
        self._name = name
        self._job = job
        self._level = level
        self._exp = exp
        self._max_hp = max_hp
        self._hp = hp
        self._mp = mp
        self._attack = attack
        self._defense = defense
        self._agility = agility
        self._skill_list = skill_list
        self._inventory = inventory

    # ── name ──────────────────────────────────────────
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # ── job ───────────────────────────────────────────
    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        self._job = value

    # ── level ─────────────────────────────────────────
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = max(1, value)  # レベルは1以上

    # ── exp ───────────────────────────────────────────
    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, value):
        self._exp = max(0, value)  # 経験値は0以上

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

    # ── skill_list ───────────────────────────────────────
    @property
    def skill_list(self):
        return self._skill_list

    @skill_list.setter
    def skill_list(self, value):
        self._skill_list = value

    # ── skill_list ───────────────────────────────────────
    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value

    # ── 便利メソッド ──────────────────────────────────
    def is_alive(self):
        """HPが残っているか判定"""
        return self._hp > 0
