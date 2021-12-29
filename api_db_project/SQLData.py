import sqlite3
from api_db_project.FetchNews import News
from api_db_project.EmailFunction import SendNewsEmails


class Connection():
    db_name = 'db.sqlite3'
    lst = []
    conn = None
    c = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.c = self.conn.cursor()

    def fetch_data(self):
        self.c.execute('SELECT name, email_address, interests from Table_Name')
        rows = self.c.fetchall()
        return rows

    def close_connection(self):
        self.conn.close()


if __name__ == "__main__":
    sql_connect = Connection()
    sql_connect.connect()
    sql_data = sql_connect.fetch_data()
    sql_connect.close_connection()

    email_obj = SendNewsEmails()

    for name, email, interest in sql_data:
        user_news = News(name, email, interest)
        user_news.fetch_data()
        email_obj.send_mail(user_news)


