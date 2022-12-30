import win32apicom.client as client
from typing import List


def send_email(
    to_email: str, body: str, path_atachments: List[str], subject: str = "Prueba"
) -> None:
    outlook = client.Dispatch("Outlook.Application")
    message = outlook.CreateItem(0)
    message.to = to_email
    message.Subject = subject
    message.HTMLBody = body
    for i in path_atachments:
        message.Attachements.Add(i)
    message.save()
    message.send()
