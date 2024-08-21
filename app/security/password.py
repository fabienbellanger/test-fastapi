from passlib.context import CryptContext


class Password:
    ctx: CryptContext

    def __init__(self):
        self.ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password, hashed_password):
        return self.ctx.verify(plain_password, hashed_password)

    def get_hash(self, password):
        return self.ctx.hash(password)
