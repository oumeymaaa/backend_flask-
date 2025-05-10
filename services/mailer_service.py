from flask_mail import Message

from config import mailer


def send_mail(
        subject: str,
        body: str,
        recipients: list[str]
):
    msg = Message(
        subject=subject,
        recipients=recipients,
        body=body
    )
    mailer.send(msg)
    return "Mail Sent Successfully"
