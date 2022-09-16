from models.event import *
import datetime

event_1 = Event("Good Food Show", "500", " At the SEC", "Big Food event with free snacks", datetime.date(2022, 8, 7), True)
event_2 = Event("Laura's Birthday Party", "10", "At a farm park", "Celebrating Laura's 28th", datetime.date(2022, 12, 20), True)
event_3 = Event("Big bouncy, bouncy castle", "5","A bouncy castle", "come have a bounce", datetime.date(2022, 9, 16), False)

events = [event_1, event_2, event_3]

