import logging
from os import getenv, environ
from datetime import date, datetime
from typing import Dict, List


from telegram import Update, update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext
)

from dotenv import load_dotenv

from notion_api import Notionpy


class DiaryBot:

    def __init__(self,
                 telegramkey: str,
                 port: int,
                 ) -> None:
        self.token = telegramkey
        self.port = port
        self.updater = Updater(token=self.token)
        self.dispatcher = self.updater.dispatcher
        self.notionpy = None

        self.selected = None

    def start(self, update: Update, context: CallbackContext) -> None:
        text = "Welcome! Please use /set NOTION_KEY_HERE to init setup!"
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    def set(self, update: Update, context: CallbackContext) -> None:
        NOTION_KEY = context.args[0]
        self.notionpy = Notionpy(NOTION_KEY)

        titles = ""
        for value in self.list_databases():
            titles += value["title"] + "\n"
        text = f"Great! Now, type /select for select the database which you'll use.\n{titles}"
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    def select(self, update: Update, context: CallbackContext) -> None:
        option = context.args[0]
        self.selected = self.notionpy.get_database_by_name(option)
        title = self.selected["title"]
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=f"Base de dados {title} selecionada!")

    def create(self, update: Update, context: CallbackContext) -> None:
        today = datetime.today()

        if not self.notionpy.has_today_page(today, self.selected["id"]):
            today = today.strftime("%d/%m/%y")
            self.notionpy.create_page(today, self.selected["id"])
        else:
            self.append_messages(update.message.text)

    def list_databases(self):
        results = self.notionpy.search_all_databases()
        parsed_results = self.notionpy.parse_databases(results)
        return parsed_results

    def append_messages(self, message: str):
        block = [{
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "text": [{"type": "text", "text": {
                    "content": message
                }}]
            }
        }]
        self.notionpy.append_block(block)

    def setup_dispatcher(self):
        self.dispatcher.add_handler(CommandHandler("start", self.start))
        self.dispatcher.add_handler(CommandHandler("set", self.set))
        self.dispatcher.add_handler(CommandHandler("select", self.select))
        self.dispatcher.add_handler(MessageHandler(
            Filters.update.message, self.create))

    def initbot(self):
        self.setup_dispatcher()
        self.updater.start_webhook(listen="0.0.0.0",
                                   port=int(self.port),
                                   url_path=self.token,
                                   webhook_url='https://telegramtonotion.herokuapp.com/'+self.token
                                   )
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        self.updater.idle()


if __name__ == "__main__":
    load_dotenv()
    PORT = int(environ.get('PORT', 8443))
    api_key = getenv("TELEGRAM_KEY")

    bot = DiaryBot(api_key, PORT)
    bot.initbot()
