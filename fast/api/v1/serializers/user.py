from pydantic import BaseModel


class UserInput(BaseModel):

    name: str
    email: str
    password: str
    confirm_pass: str

    def get_properties(self):
        return (
            self.name, self.email, self.password, self.confirm_pass
        )


class UserOutput(BaseModel):

    name: str
    email: str

    def get_properties(self):
        return (
            self.name, self.email
        )
