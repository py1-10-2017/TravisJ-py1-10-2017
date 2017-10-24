class Patient(object):
    PATIENT_ID = 0

    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
        self.id_num = self.__class__.PATIENT_ID
        self.bed_number = "None"

        self.__class__.PATIENT_ID += 1

    def patient_info(self):
        print "\n" + ("#" * 20)
        for k, v in self.__dict__.iteritems():
            print k, ":", v
        print "#" * 20


class Hospital(object):
    BED_NUM = 0

    def __init__(self, hospital_name, capacity):
        self.patients = []
        self.hospital_name = hospital_name
        self.capacity = capacity
        self.__class__.BED_NUM = self.capacity

    def admit(self, patient):
        if self.__class__.BED_NUM > 0:
            patient.bed_number = self.__class__.BED_NUM
            self.__class__.BED_NUM -= 1
            self.patients.append(patient)
            print patient.name, "has been admitted."
            return self
        else:
            print "Unable to add", patient.name, "- No beds available!"

    def total_patients(self):
        print len(self.patients)
        return self

    def beds_available(self):
        print self.__class__.BED_NUM
        return self

    def display_patients_info(self):
        for patient in self.patients:
            patient.patient_info()
        return self

    def discharge(self, patient_name):
        for patient in self.patients:
            if patient.name == patient_name:
                patient.bed_number = "None"
                self.__class__.BED_NUM += 1
                self.patients.remove(patient)
                print patient.name, "has been discharged."


travis = Patient("Travis", ["Lactose", "Contrast"])
rebecca = Patient("Rebecca", ["Vicodin"])

# hospital_1 = Hospital("Swedish", 1000)
# hospital_1.admit(travis)
# hospital_1.admit(rebecca)
# hospital_1.beds_available().total_patients().display_patients_info()

hospital_2 = Hospital("Mount Si", 1)
hospital_2.admit(travis)
hospital_2.discharge("Travis")
hospital_2.admit(rebecca).total_patients()
travis.patient_info()
