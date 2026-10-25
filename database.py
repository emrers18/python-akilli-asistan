import sqlite3

DB_NAME = "assistant.db"

def create_table():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_message TEXT NOT NULL,
                assistant_response TEXT NOT NULL
            )

        """
    )

    conn.commit()
    conn.close()


def save_message(user_message:str, assistant_response:str):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """ 
            INSERT INTO messages (user_message, assistant_response)
            VALUES (?, ?)
        """, (user_message, assistant_response)
    )

    conn.commit()
    conn.close()


def get_all_messages():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT id, user_message, assistant_response 
            FROM messages
            ORDER BY id ASC
        """
    )

    rows = cursor.fetchall()
    conn.close()

    messages = []

    for row in rows:
        messages.append(
            {
                "id": row[0],
                "user_message": row[1],
                "assistant_response": row[2]
            }
        )
    
    return messages

if __name__ == "__main__":
    create_table()
    save_message("Merhaba", "Merhaba!")
    save_message("Nasılsın?", "İyiyim, teşekkür ederim.")
    
    messages = get_all_messages()
    print(messages)