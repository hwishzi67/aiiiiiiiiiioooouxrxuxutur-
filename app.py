import os
import sys
import subprocess
import time

# =========================================================================
# 1. حركة جلب وشغل السكربت داخل نافذة تيرمينال/تيرمكس مستقلة تلقائياً
# =========================================================================
def force_open_window():
    # الفحص إذا كان السكربت شغال أصلاً داخل نافذة تفاعلية أو لا
    if not sys.stdin.isatty():
        # إذا كان جهازك وندوز (Windows)
        if sys.platform.startswith('win'):
            subprocess.Popen([sys.executable] + sys.argv, creationflags=subprocess.CREATE_NEW_CONSOLE)
            sys.exit()
        # إذا كان جهازك ماك أو لينكس / تيرمكس (Mac / Linux / Termux)
        else:
            # يفحص بيئة التشغيل ويفتح تيرمينال جديدة خلف الكواليس
            if 'TERM' not in os.environ:
                os.environ['TERM'] = 'xterm-256color'
            # يفتح النافذة المستقلة لتشغيل الأوامر تلقائياً
            subprocess.Popen(['xterm', '-e', sys.executable] + sys.argv)
            sys.exit()

# تشغيل حركة فتح النافذة التلقائية
try:
    force_open_window()
except Exception:
    pass # إذا كان شغال في نافذة من قبل يكمل طبيعي

print("=========================================================")
print("          🔥 AETHER AI SYSTEM - AUTO INSTALLER 🔥        ")
print("=========================================================")

# =========================================================================
# 2. الفحص والتثبيت التلقائي الصامت للمكتبات البرمجية الناقصة
# =========================================================================
required_libraries = {
    "flask": "Flask",
    "google-generativeai": "google.generativeai"
}

print("🔄 جاري فحص مكتبات النظام وتثبيت النواقص تلقائياً...")
for package, import_name in required_libraries.items():
    try:
        __import__(import_name)
    except ImportError:
        print(f"📦 لقيت مكتبة ناقصة: [{package}].. جاري تنزيلها الحين صامت...")
        try:
            # تشغيل التثبيت تلقائياً وبسرعة
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
            print(f"✅ تم تثبيت {package} بنجاح ومستعد للشغل!")
        except Exception as e:
            print(f"❌ فشل التثبيت التلقائي لـ {package}: {e}")
            time.sleep(5)
            sys.exit()

# استدعاء المكتبات بعد التأكد التام من تثبيتها تلقائياً
from flask import Flask, request, jsonify
import google.generativeai as genai
import base64

# =========================================================================
# 3. بناء سيرفر العقل الذكي وتجهيز الـ API بالعامية
# =========================================================================
app = Flask(__name__)

# 🔴 حط مفتاح الـ API حقك هنا (تأخذه مجاناً وبسرعة من Google AI Studio)
GOOGLE_API_KEY = "ضع_مفتاح_الـ_API_الخاص_بك_هنا"
genai.configure(api_key=GOOGLE_API_KEY)

# إعداد خيارات العقل ليكون خبير جداً في الأكواد وسريع الاستجابة
generation_config = {
    "temperature": 0.4, 
    "top_p": 0.95,
    "max_output_tokens": 8192,
}

# الموديل الأحدث عالمياً لدعم قراءة وفحص الصور والفيديوهات الطويلة بدقة فائقة وبحث الويب
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest", 
    generation_config=generation_config,
    tools=[{"google_search": {}}] # تشغيل البحث التلقائي بالويب لجلب الأكواد الجديدة
)

# بدء المحادثة مع الذاكرة المستمرة
chat_session = model.start_chat(history=[])

@app.route('/')
def index():
    # استدعاء واجهتك الأسطورية index.html تلقائياً أول ما يفتح السيرفر
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "<h3>❌ خطأ: تكفى سمّ ملف الـ HTML باسم index.html وحطه في نفس المجلد مع السكربت.</h3>"

@app.route('/ask', methods=['POST'])
def ask_ai():
    try:
        data = request.json
        user_message = data.get("message", "")
        file_data = data.get("file", None)

        contents = []

        # إذا رفعت (صورة، فيديو، ملف) من زر الـ (+) بالواجهة
        if file_data:
            file_src = file_data.get("src", "")
            file_type = file_data.get("type", "")
            
            # فك التشفير الصامت للميديا عشان البايثون يحللها بسرعة البرق
            if ";base64," in file_src:
                header, encoded = file_src.split(";base64,")
                bytes_data = base64.b64decode(encoded)
                
                contents.append({
                    "mime_type": file_type,
                    "data": bytes_data
                })

        # 🧠 هندسة الأوامر الصارمة عشان يهرج معك بالعامية ويفهمك بالملي
        system_prompt = (
            "أنت مساعد ذكاء اصطناعي خارق وأسطوري واسمك AETHER AI، خبير ومحترف في كل لغات البرمجة بالعالم "
            "(مثل Python, JavaScript, Luau حقت روبلوكس، C++, HTML) والأمن السيبراني، وأقوى من شات جي بي تي بمراحل.\n"
            "شروطك الحاكمة في الرد:\n"
            "1. تكلم مع المستخدم باللغة العامية السعودية المريحة جداً وبدون أي رسميات كأنك خويّه الروح بالروح.\n"
            "2. افهم كلامه بالملي وحلل أي صورة أو فيديو أو ملف يرسله بدقة متناهية وعطه الخلاصة بالعامية الفصيحة.\n"
            "3. إذا طلب كود برمجي، اكتبه كاااامل بدون أي اختصارات أو نقصان أو نقط، وضعه دائماً داخل علامات الأكواد الخفية "
            "(مثل ```python أو ```html أو ```lua) عشان يظهر في صندوق النسخ الفخم بالواجهة تلقائياً.\n"
            "4. ابحث في الويب تلقائياً لتأكيد المعلومات الجديدة والأكواد المحدثة."
        )

        if user_message:
            full_prompt = f"{system_prompt}\n\nالمستخدم كتب لك: {user_message}"
            contents.append(full_prompt)
        else:
            contents.append(f"{system_prompt}\n\nحلل هذا الملف المرفق بدقة شديدة واشرح لي الي داخله بالعامية وعطني الحل.")

        # إرسال البيانات واستلام الرد الذكي الصاروخي
        response = chat_session.send_message(contents)
        
        return jsonify({"reply": response.text})

    except Exception as e:
        return jsonify({"reply": f"❌ واجهت مشكلة داخل العقل البرمجي: {str(e)}"})

@app.route('/new_chat', methods=['POST'])
def reset_chat():
    global chat_session
    # تصفير الذاكرة وبدء شات جديد فوراً عند الضغط على زر التصفير العلوي (✎)
    chat_session = model.start_chat(history=[])
    return jsonify({"status": "success"})

if __name__ == '__main__':
    print("\n🚀 العقل الذكي لـ AETHER AI شغال الحين بأعلى كفاءة!")
    print("👉 افتح المتصفح وادخل على الرابط هذا عشان تعيش التجربة الأسطورية: [http://127.0.0.1:5000](http://127.0.0.1:5000)")
    print("=========================================================\n")
    
    # تشغيل السيرفر صامت ومحلي
    app.run(debug=False, host='0.0.0.0', port=5000)
