import psycopg2
import logging
from typing import List
import datetime

from config import DATABASE_HOST, DATABASE_PORT, DATABASE_USER, DATABASE_PASSWORD, DATABASE_DB
from record import Record

logger = logging.getLogger(__name__)



class Database:
    def __init__(self) -> None:
        self.initilize()

    def __enter__(self) -> 'Database':
        # with文を始めるときに呼ばれる
        self.initilize()
        return self

    def initilize(self) -> None:
        # データベースに接続
        self.conn = psycopg2.connect(
            host=DATABASE_HOST,
            port=DATABASE_PORT,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD,
            database=DATABASE_DB,
        )
        #psycopg2.connect('postgresql://idaten:idaten_pass@db:5432/postgres')
    
    def insert_record(self, record:Record) -> None:
        # INSERT文を実行
        with self.conn.cursor() as cur:
            cur.execute(
                'INSERT INTO records (user_id, date, category, sets, reps, weight) VALUES (%s, %s, %s, %s, %s, %s)',
                (record.user_id, record.date, record.category, record.sets, record.reps, record.weight)
            )

        # 変更をコミット
        self.conn.commit()
    
    def parse_record(self, record:[int, int, datetime.date, str, int, int, int]) -> Record:
        """
        input: record (col, user_id, date, category, sets, reps, weight)
        Return: Record(user_id, date, category, sets, reps, weight)
        """
        col, user_id, date, category, sets, reps, weight = record
        return Record(user_id, date, category, sets, reps, weight)
    
    def get_records(self) -> List[Record]:
        """
        param: 
        return: レコードを返す[(user_id, date, category, sets, reps, weight), ...]
        """
        # SELECT文を実行
        with self.conn.cursor() as cur:
            cur.execute('SELECT * FROM records')
            records = cur.fetchall()
        res:List[Record] = []
        for record in records:
            res.append(self.parse_record(record))
        # レコードを返す
        return res
    
    def finalize(self) -> None:
        # データベースとの接続を切断
        if self.conn != None and self.conn.closed == 0:
            self.conn.close()
    
    def __del__(self) -> None:
        pass
    
    def __exit__(self, exc_type, exc_value, traceback) -> None:
        # with文を抜けるときに呼ばれる
        self.finalize()
