def send_email(recipient, message, *, sender="university.help@gmail.com"):
    if "@" in recipient or (recipient.endswith(".com") or recipient.endswith(".ru") or recipient.endswith(".net")):
        if sender != recipient:
            if sender == "university.help@gmail.com":
                print(f"Письмо успешно отправлено с адресса {sender} на адресс {recipient}")
            else:
                print("Нестандартный отправитель!")
                print(f"Письмо отправлено с адресса {sender} на адресс {recipient}")
        else:
            print("Нельзя отправить письмо самому себе!")
    else:
        print("Невозмодно отправить письмо с адресса {sender} на адресс {recipient}")
send_email("university@gmail.com", "123456")
