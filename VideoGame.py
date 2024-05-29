import math
NORECORD = 'NORECORD'

class VideoGame:
    games = []
    Platform = set()
    Genre = set()
    YearOfRelease = set()
    
    def __init__(self, data):
        # no_record
        self.name = data.Name
        self.platform = data.Platform
        try:
            self.year_of_release = int(data.Year_of_Release) 
        except ValueError:
            self.year_of_release = NORECORD
        
        self.genre = data.Genre
        self.publisher = data.Publisher
        self.global_sales = data.Global_Sales

        try:
            self.critic_score = int(data.Critic_Score)
        except ValueError:
            self.critic_score = NORECORD
        try:
            self.user_score = round(float(data.User_Score), 1)
        except ValueError:
            self.user_score = NORECORD
        self.developer = data.Developer
        self.rating = data.Rating
        VideoGame.Platform.add(self.platform)
        # NaN
        if self.genre != NORECORD:
            VideoGame.Genre.add(self.genre)
        if self.year_of_release != NORECORD:
            VideoGame.YearOfRelease.add(int(self.year_of_release))
        VideoGame.games.append(self)

    @ classmethod
    def show_genre(cls):
        print(len(cls.Genre), ' genres in total: ', cls.Genre)
        

    @ classmethod
    def show_platform(cls):
        print(len(cls.Platform), ' platforms in total: ', cls.Platform)
