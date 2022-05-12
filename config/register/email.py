from djoser import email


# Override the default Djoser confirmation email.
class PasswordChangedConfirmationEmail(email.PasswordChangedConfirmationEmail):
    template_name = 'email/password_changed_confirmation.html'

    def send(self, to, *args, **kwargs):
        print(f"Sending password changed mail to {to}")
        try:
            super().send(to, *args, **kwargs)
        except:
            print(f"Couldn't send mail to {to}")
            raise
        print(f"Password changed mail sent successfully to {to}")
