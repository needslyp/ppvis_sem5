class Launch:
    def __init__(self):
        self.departments = [HospitalDepartment('', '', '', '', '', '') for _ in range(10)]
        self.diagnosis = [Diagnosis('', '', '', '', '') for _ in range(10)]

        self.queue = Queue('', '')
        self.doctors = [Doctor('', '', '', '', '', '', '') for _ in range(10)]

        self.system = System('', self.queue, '', self.departments)

    def main(self):
        self.system.start()


class System():
    def __init__(self, time, queue, list_of_patients, list_of_departments):
        self._time = time

        self._queue = queue
        self._list_of_patients = list_of_patients
        self._list_of_departments = list_of_departments

    def start(self):
        pass

    def authorization(self):
        # авторизация текущего врача
        pass

    def findChamber(self, diagnosis):
        # поиск свободной палаты для пациента с диагнозом
        pass

    def addNewPatient(self, diagnosis, name):
        # добавление нового пацинта в систему
        pass

    def updateQueue(self, patientID, doctorID):
        # обновить очередь согласно поступившему пациенту и врачу, который его будет принимать
        pass

    def transferPatient(self, patientID, departmentID):
        # передать пациента в отделение, где ему будет предоставлено лечение
        pass

    def fillData(self):
        # заполнить данные пациента
        pass


class Authorization():
    def __init__(self, list_of_users):
        self.list_of_users = list_of_users

    def authorization(self, doctor_id):
        # авторизация созданного пользователя
        pass


class Doctor():
    def __init__(self, id, name, specialist, login, password, cabinet, patients):
        self._id = id
        self._name = name
        self._specialist = specialist
        self._login = login
        self._password = password
        self._cabinet = cabinet

        self.list_of_patients = patients


class ExamDoctor(Doctor):
    def __init__(self, id, name, specialist, login, password, cabinet):
        super().__init__(id, name, specialist, login, password, cabinet)

    def closeHistory(self, patient_id):
        # закрыть историю болезни пациенту
        pass


class Queue():
    def __init__(self, arrival_time, waiting_time):
        self._arrival_time = arrival_time
        self._waiting_time = waiting_time

    def calc_waiting_time(self, arrival_time, amount):
        # расчитать время ожидания
        pass


class HospitalDepartment():
    def __init__(self, id, name, capacity, number, doctors, patients):
        self._id = id
        self._name = name
        self._capacity = capacity
        self._number = number

        self.list_of_doctors = doctors
        self.list_of_patients = patients


class Diagnosis():
    def __init__(self, id, name, id_dep, analysis, prio):
        self._id = id
        self._name = name
        self._id_dep = id_dep
        self._analysis = analysis
        self._prio = prio


class Patient():
    def __init__(self, id, fio, number, address, ills):
        self._id = id
        self._FIO = fio
        self._address = address
        self._number = number
        self._ills = ills


class IllsHistory():
    def __init__(self, id, result):
        self._id = id
        self._result = result
