from flask import Flask, render_template, request, jsonify
import os
from enum import Enum
import random
import asyncio
import winsound
app = Flask(__name__)
class Rps(Enum):
   ROCK = 1
   PAPER = 2
   SCISSORS = 3
   @classmethod
   def get(cls):
       return cls(random.randrange(1,4,1)).name
   
# ホームページ
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/game",methods=["POST"])
def game():
    try:
       hand = request.form['hand']
       cpu = Rps.get()
       result = ""
       if cpu == hand:
            result = "あいこ"
       elif hand == "ROCK":
         if cpu == "SCISSORS":
            result = "勝ち"
         else:
            result = "負け"
       elif hand == "PAPER":
         if cpu == "ROCK":
            result = "勝ち"
         else:
            result = "負け"
       elif hand == "SISSORS":
         if cpu == "PAPER":
            result = "勝ち"
         else:
            result = "負け"   
       if result ==  "勝ち":    
         asyncio.run(playsound("omedetou.wav"))  
       elif result == "負け": 
         asyncio.run(playsound("hazure.wav"))      
    except Exception as e:
       print(e)    
    return result 
     
    # audioファイルの再生
async def playsound(soundfile):
    winsound.PlaySound(soundfile, winsound.SND_ASYNC)
       
if __name__ == "__main__":
    # 現在いるディレクトリを取得する
    current_folder = os.getcwd()
    static_folder_path = current_folder + "/static"
    # flaskに staticファイルフォルダーのパスを設定する
    app.config["STATIC_FOLDER"] = static_folder_path
    # 
    app.run(debug=True)