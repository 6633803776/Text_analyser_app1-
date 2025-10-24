from flask import Flask, render_template, request

app = Flask(__name__)

# ฟังก์ชันหลักสำหรับการวิเคราะห์ข้อความ (นำมาจากโค้ด CLI ของคุณ)
def analyze_text(text_to_analyze):
    if not text_to_analyze:
        return {
            'char_count': 0,
            'word_count': 0,
            'error': "No text to analyze. Please enter some text."
        }

    # 1. นับจำนวนตัวอักษรทั้งหมด (รวมช่องว่าง)
    char_count = len(text_to_analyze)

    # 2. นับจำนวนคำ
    words = text_to_analyze.split()
    word_count = len(words)

    return {
        'char_count': char_count,
        'word_count': word_count,
        'error': None
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    analysis_results = None
    input_text = ""
    
    # หากมีการส่งข้อมูลแบบ POST (ผู้ใช้กดปุ่ม 'Analyze')
    if request.method == 'POST':
        # ดึงข้อความจากฟอร์มในหน้าเว็บ
        input_text = request.form.get('input_text', '')
        
        # เรียกใช้ฟังก์ชันวิเคราะห์
        analysis_results = analyze_text(input_text)

    # แสดงหน้าเว็บ โดยส่งผลลัพธ์และการป้อนข้อมูลเดิมกลับไปด้วย
    return render_template('index.html', results=analysis_results, current_text=input_text)

if __name__ == '__main__':
    # รันแอปพลิเคชัน
    app.run(debug=True)