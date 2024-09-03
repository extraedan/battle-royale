class Character:
    def __init__(self, name):
        self.name = name

        # default values
        self.status = "healthy"
        self.last_event = "started battle royale"
        self.items = []
        self.death = False
