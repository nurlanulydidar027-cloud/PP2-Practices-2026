import csv
import psycopg2
import os
from config import DB_CONFIG
from connect import get_connection

def create_table():
    """Создает таблицу, если она еще не создана"""
    sql = """
    CREATE TABLE IF NOT EXISTS phonebook (
        user_id SERIAL PRIMARY KEY,
        user_name VARCHAR(100) NOT NULL,
        phone_number VARCHAR(20) NOT NULL UNIQUE
    );
    """
    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            cur.close()
        finally:
            conn.close()

def add_contact(name, phone):
    """Добавляет один контакт вручную"""
    sql = "INSERT INTO phonebook(user_name, phone_number) VALUES(%s, %s) ON CONFLICT (phone_number) DO NOTHING;"
    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(sql, (name, phone))
            conn.commit()
            print(f"Контакт '{name}' добавлен.")
            cur.close()
        finally:
            conn.close()

def import_from_csv(file_path):
    """Загружает данные из CSV файла"""
    # Проверка: существует ли файл по указанному пути
    if not os.path.exists(file_path):
        print(f"Ошибка: Файл не найден по пути: {os.path.abspath(file_path)}")
        return

    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            with open(file_path, mode='r', encoding='utf-8') as f:
                reader = csv.reader(f)
                count = 0
                for row in reader:
                    if row and len(row) >= 2:
                        cur.execute(
                            "INSERT INTO phonebook (user_name, phone_number) VALUES (%s, %s) ON CONFLICT (phone_number) DO NOTHING",
                            (row[0].strip(), row[1].strip())
                        )
                        count += 1
            conn.commit()
            print(f"Успешно обработано строк: {count}. Данные импортированы!")
            cur.close()
        except Exception as e:
            print(f"Ошибка при чтении файла или записи в БД: {e}")
        finally:
            conn.close()

def update_contact(name, new_phone):
    """Обновляет номер телефона по имени пользователя"""
    sql = "UPDATE phonebook SET phone_number = %s WHERE user_name = %s"
    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(sql, (new_phone, name))
            conn.commit()
            if cur.rowcount > 0:
                print(f"Номер для '{name}' обновлен на {new_phone}.")
            else:
                print("Контакт не найден.")
            cur.close()
        finally:
            conn.close()

def query_contacts(search_term):
    """Ищет контакты по части имени"""
    sql = "SELECT * FROM phonebook WHERE user_name ILIKE %s"
    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(sql, ('%' + search_term + '%',))
            rows = cur.fetchall()
            if rows:
                print("\nРезультаты поиска:")
                for row in rows:
                    print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")
            else:
                print("Ничего не найдено.")
            cur.close()
        finally:
            conn.close()

def delete_contact(name_or_phone):
    """Удаляет контакт по имени или номеру телефона"""
    sql = "DELETE FROM phonebook WHERE user_name = %s OR phone_number = %s"
    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(sql, (name_or_phone, name_or_phone))
            conn.commit()
            if cur.rowcount > 0:
                print(f"Контакт '{name_or_phone}' удален.")
            else:
                print("Контакт не найден.")
            cur.close()
        finally:
            conn.close()

if __name__ == "__main__":
    create_table() 
    
    while True:
        print("\n--- PhoneBook Меню ---")
        print("1. Импорт из CSV")
        print("2. Добавить контакт вручную")
        print("3. Обновить номер контакта")
        print("4. Удалить контакт (по имени или номеру)")
        print("5. Поиск контакта")
        print("6. Выход")
        
        choice = input("Выберите действие (1-6): ")
        
        if choice == '1':
            # Используем путь, который ты скинул
            import_from_csv('Practice_7/contact.csv')
        elif choice == '2':
            n = input("Введите имя: ")
            p = input("Введите номер: ")
            add_contact(n, p)
        elif choice == '3':
            n = input("Введите имя для обновления: ")
            p = input("Введите новый номер: ")
            update_contact(n, p)
        elif choice == '4':
            val = input("Введите имя или номер для удаления: ")
            delete_contact(val)
        elif choice == '5':
            term = input("Введите имя (или часть имени) для поиска: ")
            query_contacts(term)
        elif choice == '6':
            print("Завершение работы...")
            break
        else:
            print("Неверный ввод, попробуйте снова.")