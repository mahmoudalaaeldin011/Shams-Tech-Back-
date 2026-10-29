# ساعات الشمس اليومية على مدار الأسبوع:
sun_hours = [5.5, 6.0, 4.5, 7.0, 5.0, 6.5, 4.0]

# المطلوب:
# اكتب دالة باسم analyze_sun_hours(hours: list[float]) تقوم بـ:
# 1. لو القائمة فارغة ترجع 0.
# 2. تعد وترجع عدد الأيام التي تكون فيها ساعات الشمس 6.0 أو أكثر (hours >= 6.0).

def analyze_sun_hours(hours: list[float]) ->int :
    if not hours :
        return 0
    # 2. إنشاء عداد يبدأ من الصفر
    good_days_count = 0

    # 3. المرور على كل قراءة وفحصها
    for h in hours:
        if h >= 6.0:
            good_days_count += 1  # زيادة العداد بواحد

    return good_days_count
        
xx=analyze_sun_hours(sun_hours)
print(xx)
