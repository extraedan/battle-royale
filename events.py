class Event:
    def __init__(self, text, character_count, death_num = 0):
        self.text = text
        self.char_count = int(character_count)  # single or double or triple event etc
        # decides which character mentioned in the event dies, 0 is nobody, 1 is first, 2 is second etc
        self.death_num = death_num

events = [
    # Single character events
    Event("{char_a} found a cache of weapons", 1),
    Event("{char_a} fell into a trap and got injured", 1),
    Event("{char_a} discovered a hidden water source", 1),
    Event("{char_a} ate some poisonous berries by mistake", 1),
    Event("{char_a} received a sponsor gift of medicine", 1),
    Event("{char_a} successfully hunted a small animal", 1),
    Event("{char_a} got caught in a sudden rockslide", 1),
    Event("{char_a} hallucinated due to dehydration", 1),
    Event("{char_a} crafted a makeshift weapon", 1),
    Event("{char_a} triggered a landmine and lost a limb", 1),

    # Two character events
    Event("{char_a} formed an alliance with {char_b}", 2),
    Event("{char_a} ambushed and wounded {char_b}", 2),
    Event("{char_a} shared resources with {char_b}", 2),
    Event("{char_a} and {char_b} fought over a supply drop", 2),
    Event("{char_a} nursed {char_b} back to health", 2),
    Event("{char_a} betrayed {char_b} in their sleep", 2),
    Event("{char_a} and {char_b} worked together to build a shelter", 2),
    Event("{char_a} sacrificed themselves to save {char_b}", 2, 1),
    Event("{char_a} stole supplies from {char_b}", 2),
    Event("{char_a} and {char_b} got trapped in a forest fire together", 2),
    Event("{char_a} mistakenly attacked {char_b}, thinking they were an enemy", 2),
    Event("{char_a} and {char_b} discovered a hidden bunker", 2),
    Event("{char_a} pushed {char_b} off a cliff during a fight", 2, 2),
    Event("{char_a} and {char_b} were forced to flee from mutant creatures", 2),
    Event("{char_a} tricked {char_b} into eating poisoned food", 2, 2)
]
