from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from decouple import config


class SendgridApi:
    def send_email(self, to, subject, content):
        message = Mail(
            from_email="ian.sandes@outlook.com",
            to_emails=to,
            subject=subject,
            html_content=f"<strong>{content}</strong>",
        )
        try:
            sg = SendGridAPIClient(config("SENDGRID_API_KEY"))
            sg.send(message)
        except Exception as e:
            print(e.message)
