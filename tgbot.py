from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler
from telegram.ext import  filters 
from pytube import YouTube
from aiogram import Dispatcher

dp=Dispatcher()

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Salom! Menga YouTube video havolasini yuboring.')

def download_video(update: Update, context: CallbackContext) -> None:
    url = update.message.text
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        update.message.reply_text('Video muvaffaqiyatli yuklandi!')
    except Exception as e:
        update.message.reply_text(f'Xato: {str(e)}')

def main() -> None:
 token = '7397504725:AAF0UAW2oP-YmK6bXDY4tUDX3rnSJm4M8kQ'
    
    updater = Updater(token)
    
    dispatcher = updater.dp

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, download_video))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()