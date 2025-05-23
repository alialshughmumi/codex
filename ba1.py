from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "7816610229:AAH4lb5IK3JA46jD04CrHS3Tod26Qp3Mrcc"

WELCOME_MESSAGE = """
⚜️ أهلاً وسهلاً بك في بوت **استراتيجية الصمود الذهبي** ⚜️

مرحبًا بك في قلعة المتداولين الذهبيين حيث تُصنع القرارات الذكية وتُقهر تقلبات السوق!

هنا نقدم لك:

📊 تحليلات فنية لحظية تُبقيك في قلب الحدث  
🎯 نقاط دخول وخروج محسوبة بدقة  
🐋 مراقبة حية لتحركات كبار الحيتان  
⚔️ استراتيجية الصمود الذهبي – سلاحك في وجه الانهيارات  
💰 توصيات صفقات مدفوعة لتحقيق أرباح قوية  
🧠 أدوات احترافية واستشارات تداول  
🎓 انضمام إلى دورات وقنوات خاصة للنخبة  
⏳ نظام اشتراك ذكي لمتابعة خدماتك بسهولة  
🛠️ دعم فني دائم لخدمتك

ابدأ رحلتك معنا نحو صمود أقوى وربح أذكى...  
**أنت الآن ضمن صفوة المتداولين الذهبيين!**
"""

def main_keyboard():
    keyboard = [
        ["🧠 طريقة استخدام البوت", "📊 التحليل الفني اللحظي"],
        ["🐋 مراقبة صفقات الحيتان", "💡 شرح عملات التداول"],
        ["⚔️ استراتيجية الصمود الذهبي", "💰 الدخول في صفقات مدفوعة"],
        ["📝 الاشتراك", "⏳ مراقبة وتجديد الاشتراك"],
        ["🎓 دورات وقنوات خاصة", "🛠️ الدعم الفني"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE, reply_markup=main_keyboard(), parse_mode="Markdown")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ البوت يعمل الآن ...")
    app.run_polling()

if __name__ == "__main__":
    main()
