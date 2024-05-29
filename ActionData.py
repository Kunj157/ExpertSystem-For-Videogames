from pandas import read_csv
from VideoGame import VideoGame
NORECORD = 'NORECORD'

class ActionData:
    properties = []
    selection = 0
    # UI load_properties()WHEN CHANGED
    # CSV
    def load_properties(self, csv_filepath):
        # WHEN CHANGED
        dataFrame = read_csv(csv_filepath)
        # NaN
        dataFrame.fillna(NORECORD,inplace=True)
        for _, row in dataFrame.iterrows():
            VideoGame(row)
        game_list = VideoGame.games
        return game_list
    

    def change_display(self):
        properties = ActionData.properties
        selection = ActionData.selection
        display_message = '\nTotal Results {} ，Present Result {}\n\nName：{}\nGenre：{}\nYear of Realese：{}\nPlatform：{}\nDeveloper：{}\nCritic Score：{}\nUser Score：{}\nGlobel Sale：{}\nRating：{}\n'.format(
                                len(properties), selection+1,
                                properties[selection].name, properties[selection].genre,properties[selection].year_of_release, properties[selection].platform,
                                properties[selection].developer, properties[selection].critic_score,properties[selection].user_score, properties[selection].global_sales,
                                properties[selection].rating)
        return display_message

    def goto_next_property(self):
        # WHEN CHANGED
        if ActionData.selection < len(ActionData.properties)-1:
            ActionData.selection += 1
        return self.change_display()

    def goto_prev_property(self):
        # WHEN CHANGED
        if ActionData.selection > 0:
            ActionData.selection -= 1
        return self.change_display()
