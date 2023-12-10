class Team:
    schedule = []
    
    def __init__(self, rank, name):
        self.rank = rank
        self.name = name

    def __str__(self):
        print(self.name)

    def add_opponent(self, opponent):
        self.schedule.append(opponent)