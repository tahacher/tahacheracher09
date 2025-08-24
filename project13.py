import smtplib

def automatic_email():
    user = input("Enter Your Name >>: ")
    email = input("Enter Your Email >>: ")

    # Proper email format with subject and body
    subject = "Welcome to TheClevelProgrammer"
    body = "Dear " + str(user) + ",\n\nWelcome to TheClevelProgrammer!"
    message = "Subject: " + subject + "\n\n" + body

    try:
        # Connect to Gmail SMTP
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        
        # Login with your Gmail + App Password
        s.login("your_gmail@gmail.com", "your_app_password")

        # Send email (from, to, message)
        s.sendmail("your_gmail@gmail.com", email, message)
        print(" Email sent successfully to " + email)

    except Exception as e:
        print(" Error:", e)

    finally:
        s.quit()

automatic_email()
