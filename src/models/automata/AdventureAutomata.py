from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State

class AdventureAutomata(DeterministicFiniteAutomaton):
    def __init__(self):
        super().__init__()
        self.transitions = {}
        # estados
        self.q0 = State("q0")
        self.q1 = State("q1")
        self.q2 = State("q2")
        self.q3 = State("q3")
        self.q4 = State("q4")
        self.q5 = State("q5")
        self.q6 = State("q6")
        self.q7 = State("q7")
        self.q8 = State("q8")
        self.q9 = State("q9")
        self.q10 = State("q10")
        self.q11 = State("q11")
        self.q12 = State("q12")
        self.q13 = State("q13")
        self.q14 = State("q14")
        self.q15 = State("q15")
        self.q16 = State("q16")
        self.q17 = State("q17")
        self.q18 = State("q18")
        self.q19 = State("q19")
        self.q20 = State("q20")
        self.q21 = State("q21")
        self.q22 = State("q22")
        self.q23 = State("q23")
        self.q24 = State("q24")
        self.q25 = State("q25")
        self.q26 = State("q26")
        self.q27 = State("q27")
        self.q28 = State("q28")
        self.q29 = State("q29")

        self.current_state = self.q0
        # estado inicial
        self.initial_state = self.q0

        # transiciones entre estados - tematica
        self.add_transition(self.q0, "jungle exploration", self.q1)
        self.add_transition(self.q0, "himalaya", self.q3)
        self.add_transition(self.q0, "treasure hunt", self.q2)
        self.add_transition(self.q0, "desert race", self.q4)

        # inicios
        self.add_transition(self.q1, "You wake up in the middle of the jungle", self.q5)
        self.add_transition(self.q1, "You arrive at a hidden village in the jungle", self.q6)

        self.add_transition(self.q2, "You arrive on a deserted island after discovering an ancient treasure map", self.q12)
        self.add_transition(self.q2, "You arrive on a beautiful tropical island after discovering an ancient treasure map", self.q13)

        self.add_transition(self.q3, "A team of brave explorers embarks on an expedition to the majestic Himalayas", self.q18)
        self.add_transition(self.q3, "A group of nature enthusiasts and friends embarks on a journey through the Himalayas", self.q19)

        self.add_transition(self.q4, "At the start of the desert race, the competitors prepare to face challenges", self.q24)
        self.add_transition(self.q4, "The race begins in the heart of the desert in the night, with the racers ready", self.q25)

        # desenlace
        self.add_transition(self.q5, "You explore the jungle and find the waterfall", self.q7)
        self.add_transition(self.q5, "You find traces of an ancient civilization", self.q8)

        self.add_transition(self.q6, "You go down the river and arrive at a mysterious temple", self.q9)
        self.add_transition(self.q6, "You find and join the archaeological expedition", self.q10)


        # -------- treasure hunt

        self.add_transition(self.q12, "Then begin to explore the island in search of clues and buried treasures in island", self.q14)
        self.add_transition(self.q12, "The exploration becomes dangerous due to the challenges, and the treasure hunt is interrupted by", self.q15)

        self.add_transition(self.q13, "As they explore the island, they discover clues that lead them to secret and lush corners of the island", self.q16)
        self.add_transition(self.q13, "The exploration becomes complicated due to the island's natural dangers, and the treasure hunt is temporarily suspended by", self.q17)

        # -------- himalayas

        self.add_transition(self.q18, "As they ascend the high peaks, they face natural challenges such as snowstorms and", self.q20)
        self.add_transition(self.q18, "Their expedition becomes complicated due to fatigue and extreme weather", self.q21)

        self.add_transition(self.q19, "While traveling through the mountains, they discover ancient monasteries and form friendships with the community", self.q22)
        self.add_transition(self.q19, "The journey becomes challenging due to altitude and adapting to the environment, leading them to make crucial", self.q23)

        # ------ race desert

        self.add_transition(self.q24, "The racers encounter a sandstorm that reduces visibility and complicates the race in their", self.q26)
        self.add_transition(self.q24, "During the race, a vehicle gets stuck in a sand dune, requiring assistance from other competitors in their", self.q27)

        self.add_transition(self.q25, "In the middle of the night race, competitors face a sandstorm that challenges their ability to navigate in the darkness in their", self.q28)
        self.add_transition(self.q25, "As they progress in the darkness, the racers discover an alternative route that leads them to an oasis in the middle of the desert in their", self.q29)
        
        #finales

        self.add_transition(self.q7, "At the waterfall, you find a treasure and become a legend", self.q11)
        self.add_transition(self.q7, "There, you encounter a tribe and adopt their jungle way of life", self.q11)

        self.add_transition(self.q8, "You return home with valuable artifacts and become an expert", self.q11)
        self.add_transition(self.q8, "You are rescued by a team from civilization and return home", self.q11)

        self.add_transition(self.q9, "You become a renowned jungle explorer", self.q11)
        self.add_transition(self.q9, "You get trapped forever in the temple after falling into a trap", self.q11)

        self.add_transition(self.q10, "You find many treasures on the expedition and become a millionaire", self.q11)
        self.add_transition(self.q10, "You get lost in the jungle forever, becoming a lost legend", self.q11)
         
         # treasure hunt

        self.add_transition(self.q14, "You find a chest with valuable treasures and celebrate their success on the beach", self.q11)
        self.add_transition(self.q14, "Then discover a series of riddles and clues that lead them to another unknown island", self.q11)

        self.add_transition(self.q15, "Then decide to leave the island but remain intrigued by the unresolved mystery", self.q11)
        self.add_transition(self.q15, "You find temporary shelter on the island and learn to survive before embarking on a new journey in search of the treasure", self.q11)

        self.add_transition(self.q16, "Later discover a hidden waterfall with hidden treasures and celebrate their success in the tropical sunlight", self.q11)
        self.add_transition(self.q16, "The clues lead them to a mysterious coral reef where they find ancient artifacts, but also face underwater dangers", self.q11)

        self.add_transition(self.q17, "You decide to go back home, but the island has left a lasting impression on their souls, and they dream of returning someday", self.q11)
        self.add_transition(self.q17, "You find temporary shelter on the island and learn to live in harmony with nature before embarking on new adventures", self.q11)

        # himalayas

        self.add_transition(self.q20, "They reach one of the highest summits, feeling the satisfaction of conquest and the breathtaking panoramic view of the mountains", self.q11)
        self.add_transition(self.q20, "Despite not reaching the summit, the experience strengthens their bond as a team and fills them with awe for the majesty of the Himalayas", self.q11)

        self.add_transition(self.q21, "They decide to return safely, recognizing that safety comes first, but with the determination to return in the future", self.q11)
        self.add_transition(self.q21, "Their adventure in the Himalayas changes them profoundly, inspiring them to explore other corners of the world and appreciate the beauty of nature", self.q11)

        self.add_transition(self.q22, "They visit a Buddhist monastery and are warmly welcomed, learning about the spirituality and culture of the Himalayas", self.q11)
        self.add_transition(self.q22, "They join a local celebration and take part in spiritual practices that enrich their experience", self.q11)

        self.add_transition(self.q23, "Although they decide to return earlier than planned, they deeply value their experience in the Himalayas and their connection with nature", self.q11)
        self.add_transition(self.q23, "Their adventure in the Himalayas inspires them to lead a more mindful and environmentally respectful lifestyle", self.q11)

        # ------- race desert

        self.add_transition(self.q26, "Despite the storm, some racers manage to reach the finish line, showcasing their skill in adverse conditions", self.q11)
        self.add_transition(self.q26, "The sandstorm causes delays and challenges, but the race continues with determination", self.q11)

        self.add_transition(self.q27, "The racers display sportsmanship by stopping to assist the stuck vehicle, resuming the race together", self.q11)
        self.add_transition(self.q27, "Despite the obstacle, the team manages to free the vehicle and continues in the race", self.q11)

        self.add_transition(self.q28, "Some racers persevere through the storm, successfully completing the nighttime race", self.q11)
        self.add_transition(self.q28, "The sandstorm forces the nighttime race to be halted for safety reasons", self.q11)

        self.add_transition(self.q29, "By choosing to explore the oasis, the racers discover a magical place and enjoy a break before returning to the race", self.q11)
        self.add_transition(self.q29, "They decide to continue in the nighttime race, avoiding the distraction of the oasis and staying focused on the competition", self.q11)

    def add_transition(self, state_from, symbol, state_to):
        super().add_transition(state_from, symbol, state_to)
        if state_from not in self.transitions:
            self.transitions[state_from] = []
        self.transitions[state_from].append((symbol, state_to))
    
   

    


