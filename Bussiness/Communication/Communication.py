from Integration.IntegrationApi import IntegrationApi


class Communication:

    def __init__(self):
        self.integration = IntegrationApi()

    def authenticate_user(self, user, password):
        """
        establece la sesión para un usuarios
        :param user:
        :param password:
        :return:
        """
        token = self.integration.post("autenticar", {'identificacion': user, 'contrasena': password})

        self.integration.set_header('Authorization', token)

    def get_user(self, user_id):
        user = self.integration.get(f"usuario/{user_id}")
        print(user)
