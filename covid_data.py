from pydantic import BaseModel
class Covid(BaseModel):
    Breathing_Problem:int
    Fever:int
    Dry_Cough:int
    Sore_throat:int
    Running_Nose:int
    Headache:int
    Hyper_Tension:int
    Fatigue :int
    Gastrointestinal :int
    Abroad_travel:int
    Contact_with_COVID_Patient:int
    Attended_Large_Gathering:int
    Visited_Public_Exposed_Places:int
    Family_working_in_Public_Exposed_Places:int