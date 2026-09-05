class User:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def login(self) -> None:
        print(f"Bienvenido {self.username}")


class Staff(User):
    def login(self) -> None:
        print("--- PORTAL DEL STAFF ---")
        super().login()
        # print(f"Bienvenido {self.username}")


class Patient(User):
    def login(self) -> None:
        print("--- PORTAL DEL PATIENT ---")
        super().login()
        # print(f"Bienvenido {self.username}")


def main():
    user = User(username="usuario", password="user123")
    user.login()
    staff = Staff(username="staff", password="staff123")
    staff.login()
    patient = Patient(username="patient", password="patient123")
    patient.login()


if __name__ == "__main__":
    main()
