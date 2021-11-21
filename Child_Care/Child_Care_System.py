from experta import *

diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

def preprocess():
    global diseases_list,diseases_symptoms,symptom_map,d_desc_map,d_treatment_map
    diseases = open("diseases.txt")
    diseases_t = diseases.read()
    diseases_list = diseases_t.split("\n")
    diseases.close()
    for disease in diseases_list:
        disease_s_file = open("Disease Symptoms/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        s_list = disease_s_data.split("\n")
        diseases_symptoms.append(s_list)
        symptom_map[str(s_list)] = disease
        disease_s_file.close()
        disease_s_file = open("Disease Descriptions/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_desc_map[disease] = disease_s_data
        disease_s_file.close()
        disease_s_file = open("Disease Treatments/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_treatment_map[disease] = disease_s_data
        disease_s_file.close()

def identify_disease(*arguments):
    symptom_list = []
    for symptom in arguments:
        symptom_list.append(symptom)
    # Handle key error
    return symptom_map[str(symptom_list)]

def get_details(disease):
    return d_desc_map[disease]

def get_treatments(disease):
    return d_treatment_map[disease]

def if_not_matched(disease):
    print("")
    id_disease = disease
    disease_details = get_details(id_disease)
    treatments = get_treatments(id_disease)
    print("")
    print("The most probable disease that you have is %s\n" %(id_disease))
    print("A short description of the disease is given below :\n")
    print(disease_details+"\n")
    print("The common medications and procedures suggested by other real doctors are: \n")
    print(treatments+"\n")

class Greetings(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        print("")
        print("Hi! I am Dr.Yar, I am here to help you make your health better.")
        print("For that you'll have to answer a few questions about your conditions")
        print("Do you feel any of the following symptoms:")
        print("")
        yield Fact(action="find_disease")

    @Rule(Fact(action='find_disease'), NOT(Fact(pain_in_throat = W())),salience = 1)
    def symptom_0(self):
        self.declare(Fact(pain_in_throat=input("Pain in Throat: ")))

    @Rule(Fact(pain_in_throat=L('yes')))
    @Rule(Fact(action='find_disease'), NOT(Fact(cold = W())),salience = 1)
    def symptom_00(self):
        self.declare(Fact(cold=input("Cold: ")))

    @Rule(Fact(pain_in_throat=L('yes')))
    @Rule(Fact(action='find_disease'), NOT(Fact(fever = W())),salience = 1)
    def symptom_01(self):
        self.declare(Fact(fever=input("Fever: ")))

    @Rule(Fact(pain_in_throat=L('yes')))
    @Rule(Fact(action='find_disease'), NOT(Fact(cough = W())),salience = 1)
    def symptom_02(self):
        self.declare(Fact(cough=input("Cough: ")))
        count = 1
        while 1:
            if count==1:
                break
            else:
                continue

    @Rule(Fact(action='find_disease'), NOT(Fact(burning_micturation = W())),salience = 1)
    def symptom_1(self):
        self.declare(Fact(burning_micturation=input("Burning Micturation: ")))

    # @Rule(Fact(burning_micturation=L('yes')))
    # @Rule(Fact(action='find_disease'), NOT(Fact(abdominal_pain = W())),salience = 1)
    # def symptom_11(self):
    #     self.declare(Fact(abdominal_pain=input("Abdominal Pain: ")))
    #
    # @Rule(Fact(burning_micturation=L('yes')))
    # @Rule(Fact(action='find_disease'), NOT(Fact(fever = W())),salience = 1)
    # def symptom_12(self):
    #     self.declare(Fact(fever=input("Fever: ")))
    #
    # @Rule(Fact(action='find_disease'), NOT(Fact(pain_in_ear = W())),salience = 1)
    # def symptom_2(self):
    #     self.declare(Fact(pain_in_ear=input("Pain in Ear: ")))
    #
    # @Rule(Fact(pain_in_ear=L('yes')))
    # @Rule(Fact(action='find_disease'), NOT(Fact(fever = W())),salience = 1)
    # def symptom_21(self):
    #     self.declare(Fact(fever=input("Fever: ")))
    #
    # @Rule(Fact(pain_in_ear=L('yes')))
    # @Rule(Fact(action='find_disease'), NOT(Fact(cold = W())),salience = 1)
    # def symptom_22(self):
    #     self.declare(Fact(cold=input("Cold: ")))
    #
    # @Rule(Fact(action='find_disease'), NOT(Fact(headache = W())),salience = 1)
    # def symptom_3(self):
    #     self.declare(Fact(headache=input("Headache: ")))

    # @Rule(Fact(action='find_disease'), NOT(Fact(loose_motion = W())),salience = 1)
    # def symptom_4(self):
    #     self.declare(Fact(loose_motion=input("Loose Motion: ")))
    #
    # @Rule(Fact(action='find_disease'), NOT(Fact(rashes_over_hand= W())),salience = 1)
    # def symptom_5(self):
    #     self.declare(Fact(rashes_over_hand=input("Rashes over Hands and Feet: ")))
    #
    # @Rule(Fact(action='find_disease'), NOT(Fact(rashes_over_body = W())),salience = 1)
    # def symptom_6(self):
    #     self.declare(Fact(rashes_over_body=input("rashes_over_body: ")))
    #
    # @Rule(Fact(action='find_disease'), NOT(Fact(redness_of_eye = W())),salience = 1)
    # def symptom_7(self):
    #     self.declare(Fact(redness_of_eye=input("Redness of Eyes: ")))
    #
    # @Rule(Fact(action='find_disease'), NOT(Fact(anxiety = W())),salience = 1)
    # def symptom_8(self):
    #     self.declare(Fact(anxiety=input("Anxiety: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(impulsive_behaviour = W())),salience = 1)
    def symptom_9(self):
        self.declare(Fact(impulsive_behaviour=input("Impulsive Behaviour: ")))

    @Rule(Fact(action='find_disease'),Fact(pain_in_throat="yes"),Fact(cough="yes"),Fact(cold="yes"),Fact(fever="yes"))
    def disease_0(self):
        self.declare(Fact(disease="Acute Tonsillitis"))

    @Rule(Fact(action='find_disease'),Fact(burning_micturation="yes"),Fact(abdominal_pain="yes"),Fact(fever="yes"))
    def disease_1(self):
        self.declare(Fact(disease="Urinary Tract Infection"))

    @Rule(Fact(action='find_disease'),Fact(pain_in_ear="yes"),Fact(cold="yes"),Fact(fever="yes"))
    def disease_2(self):
        self.declare(Fact(disease="Earache"))

    @Rule(Fact(action='find_disease'),Fact(disease=MATCH.disease),salience = -998)
    def disease(self, disease):
        print("")
        id_disease = disease
        disease_details = get_details(id_disease)
        treatments = get_treatments(id_disease)
        print("")
        print("The most probable disease that you have is %s\n" %(id_disease))
        print("A short description of the disease is given below :\n")
        print(disease_details+"\n")
        print("The common medications and procedures suggested by other real doctors are: \n")
        print(treatments+"\n")

	# @Rule(Fact(action='find_disease'),
	# 	  Fact(headache=MATCH.headache),
	# 	  Fact(back_pain=MATCH.back_pain),
	# 	  Fact(chest_pain=MATCH.chest_pain),
	# 	  Fact(cough=MATCH.cough),
	# 	  Fact(fainting=MATCH.fainting),
	# 	  Fact(sore_throat=MATCH.sore_throat),
	# 	  Fact(fatigue=MATCH.fatigue),
	# 	  Fact(low_body_temp=MATCH.low_body_temp),
	# 	  Fact(restlessness=MATCH.restlessness),
	# 	  Fact(fever=MATCH.fever),
	# 	  Fact(sunken_eyes=MATCH.sunken_eyes),
	# 	  Fact(nausea=MATCH.nausea),
	# 	  Fact(blurred_vision=MATCH.blurred_vision),NOT(Fact(disease=MATCH.disease)),salience = -999)



if __name__ == "__main__":
    preprocess()
    engine = Greetings()
    while(1):
        engine.reset()  # Prepare the engine for the execution.
        engine.run()  # Run it!
        print("Would you like to diagnose some other symptoms?")
        if input() == "no":
            exit()
        print(engine.facts)
