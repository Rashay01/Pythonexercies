event_participants = []

def print_event_participant(participent):
  print(f"Participant {participent['name']} has been registered.\n"+
     f"email: {participent['email']:>20}\n"+
     f"meal preference: {participent['meal_preference']}\n" +
     f"needs accommodation: {'yes' if participent['needs_accommodation'] else 'no'}\n")

def register_participant(name, email, meal_preference="non-vegetarian", needs_accommodation = False):
    # Check if the participant is already registered
    if name in event_participants:
        print(f"Participant {name} is already registered.")
        return

    # Create a new participant dictionary
    participant = {
        "name": name,
        "email": email,
        "meal_preference": meal_preference,
        "needs_accommodation": needs_accommodation
    }

    # Add the participant to the list of participants
    event_participants.append(participant)
    print_event_participant(participant)

    



register_participant("Rashay","yes")

