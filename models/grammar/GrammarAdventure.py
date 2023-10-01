from pyformlang.cfg import CFG
import random

class GrammarAdventure():
    
    def __init__(self):
        self.gic_inicio_1 = """
            S -> The player wakes up in a tent in the middle of the jungle.
            S -> Upon waking up, the player finds themselves in a tent surrounded by dense vegetation in the jungle.
            S -> After a deep sleep, the player realizes they are in a tent in the middle of the jungle.
        """
        self.gic_inicio_2 = """
            S -> The player arrives at a hidden tribal village in the jungle.
            S -> After a long journey, the player discovers a hidden tribal village nestled within the dense jungle.
            S -> As the player ventures into the jungle, they come across a hidden tribal village.
        """
        self.gic_inicio_3 = """
            S -> Upon the serendipitous discovery of an ancient treasure map, you embark on a thrilling expedition, culminating in your arrival on a deserted island.
            S -> As you uncover the secrets hidden within an age-old treasure map, your epic journey unfolds, eventually leading you to the shores of a secluded and uninhabited island.
            S -> Your destiny takes a fateful turn when you stumble upon the dusty parchment of an ancient treasure map, setting in motion a grand adventure.
        """
        self.gic_inicio_4 = """
            S -> As the sun sets over the vast ocean, painting the sky with shades of orange and pink, you step onto the shore of a beautiful and remote tropical island. 
            S -> With the ancient treasure map clutched in your hand, you set foot on the untouched sands of a breathtaking tropical island. The sun's warm rays caress your skin
            S -> Your journey in search of adventure and riches has brought you to the edge of the world, where a pristine tropical island awaits your exploration. 
        """
        self.grammar1 = CFG.from_text(self.gic_inicio_1)
        self.grammar2 = CFG.from_text(self.gic_inicio_2)
        self.grammar3 = CFG.from_text(self.gic_inicio_3)
        self.grammar4 = CFG.from_text(self.gic_inicio_4)

    def descgic1(self):
        produccion = random.choice(list(self.grammar1.productions))
        descripcion = " ".join([str(simbolo.value) for simbolo in produccion.body])
        return descripcion
    
    def descgic2(self):
        produccion = random.choice(list(self.grammar2.productions))
        descripcion = " ".join([str(simbolo.value) for simbolo in produccion.body])
        return descripcion
    
    def descgic3(self):
        produccion = random.choice(list(self.grammar3.productions))
        descripcion = " ".join([str(simbolo.value) for simbolo in produccion.body])
        return descripcion

    def descgic4(self):
        produccion = random.choice(list(self.grammar4.productions))
        descripcion = " ".join([str(simbolo.value) for simbolo in produccion.body])
        return descripcion

