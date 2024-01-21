from pydantic import BaseModel


class UserCreate(BaseModel):

    name: str
    email: str
    password: str

    def get_properties(self):
        return (self.name, self.email, self.password)


class UserOutput(BaseModel):

    id: int
    name: str
    email: str

    def get_properties(self):
        return (self.id, self.name, self.email)


class UserUpdate(BaseModel):

    id: int | None
    name: str | None
    email: str | None
    password: str | None

    def get_properties(self):
        return (self.id, self.name, self.email, self.password)
