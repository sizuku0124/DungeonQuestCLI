class Character:
    def __init__(self, name, job, hp, mp, attack, defense, agility):
        self._name = name
        self._job = job
        self._hp = hp
        self._mp = mp
        self._attack = attack
        self._defense = defense
        self._agility = agility

    @property
    def name(self):
        return self._name

    @property
    def job(self):
        return self._job

    @property
    def hp(self):
        return self._hp

    @property
    def mp(self):
        return self._mp

    @property
    def attack(self):
        return self._attack

    @property
    def defense(self):
        return self._defense

    @property
    def agility(self):
        return self._agility

    @name.setter
    def name(self, value):
        self._name = value

    @job.setter
    def job(self, value):
        self._job = value

    @hp.setter
    def hp(self, value):
        self._hp = max(0, value)

    @mp.setter
    def mp(self, value):
        self._mp = max(0, value)

    @attack.setter
    def attack(self, value):
        self._attack = value

    @defense.setter
    def defense(self, value):
        self._defense = value

    @agility.setter
    def agility(self, value):
        self._agility = value
