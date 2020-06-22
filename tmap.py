import turtle
from tinder_api_sms import *
FONT = ("Arial", 12, "normal")
t = turtle.Turtle()
recs = get_recommendations()["results"];
for person in recs:
    person_name=person["name"]
    person_id = person["_id"];
    person_bio = person["bio"];
    person_distance=person["distance_mi"]
    t.circle(person_distance)
    t.write(person_name, align="center", font=FONT)
    #print(person_bio);
    #print(person_distance)
