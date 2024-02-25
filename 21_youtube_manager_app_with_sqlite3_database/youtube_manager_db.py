import os
import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_videos():
    print("\n")
    print("*" * 70)
    print("\n")
    cursor.execute("SELECT * FROM videos")
    result_set = cursor.fetchall()
    if len(result_set) == 0:    
        print("There is no video available in database.")
    for row in result_set:
            print(row)
    print("\n")
    print("*" * 70)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?", (video_id,))
    conn.commit()

def main():
    while True:
        print("\n \t \t \t \t Youtube Manager App With Sqlite3 DB")
        print("\t \t \t \t  1. List Videos")
        print("\t \t \t \t  2. Add Videos")
        print("\t \t \t \t  3. Update Videos")
        print("\t \t \t \t  4. Delete Videos")
        print("\t \t \t \t  5. exit app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video ID to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice ")

        input("Enter to run more option..")
        os.system("cls")

    conn.close()

if __name__ == "__main__":
    main()