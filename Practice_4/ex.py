import json

# Читаем JSON файл
with open(r"C:\Users\User\kalmik\PP2_Practices-2026\Practice_4\sample-data.json", "r") as f:
    data = json.load(f)

# Заголовок таблицы
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU'}")
print(f"{'-'*50} {'-'*20} {'-'*6} {'-'*6}")

# Парсим каждый интерфейс
for item in data["imdata"]:
    attrs = item["l1PhysIf"]["attributes"]
    dn    = attrs["dn"]
    descr = attrs["descr"]
    speed = attrs["speed"]
    mtu   = attrs["mtu"]

    print(f"{dn:<50} {descr:<20} {speed:<10} {mtu}")