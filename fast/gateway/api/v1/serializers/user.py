from pydantic import BaseModel


class UserInput(BaseModel):

    name: str
    email: str
    password: str
    confirm_pass: str

    def get_properties(self):
        return (self.name, self.email, self.password, self.confirm_pass)


class UserInputUpdate(BaseModel):

    name: str | None
    email: str | None
    password: str | None

    def get_properties(self):
        return (self.name, self.email, self.password)
