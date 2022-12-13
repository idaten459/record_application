from flask import Flask, request, redirect, url_for, render_template
from typing import List
import logging

from database import Database
from record import Record
from datetime import datetime

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s - %(levelname)s - %(pathname)s:%(lineno)d]\t%(message)s ')
logger = logging.getLogger(__name__)
app = Flask(__name__)

@app.route('/')
def index():
    # 記録入力フォームのHTMLを返す
    return render_template('record_form.html')

@app.route('/record', methods=['POST'])
def record():
    logger.debug(request.form)
    # ユーザーから送信されたデータを取得
    #user_id = request.form['user_id']
    user_id = 1
    date = request.form['date']
    category = request.form['category']
    sets = request.form['sets']
    reps = request.form['reps']
    weight = request.form['weight']

    # データベースに記録を登録
    with Database() as db:
        logger.info('insert record')
        record = Record(user_id, date, category, sets, reps, weight)
        db.insert_record(record)

    # 記録一覧画面にリダイレクト
    return redirect(url_for('records'))

@app.route('/records')
def records():
    # 記録一覧のHTMLを返す
    with Database() as db:
        records:List[Record] = db.get_records()
    return render_template('records.html', records=records)

if __name__ == '__main__':
    app.run()
