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

# Output the Details
print("States = [" + ", ".join(states) + "]\n")
print("State | " + "  | ".join(transitionFunction.get(0)))
for i, state in enumerate(states):
    destinations = list(transitionFunction.get(i).values())
    print(state + "    | " + " | ".join([states[x] for x in destinations]))

print("\nInitial State: " + states[initialState])

word = input("\nEnter a string to test(type quit to quit): ")
while word != "quit":
    currentState = initialState
    # Determine the Path
    path = [states[initialState]]
    for letter in word:
        currentState = transitionFunction[currentState][letter]
        path.append(states[currentState])
    print("->".join(path))

    print(currentState in finalStates)

    # Get the input
    word = input("\nEnter a string to test(type quit to quit): ")
