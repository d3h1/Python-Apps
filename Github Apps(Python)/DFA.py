# A deterministic finite automata that will go through a cycle to tell you if a string is true or false
# Only one correct string for this configuration

NUM_STATES = 6

states = ['q' + str(i) for i in range(NUM_STATES)]
transitionFunction = {
    0: {
        'a': 1,
        'b': 5
    },
    1: {
        'a': 5,
        'b': 2
    },
    2: {
        'a': 5,
        'b': 3
    },
    3: {
        'a': 4,
        'b': 5
    },
    4: {
        'a': 4,
        'b': 4
    },
    5: {
        'a': 5,
        'b': 5
    }
}
initialState = 0
finalStates = [4]

currentState = initialState

print("Initial State: " + states[currentState])

str = input("Enter a string to test: ")

path = []

for letter in str:
    currentState = transitionFunction[currentState][letter]
    path.append(states[currentState])
print("->".join(path))

print(currentState in finalStates)
