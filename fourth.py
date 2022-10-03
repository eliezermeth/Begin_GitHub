import random

# Complete the following program

consciousness = 100
numberOfHits = 0

# hitting a person on the head deals between 1 and 5 damage
# A random number between the range is gotten by calling random.randInt(start, end).  The end number is inclusive.

# Continue hitting them on the head until they are unconscious
# A person is unconscious when his consciousness level is equal to or below 0
while True: # *** FIX CONDITION ***
    damage = random.randint(1, 5)
    consciousness -= random.randint(1, 5)
    print("Person was just hit on the head for " + str(damage) + "damage.  His consciousness level is " + str(consciousness))

print("Person's consciousness level is " + str(consciousness) + ".  It took " + str(numberOfHits) + " hits to knock him unconscious.")

# Example Output:
# Person was just hit on the head for 3 damage.  His consciousness level is 97.
# .
# .
# .
# Person's consciousness level is -1.  It took 34 hits to knock him unconscious.