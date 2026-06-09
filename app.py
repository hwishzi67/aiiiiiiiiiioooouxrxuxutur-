import os
import sys
import subprocess
import time

# =========================================================================
# 1. التثبيت التلقائي الصامت للمكتبات البرمجية الناقصة فوراً قبل بدء السيرفر
# =========================================================================
required_libraries = {
    "flask": "Flask",
    "requests": "requests"
}

print("=========================================================")
print("          🔥 AETHER AI CORE v2.0 - NO API KEY 🔥        ")
print("=========================================================")

print("🔄 جاري فحص مكتبات النظام وتثبيت النواقص تلقائياً...")
for package, import_name in required_libraries.items():
    try:
        __import__(import_name)
    except ImportError:
        print(f"📦 لقيت مكتبة ناقصة: [{package}].. جاري تنزيلها الحين صامت...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
        except Exception as e:
            print(f"❌ فشل التثبيت التلقائي لـ {package}: {e}")
            time.sleep(5)
            sys.exit()

# استدعاء المكتبات بعد التأكد التام من وجودها تلقائياً
from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# =========================================================================
# 2. عقل الذكاء الاصطناعي الخبير والمربوط بالإنترنت تلقائياً (بدون مفتاح)
# =========================================================================
def ask_expert_ai_with_web(user_prompt):
    # استخدام سيرفر معالجة ذكي ومفتوح يدعم البحث في الويب الحي
    url = "https://ai-engine.p.rapidapi.com/chat" # أو أي محرك معالجة حر وسريع
    
    # هندسة الأوامر الصارمة لضبط العقل ليصبح خبير ورهيب ويتحدث بالعامية السعودية
    system_instruction = (
        "أنت مساعد ذكاء اصطناعي خارق وأسطوري واسمك AETHER AI، خبير ومحترف في كل لغات البرمجة بالعالم "
        "(مثل Python, JavaScript, Luau حقت روبلوكس، C++, HTML) والأمن السيبراني، وأقوى من شات جي بي تي بمراحل.\n"
        "شروطك الحاكمة في الرد:\n"
        "1. تكلم مع المستخدم باللغة العامية السعودية المريحة جداً وبدون أي رسميات كأنك خويّه الروح بالروح.\n"
        "2. افهم كلامه بالملي واستخدم محرك البحث المدمج في الويب لتأكيد أي معلومة جديدة وأكواد محدثة وعطه الخلاصة.\n"
        "3. إذا طلب كود برمجي، اكتبه كاااامل بدون أي اختصارات أو نقصان أو نقط، وضعه دائماً داخل علامات الأكواد الخفية "
        "(مثل ```python أو ```html أو ```lua) عشان يظهر في صندوق النسخ الفخم بالواجهة تلقائياً."
    )
    
    # دمج الأوامر مع رسالة المستخدم
    full_query = f"{system_instruction}\n\nسؤال المستخدم الحالي: {user_prompt}"
    
    # إرسال الداتا إلى محرك الذكاء الاصطناعي المفتوح مع تفعيل البحث الفوري بالإنترنت
    try:
        # استخدام بوابة الاستدعاء الحرة والسريعة (Free Reverse Proxy)
        response = requests.post(
            "[https://open-ai-api-free.vercel.app/api/chat](https://open-ai-api-free.vercel.app/api/chat)", # سيرفر وسيط مجاني وسريع جداً
            json={
                "model": "gpt-4o", # تحديد الموديل الخبير جداً والأقوى عالمياً في الأكواد
                "messages": [{"role": "user", "content": full_query}],
                "web_search": True # تفعيل البحث الحي بالويب تلقائياً لإحضار آخر المعلومات والأكواد
            },
            headers={"Content-Type": "application/json"},
            timeout=30
        )
        
        if response.status_code == 200:
            res_data = response.json()
            return res_data.get("reply", {}).get("content", "") or res_data.get("content", "")
        else:
            # خطة بديلة سريعة في حال ضغط السيرفر الأول
            alt_res = requests.get(f"[https://api.lolhuman.xyz/api/openai?key=free&text=](https://api.lolhuman.xyz/api/openai?key=free&text=){user_prompt}")
            return alt_res.json().get("result", "يا خوي السيرفر عليه ضغط حالياً، جرب ترسل مرة ثانية الحين.")
            
    except Exception as e:
        return f"❌ واجهت مشكلة أثناء الاتصال بالويب: {str(e)}"

# =========================================================================
# 3. إدارة طرق السيرفر والربط مع واجهتك الـ HTML
# =========================================================================
chat_history_cache = []

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
        
        if not user_message:
            return jsonify({"reply": "أرسل رسالة يا بعد حي عشان أبحث لك عنها بالنت!"})
            
        # استدعاء العقل الخبير والمربوط بالإنترنت مباشرة
        ai_reply = ask_expert_ai_with_web(user_message)
        
        return jsonify({"reply": ai_reply})

    except Exception as e:
        return jsonify({"reply": f"❌ واجهت مشكلة داخل العقل البرمجي: {str(e)}"})

@app.route('/new_chat', methods=['POST'])
def reset_chat():
    global chat_history_cache
    chat_history_cache = [] # تصفير الذاكرة فوراً لتبدأ شات جديد عند الضغط على زر (✎)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    print("\n🚀 العقل الذكي لـ AETHER AI شغال الحين وبدون أي مفاتيح API!")
    print("🌐 متصل بالإنترنت ومفعّل ميزة البحث الذكي المباشر للأكواد المحدثة...")
    print("👉 افتح المتصفح وادخل على الرابط هذا: [http://127.0.0.1:5000](http://127.0.0.1:5000)")
    print("=========================================================\n")
    
    app.run(debug=False, host='0.0.0.0', port=5000)
