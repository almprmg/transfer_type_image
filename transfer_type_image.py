from PIL import Image


input_path = "input.jpg" 
output_formats = ["png", "bmp", "tiff"]  


try:
    with Image.open(input_path) as img:
        for fmt in output_formats:
            output_path = f"output.{fmt}"
            img.save(output_path, format=fmt.upper())
            print(f"تم حفظ الصورة بصيغة {fmt}: {output_path}")
except Exception as e:
    print(f"حدث خطأ: {e}")
