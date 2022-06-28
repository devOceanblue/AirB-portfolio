"""
class UserSchema():
    def validate_id(self, id):
        id_regex = re.compile(r"/^[a-z]+[a-z0-9]{5,19}$/g")
        if not id_regex.match(id):
            raise ValidationError("Invalid Id.")

    def validate_password(self, password):
        password_regex = re.compile(
            r"/^(?=.*[a-zA-z])(?=.*[0-9])(?=.*[$`~!@$!%*#^?&\\(\\)\-_=+]).{8,16}$/"
        )
        if not password_regex.match(password):
            raise ValidationError("Invalid Password.")

    def email_regex(self, email):
        email_regex = re.compile(
            r"/^[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$/i"
        )
        if not email_regex.match(email):
            raise ValidationError("Invalid Email address.")
"""
