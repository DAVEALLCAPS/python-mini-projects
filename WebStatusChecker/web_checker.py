import sqlite3
import requests

DATABASE_FILE = 'db.sqlite'

def setup_database():
    """Setup the SQLite database to store the history of website checks."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS website_status (
            id INTEGER PRIMARY KEY,
            url TEXT NOT NULL,
            status_code INTEGER,
            status_message TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def check_website_status(url):
    """Check the status of the provided URL."""
    try:
        response = requests.get(url)
        return response.status_code, 'UP' if response.status_code == 200 else 'DOWN'
    except requests.ConnectionError:
        return None, 'DOWN'

def store_website_status(url, status_code, status_message):
    """Store the status of the checked website in the database."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO website_status (url, status_code, status_message)
        VALUES (?, ?, ?)
    ''', (url, status_code, status_message))
    
    conn.commit()
    conn.close()

def view_history():
    """View the history of checked websites."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute('SELECT url, status_code, status_message FROM website_status ORDER BY id DESC')
    rows = cursor.fetchall()
    
    for row in rows:
        print(f"URL: {row[0]}, Status Code: {row[1]}, Status: {row[2]}")
    
    conn.close()

def main():
    setup_database()
    
    while True:
        print("\nWebStatusChecker Menu:")
        print("1. Check website status")
        print("2. View history")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            url = input("Enter the website URL: ")
            status_code, status_message = check_website_status(url)
            if status_code:
                print(f"Website {url} is {status_message} (Status Code: {status_code})")
                store_website_status(url, status_code, status_message)
            else:
                print(f"Website {url} is {status_message}")
                store_website_status(url, None, status_message)
        elif choice == '2':
            view_history()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
