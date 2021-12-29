import yagmail


class SendNewsEmails():
    sender_mail = yagmail.SMTP(user="##########", password="#####")

    def send_mail(self, news):
        send_data = "Hi " + news.name + "\n\n" + "Here are top news based on your Interest : " + news.interest + "\n\n" + news.body_string + "\n" "NewsTeam."
        self.sender_mail.send(to=news.email, contents=send_data, subject="You Daily NewsFeed")


if __name__ == "__main__":
    sender_mail = yagmail.SMTP(user="abhipythonlearn@gmail.com", password="test!@#1996")
    send_data1 = "Hi Abhi" + "\n\n" + "Here are top news based on your Interest : FootBall" + "\n\n" + "News on football" + "\n" "NewsTeam."
    sender_mail.send(to='myemailaddress', contents=send_data1, subject="You Daily NewsFeed")





