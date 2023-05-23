import asyncio
import websockets
import aiosqlite
import json
import sqlite3



conn = sqlite3.connect("stock.db")
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS trades')
cursor.execute(""" CREATE TABLE trades(
                    time float,
                    price float)""")

#cursor.execute('CREATE INDEX index_time ON trades(time)')

conn.commit()
conn.close

url = 'ws://localhost:8766'
#"wss://stream.binance.com:9443/ws/btcusdt@aggTrade"

async def save_down(url):
    
    async with websockets.connect(url) as websocket:
        
        trades_buffer = []
        while True:
            data = await websocket.recv()
            data = json.loads(data)
            trades_buffer.append((data['time'], data['price']))
            
            #print(data)
            
            if len(trades_buffer) > 1:    
                
                #print('Saving to db')
                
                async with aiosqlite.connect('stock.db') as db:
                    
                    await db.executemany(""" INSERT INTO trades
                                     (time, price) VALUES (?,?)""", trades_buffer)

                    await db.commit()
                
                trades_buffer = []


asyncio.run(save_down(url))
