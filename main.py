print("Hello Ezzat - GitHub Ready!")
from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display

# تجهيز النص العربي ليظهر متصلاً وبالاتجاه الصحيح
raw_text = "أهلاً بك يا عزت - جاهز للعمل"
reshaped_text = arabic_reshaper.reshape(raw_text)
bidi_text = get_display(reshaped_text)

# تحميل خط ويندوز يدعم العربية بحجم واضح (36)
font = ImageFont.truetype("C:/Windows/Fonts/tahoma.ttf", 36)

# إنشاء صورة خلفية داكنة وتوسيط النص عليها
img = Image.new("RGB", (800, 300), color=(20, 24, 38))
draw = ImageDraw.Draw(img)
draw.text((400, 150), bidi_text, font=font, fill=(255, 215, 0), anchor="mm")

img.save("welcome_banner.png")
print("تم تحديث الصورة welcome_banner.png بخط عربي واضح!")