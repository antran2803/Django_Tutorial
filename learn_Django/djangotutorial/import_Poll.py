import os
import django
from datetime import date

# Thiết lập môi trường Django để có thể dùng models bên ngoài
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
django.setup()

# Import các models từ app polls
from polls.models import Poll, Test

def seed_data():
    polls_data = [
        {"title": "Khảo sát ý kiến khách hàng", "message": "Bạn thấy dịch vụ thế nào?", "time": date(2026, 6, 18), "status": True},
        {"title": "Đánh giá chất lượng", "message": "API phản hồi có nhanh không?", "time": date(2026, 6, 19), "status": False},
        {"title": "Giao diện người dùng", "message": "Giao diện ứng dụng mới có thân thiện không?", "time": date(2026, 6, 20), "status": True},
        {"title": "Tính năng ưu thích", "message": "Bạn sử dụng tính năng nào nhiều nhất?", "time": date(2026, 6, 21), "status": True},
        {"title": "Góp ý cải thiện", "message": "Theo bạn chúng tôi cần cải thiện điều gì nhất?", "time": date(2026, 6, 22), "status": False},
    ]

    for data in polls_data:
        obj, created = Poll.objects.get_or_create(**data)
        if created:
            print(f"✅ Đã thêm Poll: {obj.title}")
        else:
            print(f"⚠️ Poll đã tồn tại: {obj.title}")

    tests_data = [
        {"name": "Nguyễn Văn A", "age": 25, "long": 1.75, "date": date(2026, 6, 18)},
        {"name": "Trần Thị B", "age": 30, "long": 1.62, "date": date(2026, 6, 19)},
        {"name": "Lê Phước C", "age": 22, "long": 1.80, "date": date(2026, 6, 20)},
        {"name": "Phạm Mai D", "age": 28, "long": 1.58, "date": date(2026, 6, 21)},
        {"name": "Hoàng Khang E", "age": 35, "long": 1.71, "date": date(2026, 6, 22)},
    ]

    for data in tests_data:
        obj, created = Test.objects.get_or_create(**data)
        if created:
            print(f"✅ Đã thêm Test: {obj.name}")
        else:
            print(f"⚠️ Test đã tồn tại: {obj.name}")

if __name__ == "__main__":
    print("Bắt đầu thêm dữ liệu...")
    seed_data()
    print("Xong!")

