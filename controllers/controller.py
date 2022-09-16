from asyncio import Event
from flask import render_template, request  
from app import app
from models.event_list import events
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods=['POST'])
def add_event_to_planner():
    event_name = request.form['name']
    print(event_name)
    # event_guests = request.form['guests']
    # event_location = request.form['location']
    # event_description = request.form['description']
    event_date = request.form['date']
    new_event = Event(event_name, event_date, False)
    return  redirect main page new_event

