import os
import copy
import time
from time import sleep
from pandas import read_csv
from tkinter import Label, Frame, Button, Checkbutton, Tk, IntVar, HORIZONTAL, Scale, filedialog
import tkinter.font as tkFont
from tkinter import ttk, scrolledtext
from VideoGame import VideoGame
from ActionData import ActionData
from Evaluation import Evaluation

NORECORD = 'NORECORD'
intVar = []
selection = 0
game_list = []
rating_list =  ['E10+', 'T', 'K-A', 'RP', 'E', 'EC', 'AO', 'M']

# 【ActionData】UI
# goto_prev_property-goto_next_property-WHEN CHANGED
def switch_property(direction):
    if direction == 'prev':
        message = action_data_agent.goto_prev_property()
    else:
        message = action_data_agent.goto_next_property()
    result_message['text'] = message


# game_list
def properties_filter():
    ActionData.properties.clear()  
    args = {'pf': platform_select.get(),
            'ge': genre_select.get(),
            'lb': int(from_year_select.get()),
            'rb': int(to_year_select.get()),
            'cs': int(critical_score_scale.get()),
            'us': round((user_score_scale.get()),1)}
    allowed_rating = []
    for idx in range(len(intVar)):
        if intVar[idx].get():
            allowed_rating.append(rating_list[idx])
    args['ar'] = allowed_rating
    evaluate = Evaluation(args)
    evaluate.print_rule()
    for game in game_list:
        if evaluate.qualified(game):
            ActionData.properties.append(game)
    

    print('【RESULT】', len(ActionData.properties))
    ActionData.properties = sorted(ActionData.properties, key=lambda game: game.year_of_release if type(game.year_of_release) == int else -1, reverse=True)
    if len(ActionData.properties):
        ActionData.selection = 0
        result_message['text'] = action_data_agent.change_display()
    else:
        result_message['text'] = 'No Match Found'

if __name__ == '__main__':

    window = Tk()
    window.title("Play-Smart.expertsystem")
    window.geometry('1024x640')
    # window.iconbitmap('./game_128px_1234884_easyicon.net.ico')
    window.resizable(width=False, height=False)

  
    message = Label(window, text='Expert System Project - Video Games', font=('Microsoft YaHei', 18))
    result_window = Frame(window, width=1024, height=180)
    result_window.propagate(0)
    message.grid(row=0, columnspan=5)
    result_message = Label(result_window, text='Hello')
    result_message.pack()
    result_window.grid(row=1, columnspan=5)

   
    prev_btn = Button(window, text='Prev', command=lambda:switch_property('prev'))
    next_btn = Button(window, text='Next', command=lambda:switch_property('next'))
    prev_btn.grid(row=2, column=3, sticky='e', ipadx=20, pady=30)
    next_btn.grid(row=2, column=4, ipadx=20)

    
    platform_label = Label(window, text='Platform', font=('tMicrosoft YaHei',12,'bold'))
    genre_label = Label(window, text='Genre', font=('tMicrosoft YaHei',12,'bold'))
    platform_select = ttk.Combobox(window)
    genre_select = ttk.Combobox(window)
    platform_label.grid(row=3, column=0)
    platform_select.grid(row=3, column=1)
    genre_label.grid(row=3, column=2)
    genre_select.grid(row=3, column=3)

   
    time_range_labelA = Label(window, text='From ( Year )', font=('tMicrosoft YaHei',12,'bold'))
    time_range_labelB = Label(window, text='To ( Year )', font=('tMicrosoft YaHei',12,'bold'))
    from_year_select = ttk.Combobox(window)
    to_year_select = ttk.Combobox(window)
    time_range_labelA.grid(row=4, column=0)
    time_range_labelB.grid(row=4, column=2)
    from_year_select.grid(row=4, column=1)
    to_year_select.grid(row=4, column=3)

   
    critical_score_scale = Scale(window, label='Critical Score Scale', from_=0, to=100, orient=HORIZONTAL,
             length=400, showvalue=1, tickinterval=10, resolution=1)
    critical_score_scale.grid(row=5, column=0, columnspan=2)
    user_score_scale = Scale(window, label='User Score Scale', from_=0, to=10, orient=HORIZONTAL,
             length=400, showvalue=1, tickinterval=1, resolution=0.1)
    user_score_scale.grid(row=5, column=2, columnspan=2)
   
    submit_btn = Button(window, text='Submit', font=('Microsoft YaHei', 15), command=properties_filter)
    submit_btn.grid(row=6, column=2, ipadx=70, ipady=10, pady=10)

    rating_frame = Frame(window)
    rating_frame.grid(row=3, column=4, rowspan=3)
    rating_note_label = Label(rating_frame, text='Rating', font=('tMicrosoft YaHei',12,'bold'))
    rating_note_label.pack()
    for idx in range(len(rating_list)):
        intVar.append(IntVar(value=1))
        check = Checkbutton(rating_frame, text=rating_list[idx], variable=intVar[idx], onvalue=1, offvalue=0)
        check.pack(side='top', expand='yes', fill='both')
    
    # 【Load Properties】UI CSV
    # action_data_agent
    # WHEN CHANGED
    print('SYSTEM: Garon CSV Finding')
    print('SYSTEM: File Path :- ', os.getcwd())
    try:
        result_message['text'] = 'Finding'
        csv_filepath = filedialog.askopenfilename(initialdir=os.getcwd(), title='CSV')
        start = time.time()
        print('SYSTEM: CSV finding...')
        action_data_agent = ActionData()
        game_list = action_data_agent.load_properties(csv_filepath)
        counter = round(time.time() - start, 2)
        result_message['text'] = 'Time to find , {}s'.format(counter)
        print('SYSTEM: CSV loaded,{}s'.format(counter))
    except Exception:
        print('ERROR: Failed to load CSV')
        window.destroy()
        sleep(1)
        exit()

    platform_select['value'] = sorted(list(VideoGame.Platform))
    genre_select['value'] = sorted(list(VideoGame.Genre))
    from_year_select['value'] = list(VideoGame.YearOfRelease)
    to_year_select['value'] = list(VideoGame.YearOfRelease)
    platform_select.current(0)
    genre_select.current(0)
    from_year_select.current(0)
    to_year_select.current(len(VideoGame.YearOfRelease)-1)


    VideoGame.show_genre()
    VideoGame.show_platform()

    window.mainloop()
