from content_moderator import ContentModeratorApi
from sendgrid_integration import SendgridApi


print(" -=-=-=-=-=- Email Sender with content checker -=-=-=-=-=- ")
email_to = input("To: ")
email_subject = input("Subject: ")
email_content = input("Content: ")

# Verificação do conteúdo e envio de emails
cm = ContentModeratorApi()
sendgrid = SendgridApi()

result_cm = cm.use_content_moderator(str(email_content) + " " + str(email_subject))
if result_cm["Terms"] != None:
    print(
        "\nEmail Not Sent! The following terms contain offensive or inappropriate language: "
    )
    for term in result_cm["Terms"]:
        print("- " + term["Term"])
else:
    sendgrid.send_email(email_to, email_subject, email_content)
    print("\nEmail successfully sent!")