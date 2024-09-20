class User:
    def __init__(self, username, email, password, role='staff'):
        self.username = username
        self.email = email
        self.password = password
        self.role = role  # Can be 'admin', 'manager', 'staff'

    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'role': self.role
        }