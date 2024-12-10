import cv2
import numpy as np

def remove_black_background(image_path, output_path):
    # تحميل الصورة
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    # التأكد من أن الصورة محملة بشكل صحيح
    if image is None:
        print("لم يتم العثور على الصورة.")
        return

    # إذا كانت الصورة لا تحتوي على قناة ألفا (شفافية)، يتم إضافتها
    if image.shape[2] == 3:  # الصورة تحتوي على RGB فقط
        image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

    # إنشاء قناع للكشف عن المناطق السوداء
    lower_black = np.array([0, 0, 0, 0])  # أقل قيمة للون الأسود
    upper_black = np.array([50, 50, 50, 255])  # أعلى قيمة للون الأسود
    mask = cv2.inRange(image, lower_black, upper_black)

    # عكس القناع للحصول على المناطق غير السوداء
    mask_inv = cv2.bitwise_not(mask)

    # تطبيق القناع لعزل الخلفية السوداء
    image[:, :, 3] = mask_inv  # ضبط الشفافية بناءً على القناع

    # حفظ الصورة الناتجة
    cv2.imwrite(output_path, image)
    print(f"تم حفظ الصورة بعد إزالة الخلفية السوداء: {output_path}")

# استخدام الدالة

input_path = "/content/output.png"
output_path = "output.png"  # احفظ الصورة بصيغة PNG لدعم الشفافية
remove_black_background(input_path, output_path)
