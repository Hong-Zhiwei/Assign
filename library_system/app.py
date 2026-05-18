import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('library.db')
    return conn

# === 1. READ：顯示列表與搜尋功能 ===
@app.route('/')
def index():
    search_query = request.args.get('search', '') # 獲取搜尋關鍵字
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if search_query:
        # SQL 條件查詢：SELECT ... WHERE ... LIKE
        cursor.execute("SELECT * FROM Books WHERE title LIKE ?", ('%' + search_query + '%',))
    else:
        # SQL 全部查詢：SELECT
        cursor.execute("SELECT * FROM Books")
        
    books = cursor.fetchall()
    conn.close()
    return render_template('index.html', books=books)

# === 2. CREATE = 新增書籍與錯誤處理 ===
@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title'].strip()
        author = request.form['author'].strip()
        isbn = request.form['isbn'].strip()
        
        # 加分項：後端阻擋空值
        if not title or not author or not isbn:
            return render_template('add.html', error="所有欄位都必須填寫！")
            
        conn = get_db_connection()
        cursor = conn.cursor()
        
        try:
            # SQL 新增：INSERT
            cursor.execute("INSERT INTO Books (title, author, isbn) VALUES (?, ?, ?)", (title, author, isbn))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
        except sqlite3.IntegrityError:
            # 加分項：錯誤處理，捕獲 ISBN 重複的錯誤
            conn.close()
            return render_template('add.html', error="錯誤：此 ISBN 已經存在，不可重複！")
            
    return render_template('add.html')

# === 3. UPDATE = 修改書籍 ===
@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        isbn = request.form['isbn']
        
        # SQL 修改：UPDATE
        cursor.execute("UPDATE Books SET title = ?, author = ?, isbn = ? WHERE book_id = ?", (title, author, isbn, book_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
        
    # GET 請求時，先撈出舊資料填入表單
    cursor.execute("SELECT * FROM Books WHERE book_id = ?", (book_id,))
    book = cursor.fetchone()
    conn.close()
    return render_template('edit.html', book=book)

# === 4. DELETE = 刪除書籍 ===
@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    # SQL 刪除：DELETE
    cursor.execute("DELETE FROM Books WHERE book_id = ?", (book_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# 初始化資料庫
def init_db():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            isbn TEXT UNIQUE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)