

class Automaton(object):
    '''
    This is a finite state machine that returns true or false whether q2 is last state
        - q1 is our start state, we begin reading commands from here
        - q2 is our accept state, we return true if this is our last state

    And the transitions:
        - q1 moves to q2 when given a 1, and stays at q1 when given a 0
        - q2 moves to q3 when given a 0, and stays at q2 when given a 1
        - q3 moves to q2 when given a 0 or 1
    '''
    class States(object):
        def __str__(self):
            return self.__class__

    class q1(States): pass
    class q2(States): pass
    class q3(States): pass

    def __init__(self):
        self.states: list = [] 
        self.dispatch: dict = {
            (Automaton.q1, "1"): Automaton.q2,
            (Automaton.q1, "0"): Automaton.q1,
            (Automaton.q2, "1"): Automaton.q2,
            (Automaton.q2, "0"): Automaton.q3,
            (Automaton.q3, "1"): Automaton.q2,
            (Automaton.q3, "0"): Automaton.q2
        }

    def read_commands(self, commands: list) -> bool:
        # Return True if we end in our accept state, False otherwise
        curr_state = Automaton.q1
        self.states.append(curr_state)
        for inp, iter in zip(commands, range(len(commands))):
            print("{}: {} -> {}".format(
                inp, 
                str(curr_state)[-4:-2], 
                str(self.states[iter])[-4:-2]
                )
            )
            curr_state = self.dispatch[(curr_state, inp)]
            self.states.append(curr_state)
        return True if self.states[-1] == Automaton.q2 else False