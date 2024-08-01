class Dog:
    def __init__(self):
        self.class_family = {}    #과
        self.class_genera = {}   #속
        self.class_species = {}  #종

        
    def family(self):
        self.class_family.update({"과":["개"]})
        return self.class_family
    
    def genera(self):
        self.class_genera.update({"속":["늑대속","여우속","자칼속","코요테속"]})
        return self.class_genera
    
    def specties(self):
        self.class_species.update({"늑대속":["회색늑대","코요테"],
                        "여우속":["붉은여우","북극여우"],
                        "자칼속":["황금자칼","줄무늬자칼"],
                        "코요테속":["코요테"]})
        return self.class_species
        
        
        


            
        
    
        