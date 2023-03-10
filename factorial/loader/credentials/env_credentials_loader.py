import os

from dotenv import load_dotenv

from .abstract_credentials import AbstractCredentials


class EnvCredentials(AbstractCredentials):
    def __init__(self, filename: str = None):
        super().__init__()

        load_dotenv(filename)
        self.email = os.getenv("FACTORIAL_EMAIL")
        self.password = os.getenv("FACTORIAL_PASSWORD")
        self.cookie = os.getenv("FACTORIAL_COOKIE")

    def get_email(self) -> str:
        """Get email from json file to login to factorialhr

        :return: string
        """
        return self.email

    def get_password(self) -> str:
        """Get password from json file to login to factorialhr

        :return: string
        """
        return self.password

    def get_cookie(self) -> str:
        return self.cookie
