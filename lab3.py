client = {
    "name": "Ahmed",
    "grid_type": "220V",
    "bill": 1200
}
if client.get("grid_type") == "220V":
    print(f" العميل {client.get('name')} يحتاج إنفرتر فاز واحد " )
elif client.get("grid_type") == "380V":
    print(f" العميل {client.get('name')} يحتاج إنفرتر 3 th. " )
else:
     print("نوع شبكة غير مدعوم")

