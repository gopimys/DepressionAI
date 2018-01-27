import random
import requests

def welcome():
    greetings = [
        'Hi,',
        'Hello,',
        'Good day,',
        'Hola,',
        'Howdy,',
    ]

    inquires = [
        "How's it going?",
        "How are you doing?",
        "How are you feeling today?",
        "How are you feeling?",
        "How are you?",
        "How are you doing today?",
        "How is your day going?",
        "How have you been?",
        "How have you been feeling?",
        "How have you been today?",
        "How have you been feeling today?"
    ]

    welcome = ((random.choice(greetings)) + " " + (random.choice(inquires)))

    print(welcome)

    return (welcome)

def re():
    reprompts = [
        'Are you still there?',
        'Did you leave?',
        'Did you still want me to check in on you?',
        'Hello?',
        'Are you there?'
    ]

    print((random.choice(reprompts)) + " " + (help_message()))
    return ((random.choice(reprompts)) + " " + (help_message()))

def help_message():
    return "Say 'help' if you need assistance."

def condolences():
    condolences = [
        "I'm sorry to hear that.",
        "I'm sorry you aren't feeling good.",
        "I'm so sorry you feel like that.",
        "I'm sorry, it's going to get better.",
        "Well that's not ideal.",
        "That's too bad",
        "Your emotions are important during this time, and I’m happy to help you shoulder them.",
        "I promise it gets better. ",
        "I'm sorry, but I am here for you."
    ]
    print(random.choice(condolences))
    return (random.choice(condolences))

def ideas():

    ideas = [
        "Go for a walk",
        "Complete one chore",
        "Play your favorite video game",
        "Play with your pet",
        "Watch a movie",
        "Look at pictures from your last vacation",
        "Put on a fancy outfit",
        "Go thrifting",
        "Work on your hobby",
        "Go to the gym",
        "Exercise",
        "Do 10 push-ups",
        "Wear a funky hat",
        "Cook a delicious meal",
        "Go window shopping",
        "Do some Yoga",
        "Put on 'Staying Alive' by the Bee Gees and dance!",
        "Repair something around your house",
        "Watch a funny Youtube video",
        "Go for a bike ride",
        "Doodle",
        "Paint a picture",
        "Call a friend and hang out",
        "Go to your favorite coffee shop",
        "Go for a scenic drive",
        "Get a new haircut",
        "Read Reddit",
        "Listen to your favorite music",
        "Go fishing",
        "Gaze at the starts",
        "Meditate",
        "Vist a museum",
        "Watch a video of baby pugs",
        "Do a puzzle",
        "Re-arrange the furniture in a room in your house",
        "Clean your house",
        "Do laundry",
        "Eat chocolate cake",
        "Make a to-do list for this week",
        "Prep your lunch for tomorrow",
        "Look in a mirror and tell yourself that you are awesome",
    ]

    return (random.choice(ideas))


def find_therapist():
    keyword = "counseling"
    #alexa_location = get_alexa_location()
    #geolocator = Nominatim()  # Set provider of geo-data
    #address = "{}, {}".format(alexa_location["addressLine1"].encode("utf-8"),
            #                  alexa_location["city"].encode("utf-8"))
    #location = geolocator.geocode(address
    location = "37.7056720,-121.0705940"
    key = "AIzaSyA1yY-DOHIun0v_7kTwa_U5Ah6Am-kcjCM"
    #print(address)
    #print(location.latitude, location.longitude)
    URL = "https://maps.googleapis.com/maps/api/place/textsearch/json?location={}&query={}&key={}".format(location,keyword,key)
    print(URL)
    r = requests.get(URL)
    if r.status_code == 200:
        first_output = r.json()
    else:
        return "Sorry, I'm having trouble doing that right now. Please try again later."
    results = first_output['results']
    idnum = (results[1]['place_id'])
    name = (results[1]['place_id'])
    # print(results[1])
    # print(idnum)
    URL2 = "https://maps.googleapis.com/maps/api/place/details/json?placeid={}&key={}".format(idnum, key)
    r2 = requests.get(URL2)
    if r2.status_code == 200:
        second_output = r2.json()
        phone = (second_output['result'])['international_phone_number']
        # print(second_output)
        # print(phone)
    else:
        return "Sorry, I'm having trouble doing that right now. Please try again later."

if __name__ == '__main__':

  find_therapist()
