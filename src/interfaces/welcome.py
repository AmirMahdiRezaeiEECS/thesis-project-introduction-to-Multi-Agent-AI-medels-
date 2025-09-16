from src.interfaces.auth import Auth

def welcome_and_role_determination(storage):
    """Welcome message and role selection."""
    print("خوش آمدید به سیستم مدیریت پایان‌نامه‌ها!")
    print("لطفاً نقش خود را انتخاب کنید:")
    print("1. دانشجو")
    print("2. استاد")
    choice = input("انتخاب شما (1 یا 2): ")

    auth = Auth(storage)
    if choice == "1":
        user = auth.login("student")
        print(f"خوش آمدید، {user.name} (دانشجو)")
        return user  # Return Student object
    elif choice == "2":
        user = auth.login("professor")
        print(f"خوش آمدید، {user.name} (استاد)")
        return user  # Return Professor object
    else:
        print("انتخاب نامعتبر. لطفاً دوباره امتحان کنید.")
        return welcome_and_role_determination(storage)