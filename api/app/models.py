from pydantic import BaseModel

class PredictionRequest(BaseModel):
    Gender: float
    Patient_Type: float
    Ensurance: float
    Class: float
    Age: float
    Clinic_Distance: float
    Wifi: float
    Time_convenience: float
    Online_booking: float
    Clinic_location: float
    Food_and_drink: float
    Waiting_room: float
    Comfort_of_the_facilities: float
    Inflight_entertainment: float
    Pre_entry_service: float
    Post_entry_service: float
    Visitor_service: float
    Check_in_service: float
    Medic_service: float
    Cleanliness: float
    Waiting_time_: float
    Delay_in_care_: float

class PredictionResponse(BaseModel):
    satisfaction: int #posible error