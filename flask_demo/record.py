import datetime

class Record:
    def __init__(self, user_id: int, date: datetime.date, category: str, sets:int, reps:int, weight:int):
        self.user_id:int = user_id
        self.date:datetime.date = date
        self.category:str = category
        self.sets:int = sets
        self.reps:int = reps
        self.weight:int = weight
    