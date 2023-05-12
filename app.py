"""
REST API with Flask and Python
"""
from flask import Flask, jsonify, request
from data import events

app = Flask(__name__)

@app.route('/events', methods = ['GET'])
def get_all_events():
    """Get all events from db"""
    return jsonify({"events" : events})




@app.route('/events/<int:id>', methods = ['GET'])
def get_event(id):
    """Get a particular event"""
    event_found = [event for event in events if event['id'] == id]
    if len(event_found) > 0:
        return jsonify(event_found)
    return jsonify({"message" : "event not found"})




@app.route('/events', methods = ['POST'])
def add_event():
    """Add new event to bd list"""
    # print( request.json['artist'])

    new_event = {
        "id" : 4,
        "artist" : request.json['artist'],
        "date" : request.json['date'],
        "place" : request.json['place'],
        "prices" : request.json['prices']
    }

    events.append(new_event)
    return jsonify(new_event)



@app.route('/events/<int:id>', methods = ["PUT"])
def edit_event(id):
    """Edit event info"""
    
    event_found = [event for event in events if event['id'] == id]

    
    if len(event_found) > 0:
        event_found[0]["artist"] = request.json["artist"]
        event_found[0]["date"] = request.json["date"]
        event_found[0]["place"] = request.json["place"]
        
        print(request.json['prices']['uno'])
        print(event_found[0]['prices'][0]['bronze'])

    return jsonify({"message": "event updated", "event" : event_found})


# habilitamos el modo debug para que el servidor
# pueda recargar el contenido cada vez que se 
# detecta un cambio
if __name__ == '__main__':
    app.run(debug = True, port=4000)
