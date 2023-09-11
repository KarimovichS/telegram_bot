import os
import asyncio
import logging
import sys

from aiogram import Bot,Dispatcher,Router,F,types
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from routers import router as all_router

load_dotenv('env')
router=Router()
router.include_router(all_router)

async def main():
    bot=Bot(os.getenv('TOKEN'),parse_mode=ParseMode.HTML)
    dp=Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__=="__main__":
    logging.basicConfig(level=logging.INFO,stream=sys.stdout)
    asyncio.run(main())
