class SignInLocatorsCollection:
    def __init__(self):
        self.__sign_in_button_locator = ('xpath', '//a[@href="https://megogo.net/ua/auth_login"]')
        self.__phone_field = ('xpath', '//input[@placeholder="Телефон"]')
        self.__code_field = ('xpath', '//input[@maxlength="4"]')

    @property
    def sign_in_button(self):
        return self.__sign_in_button_locator

    @property
    def phone_field(self):
        return self.__phone_field

    @property
    def code_field(self):
        return self.__code_field
