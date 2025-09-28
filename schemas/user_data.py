import strawberry


@strawberry.input
class UserDataInput:
    name: str
    email: str
    address: str
