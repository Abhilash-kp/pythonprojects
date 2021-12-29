from api_db_project.SQLData import Connection
from api_db_project.FetchNews import News
from api_db_project.EmailFunction import SendNewsEmails


sql_connect = Connection()
sql_connect.connect()
sql_data = sql_connect.fetch_data()
sql_connect.close_connection()

email_obj = SendNewsEmails()

for name, email, interest in sql_data:
    user_news = News(name, email, interest)
    user_news.fetch_data()
    email_obj.send_mail(user_news)



