import win32com.client as client
from typing import List
from pathlib import Path


def send_email(
    to_email: str, body: str, path_atachments: List[str], subject: str = "IBM Balance"
) -> None:
    outlook = client.Dispatch("Outlook.Application")
    message = outlook.CreateItem(0)
    message.Display()
    message.to = to_email
    message.Subject = subject
    message.HTMLBody = body
    for i in path_atachments:
        message.Attachments.Add(i)
    
    message.Save()
    message.Send()