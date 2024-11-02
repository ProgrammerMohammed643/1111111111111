import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '7486489133:AAGZ9vpWIGjNOM6ygSIHp2t3O8qBekWvXtI'
RENDER_API_KEY = 'rnd_Kl90RthyzKAxIZyuwRCat2pSHzls'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("أرسل لي ملف Python (.py) لرفعه إلى Render وتشغيله.")

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    document = update.message.document
    if document and document.file_name.endswith('.py'):
        await update.message.reply_text("جارٍ تحميل الملف...")
        await process_file(document, update)
    else:
        await update.message.reply_text("يرجى إرسال ملف بصيغة .py فقط.")

async def process_file(document, update):
    file = await document.get_file()  # الحصول على الكائن File من الوثيقة
    file_path = os.path.join(os.getcwd(), 'uploaded_file.py')  # حفظ الملف في المسار الحالي
    
    # تنزيل الملف
    await file.download_to_drive(file_path)  
    await update.message.reply_text("تم تحميل الملف بنجاح!")
    
    # رفع الملف إلى Render وتشغيله
    success = await upload_to_render(file_path)
    if success:
        await update.message.reply_text("تم رفع الملف بنجاح وتشغيله على Render.")
    else:
        await update.message.reply_text("حدث خطأ أثناء رفع الملف إلى Render.")

async def upload_to_render(file_path):
    # رفع الملف إلى Render باستخدام API
    # يمكنك تعديل هذا الجزء ليقوم برفع الملف بالفعل باستخدام Render API
    # هنا سنكتفي بطباعة رسالة كمثال فقط
    print(f"Uploading {file_path} to Render...")
    return True

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Document.FileExtension("py"), handle_document))

    application.run_polling()

if __name__ == "__main__":
    main()
