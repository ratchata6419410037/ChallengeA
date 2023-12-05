def count_words(sentence):
    # แยกคำจากประโยค
    words = sentence.split()
    
    # นับจำนวนคำทั้งหมด
    total_words = len(words)
    
    # ใช้ set เพื่อหาคำที่ไม่ซ้ำกัน
    unique_words = set(words)
    
    # นับจำนวนคำที่ซ้ำกัน
    duplicate_words = {}
    for word in unique_words:
        count = words.count(word)
        if count > 1:
            duplicate_words[word] = count
    
    # แสดงผลลัพธ์
    print("ป้อนข้อความ:", sentence)
    print("มีคำทั้งหมด", total_words, "คำ")
    print("มีคำที่ซ้ำกัน", len(duplicate_words), "คำคือ", ', '.join(duplicate_words.keys()))
    for word, count in duplicate_words.items():
        print("คำว่า", word, "ซ้ำกัน", count, "ครั้ง")

try:
    # รับประโยคจากผู้ใช้
    user_input = input("ป้อนประโยค (ภาษาอังกฤษ): ")
    count_words(user_input)
except Exception as e:
    print("เกิดข้อผิดพลาด:", e)
