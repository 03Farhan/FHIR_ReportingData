from flask import Flask
from fhir_parser.fhir import FHIR, Patient, Observation
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

fhir = FHIR()

patients = fhir.get_all_patients()


class Languages(Resource):
    def get(self):
        languages = {}
        for patient in patients:
            for language in patient.communications.languages:
                languages.update({language: languages.get(language, 0) + 1})
        return languages

class MaritalStatus(Resource):
    def get(self):
        marital_statuses = {}
        for patient in patients:
            marital_status = str(patient.marital_status)
            marital_statuses.update({marital_status: marital_statuses.get(marital_status, 0) + 1})
        return marital_statuses

class BirthDecadesMale(Resource):
    def get(self):
        birth_decades_male = {}
        for patient in patients:
            if patient.gender == "female":
                continue
            birth_year = patient.birth_date.year
            birth_decade = birth_year - (birth_year % 10)
            birth_decades_male.update({birth_decade: birth_decades_male.get(birth_decade, 0) + 1})
        return birth_decades_male

class BirthDecadesFemale(Resource):
    def get(self):
        birth_decades_female = {}
        for patient in patients:
            if patient.gender == "male":
                continue
            birth_year = patient.birth_date.year
            birth_decade = birth_year - (birth_year % 10)
            birth_decades_female.update({birth_decade: birth_decades_female.get(birth_decade, 0) + 1})
        return birth_decades_female

api.add_resource(Languages, '/languages')
api.add_resource(MaritalStatus, '/marital_statuses')
api.add_resource(BirthDecadesMale, '/birth_decades_male')
api.add_resource(BirthDecadesFemale, '/birth_decades_female')



if __name__ == '__main__':
    app.run(debug=True, port=5002)