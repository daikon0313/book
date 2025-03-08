from logging import getLogger, StreamHandler, FileHandler, Formatter, INFO, ERROR

# logger = getLogger(__name__)
# logger.setLevel(INFO)

# #標準出力
# s_handler = StreamHandler()
# s_handler.setLevel(ERROR)

# #ファイル出力
# f_handler = FileHandler("./app.log")
# f_handler.setLevel(INFO)

# logger.addHandler(s_handler)
# logger.addHandler(f_handler)

# logger.critical("クリティカルなメッセージ")
# logger.error("エラーなメッセージ")
# logger.warning("ワーニングなメッセージ")
# logger.info("インフォなメッセージ")
# logger.debug("デバックなメッセージ")

# logger = getLogger(__name__)
# f_handler = FileHandler("./app.log")
# logger.addHandler(f_handler)

# try:
#     with open("./outputs/data.txt", mode="w") as f:
#         f.write("Hello")
# except Exception:
#     logger.exception("ファイルの書き込み失敗しました")

logger = getLogger(__name__)
s_handler = StreamHandler()
formatter = Formatter(
    "%(asctime)s - %(levelname)s : %(name)s"
    "%(name)s %(filename)s : %(lineno)d"
)

s_handler.setFormatter(formatter)
logger.addHandler(s_handler)

logger.error("error message")
logger.warning("warning message")