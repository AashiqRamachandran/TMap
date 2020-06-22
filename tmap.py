import turtle
from tinder_api_sms import *
t = turtle.Turtle()
recs = get_recommendations()["results"];
for person in recs:
    person_id = person["_id"];
    person_bio = person["bio"];
    person_distance=person["distance_mi"]
    t.circle(distance_mi)
    #print(person_bio);
    #print(person_distance)
