# YOLOv8-YOLOv9-Object-Detection-Project

โครงสร้างโปรเจกต์ (Project Structure)

ภายในโปรเจกต์มีไฟล์และโฟลเดอร์หลัก ๆ ดังนี้:

1. โฟลเดอร์สำคัญ (Directories)
   
config/: เก็บไฟล์ตั้งค่าต่าง ๆ ที่จำเป็นสำหรับการฝึกหรือรันโมเดล

img_label/: โฟลเดอร์สำหรับเก็บรูปภาพและไฟล์ป้ายกำกับ (Labels) สำหรับกระบวนการ Train หรือ Valid

runs/: โฟลเดอร์ที่ระบบสร้างขึ้นอัตโนมัติเพื่อเก็บผลลัพธ์จากการ Train หรือ Predict (Logs, Weights, ผลลัพธ์รูปภาพ/วิดีโอ)

videos/: โฟลเดอร์สำหรับเก็บไฟล์วิดีโอต้นฉบับที่ใช้ทดสอบ

2. ไฟล์สคริปต์หลัก (Python Scripts)
   
test_image_yolov8.py: สคริปต์สำหรับทดสอบรันโมเดล YOLOv8 บนไฟล์รูปภาพ

test_video_yolov8.py: สคริปต์สำหรับทดสอบรันโมเดล YOLOv8 บนไฟล์วิดีโอ

ttt.py: ไฟล์สคริปต์เสริมสำหรับทดลองหรือประมวลผลเพิ่มเติมทั่วไป

3. ไฟล์โมเดลและตั้งค่า (Model Weights & Configs)
   
data222.yaml: ไฟล์ Configuration หลักสำหรับกำหนดพาธของชุดข้อมูล (Dataset) คลาสของวัตถุ

doors.pt: ไฟล์น้ำหนัก (Model Weights) ของโมเดลที่เทรนเฉพาะสำหรับการตรวจจับประตู

gelan-e.pt: ไฟล์น้ำหนักของโมเดล GELAN

yolov8x.pt: ไฟล์น้ำหนักมาตรฐานของ YOLOv8 แบบ X-large (ความแม่นยำสูง)

yolov9-c.pt: ไฟล์น้ำหนักของโมเดล YOLOv9 รุ่น Compact

4. ไฟล์ตัวอย่าง (Sample Data)
    
729399_0.jpg ถึง 729405_0.jpg: ไฟล์รูปภาพตัวอย่าง (เช่น ภาพบรรยากาศในห้องประชุม) ที่ใช้สำหรับทดสอบรันโมเดล

*****************************************************************************

Name : Patasu Daungmala

Position : R&D Manager

Tel : 0641900551

E-mail : nextsoftware.pp@gmail.com

Line : https://lin.ee/THH8PAt

Medium : https://dr-pathasu-doung.medium.com

Github : https://github.com/doungmala

Website : https://nextsoftwarethailand.com, https://autoworks24.com

Linkedin : https://linkedin.com/in/patasu-doungmala-7b90a2205

​
บริษัท เน็กซ์ ซอฟต์แวร์ จำกัด 

ที่อยู่ หมู่บ้าน inizio เลขที่ 888/257 ถนนมะลิวัลย์ ตำบลบ้านทุ่ม อำเภอเมืองขอนแก่น จังหวัดขอนแก่น 40000 เลขที่ผู้เสียภาษี : 0405558003118


ผลงานและประวัติการทำงาน

สามารถดูผลงานและประวัติการทำงานได้ที่

AI, Image Processing : https://www.dropbox.com/scl/fi/tskimhifw0hlcdea5e8t8/Next-Software-2026.pdf?rlkey=f26k2b7t69doklzwxyx54qsmh&dl=0

IoT : https://www.dropbox.com/scl/fi/a5mj4ucjotjv4xrh6sh9q/NS_IOT2025.pdf?rlkey=t0cwl0l4b81w73do2drhqqjp0&dl=0

SEO, Website : https://www.dropbox.com/scl/fi/4q811q0s88xtd8usf5e25/WEB-DEVELOPER-SEARCH-ENGINE-OPTIMIZATION.pdf?rlkey=nvqvndrxv7v9yrfmlcgtplmtx&dl=0

Affiliated companies : https://www.dropbox.com/scl/fi/y98k95g24x44511iyhdih/Affiliated-companies.pdf?rlkey=mf1z7lr6q5x58ee2nonmgnz8r&dl=0
