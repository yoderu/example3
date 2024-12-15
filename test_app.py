import pytest
from flask import Flask
from app import app, Rps
@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
        
def test_index(client):
    """ホームページのテスト"""
    response = client.get("/")
    """ HTTPステータスコードのテスト"""
    assert response.status_code == 200
    # レスポンスデータをデコードしてからアサーションを行う 
    decoded_data = response.data.decode('utf-8')
    # 表示されるページのタイトルをチェックする
    assert "<title>じゃんけんゲーム</title>" in decoded_data
    assert response.headers['Content-Type'] == 'text/html; charset=utf-8'

def test_rps_get():
    """ランダムで出すCPU結果が必ず"ROCK", "PAPER", "SCISSORS"のどれかになっているかテスト"""
    for i in range(1,18):
        assert Rps.get() in ["ROCK", "PAPER", "SCISSORS"]
        
def test_game_rock(client):
    """ROCKを選んだ場合のゲームのテスト"""
    response = client.post("/game", data={"hand": "ROCK"})
    """ HTTPステータスコードのテスト"""
    assert response.status_code == 200        
    """ 返ってきたJSONデータをjson_dataに取得 """
    data = response.get_data().decode('utf-8')
    """ 勝ち負けデータが"勝ち", "負け", "あいこ"のどれかひとつになっているかテスト"""
    assert data in ["勝ち", "負け", "あいこ"]
    
def test_game_paper(client):
    """ROCKを選んだ場合のゲームのテスト"""
    response = client.post("/game", data={"hand": "PAPER"})
    """ HTTPステータスコードのテスト"""
    assert response.status_code == 200        
    """ 返ってきたJSONデータをjson_dataに取得 """
    data = response.get_data().decode('utf-8')
    """ 勝ち負けデータが"勝ち", "負け", "あいこ"のどれかひとつになっているかテスト"""
    assert data in ["勝ち", "負け", "あいこ"]
    
def test_game_scissors(client):
    """ROCKを選んだ場合のゲームのテスト"""
    response = client.post("/game", data={"hand": "SCISSORS"})
    """ HTTPステータスコードのテスト"""
    assert response.status_code == 200        
    """ 返ってきたJSONデータをjson_dataに取得 """
    data = response.get_data().decode('utf-8')
    """ 勝ち負けデータが"勝ち", "負け", "あいこ"のどれかひとつになっているかテスト"""
    assert data in ["勝ち", "負け", "あいこ"]