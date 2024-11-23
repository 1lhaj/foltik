from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
from webdriver_manager.firefox import GeckoDriverManager

# إعداد المتصفح
options = Options()
options.add_argument("--headless")  # تشغيل المتصفح بدون واجهة
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)

# قائمة روابط الفيديوهات
videos = [
    "https://www.tiktok.com/@username/video/VIDEO_ID_1",
    "https://www.tiktok.com/@username/video/VIDEO_ID_2",
    "https://www.tiktok.com/@username/video/VIDEO_ID_3",
]

def watch_videos(video_urls, duration=15):
    try:
        for video_url in video_urls:
            print(f"فتح الفيديو: {video_url}")
            driver.get(video_url)  # فتح الفيديو
            time.sleep(duration)  # انتظر لمدة محددة (بالثواني) لمحاكاة المشاهدة
            print(f"تمت مشاهدة الفيديو لمدة {duration} ثانية.")
    except Exception as e:
        print(f"حدث خطأ أثناء المشاهدة: {e}")
    finally:
        driver.quit()
        print("تم إغلاق المتصفح.")

# تنفيذ الكود
watch_videos(videos, duration=30)  # مشاهدة كل فيديو لمدة 30 ثانية
