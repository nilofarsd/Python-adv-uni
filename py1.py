class Fetcher:
    def __init__(self):
            self.link = "https://cdn.ituring.ir/ex/users.json" 
            self.students = []

    def save_data(self):
        import requests
        response = requests.get(self.link)
        self.students = response.json()

    def nerds(self):
        concat_name = set()
        for student in self.students:
            if student["score"] > 18.5 :
                name = student["name"]+student["last_name"]
                concat_name.add(name)
                
        return concat_name
    
    def sultans(self):
        high_score = 0
        top_students = tuple()

        for student in self.students:
            if student["score"] > high_score :
                high_score = student["score"]
                top_students = (student["name"]+student["last_name"],)

            elif student["score"] == high_score :    
                top_students = top_students + (student["name"]+student["last_name"],)

        return top_students
    
    def mean(self):
        sum = 0
        counter = 0

        for student in self.students:
            sum += student["score"]
            counter += 1
        average = sum/counter

        return average


    def get_students(self):
        students_list = []

        for student in self.students:
            new_student = student
            new_student.pop("city")
            new_student.pop("province")
            new_student.pop("latitude")
            new_student.pop("longitude")
            students_list.append(new_student)

        return students_list










