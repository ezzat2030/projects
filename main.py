print("Hello Ezzat - GitHub Ready!")
from PIL import Image, ImageDraw
import arabic_reshaper
from bidi.algorithm import get_display

# تجهيز النص العربي ليظهر متصلاً وبالاتجاه الصحيح
raw_text = "أهلاً بك يا عزت - جاهز للعمل"
reshaped_text = arabic_reshaper.reshape(raw_text)
bidi_text = get_display(reshaped_text)

# إنشاء صورة خلفية داكنة وكتابة النص عليها
img = Image.new("RGB", (800, 300), color=(20, 24, 38))
draw = ImageDraw.Draw(img)
draw.text((260, 140), bidi_text, fill=(255, 215, 0))

img.save("welcome_banner.png")
print("تم إنشاء الصورة welcome_banner.png بنجاح!")