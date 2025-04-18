#Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer:
    def __init__(self, name, employee_id, role, team):
        self.name = name
        self.employee_id = employee_id
        self.role = role
        self.team = team
    
    def __str__(self):
        return f"Name: {self.name}\nEmployee ID: {self.employee_id}\nRole: {self.role}\nTeam: {self.team}\n"


if __name__ == "__main__":
    
    programmer1 = Programmer("Arpan","E1245","SSE","Software dev")
    programmer2 = Programmer("Ahana","E1234","SSE","Backend dev")

    
    print(programmer1)
    print(programmer2)


