import psycopg2
from config import DB_CONFIG
from connect import get_connection

def upsert_contact(name, phone):
    """3.2: Процедура добавления (INSERT) или обновления (UPDATE), если имя уже есть"""
    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            # Используем CALL для вызова процедуры
            cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
            conn.commit()
            print(f"Контакт '{name}' обработан (добавлен/обновлен) через процедуру.")
            cur.close()
        except Exception as e:
            print(f"Ошибка процедуры upsert: {e}")
        finally:
            conn.close()

def search_contacts(pattern):
    """3.2: Функция поиска по паттерну (имя или телефон)"""
    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            # Используем SELECT для вызова функции, возвращающей таблицу
            cur.execute("SELECT * FROM get_contacts_by_pattern(%s)", (pattern,))
            rows = cur.fetchall()
            if rows:
                print(f"\nНайдено контактов по запросу '{pattern}':")
                for row in rows:
                    print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")
            else:
                print("Ничего не найдено.")
            cur.close()
        finally:
            conn.close()

def get_paginated_contacts(limit, offset):
    """3.2: Функция для пагинации (LIMIT и OFFSET)"""
    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            # Вызываем функцию из БД для постраничного вывода
            cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
            rows = cur.fetchall()
            print(f"\nПоказ контактов (Лимит: {limit}, Смещение: {offset}):")
            for row in rows:
                print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")
            cur.close()
        finally:
            conn.close()

def delete_contact_proc(identifier):
    """3.2: Процедура удаления по имени или номеру телефона"""
    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("CALL delete_contact_by_name_or_phone(%s)", (identifier,))
            conn.commit()
            print(f"Запрос на удаление '{identifier}' выполнен.")
            cur.close()
        finally:
            conn.close()

if __name__ == "__main__":
    while True:
        print("\n--- PhoneBook (Practice 08: Functions & Procedures) ---")
        print("1. Добавить/Обновить контакт (Upsert Procedure)")
        print("2. Поиск по шаблону (Pattern Function)")
        print("3. Показать страницу контактов (Pagination Function)")
        print("4. Удалить контакт (Delete Procedure)")
        print("5. Выход")
        
        choice = input("Выберите действие (1-5): ")
        
        if choice == '1':
            n = input("Введите имя: ")
            p = input("Введите телефон: ")
            upsert_contact(n, p)
        elif choice == '2':
            patt = input("Введите часть имени или номера для поиска: ")
            search_contacts(patt)
        elif choice == '3':
            lim = int(input("Сколько записей показать? (Limit): "))
            off = int(input("Сколько пропустить? (Offset): "))
            get_paginated_contacts(lim, off)
        elif choice == '4':
            val = input("Введите имя или номер для удаления: ")
            delete_contact_proc(val)
        elif choice == '5':
            print("Выход...")
            break
        else:
            print("Неверный выбор.")
