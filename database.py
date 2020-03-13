import pymysql as SQL
from person import Person


class MoreBot_DB(Person):

    def __init__(self):
        self.user = 'mxolisi'
        self.password = 'Mx@lisi7'
        self.host = '160.153.133.158'
        self.database = 'more_bot'
        self.conn = ""
        self._query_execute = ""

    def conenct(self):
        try:
            self.conn = SQL.connect(user=self.user, password=self.password , host=self.host, db=self.database)
            self._query_execute = self.conn.cursor()
            if self._query_execute:
                print("Success: Connection to database succeeded")
        except Exception as e:
            print("Error: ", e)
        return self._query_execute

    def new_record(self, mood, chat_id):
        query = "INSERT INTO records(name, mood, chat_id) VALUES('{0}','{1}','{2}')".format(self.getUser(), mood, chat_id)
        self._query_execute.execute(query)
        pass

    def read_all_records(self):
        pass