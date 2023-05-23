import asyncio
import websockets
import aiosqlite
import json
import sqlite3


# Connect to database
conn = sqlite3.connect("stock.db")
cursor = conn.cursor()

# Create database if it doesn't exist
cursor.execute('DROP TABLE IF EXISTS trades')
cursor.execute(""" CREATE TABLE trades(
                    time float,
                    price float)""")

# Close connection
conn.commit()
conn.close

url = 'ws://localhost:8766'

async def save_down(url):
    """
    Function to read live data from websockets and save to database
    """
    # Connect to websocket
    async with websockets.connect(url) as websocket:
        
        trades_buffer = []
        while True:
            data = await websocket.recv()
            data = json.loads(data)
            trades_buffer.append((data['time'], data['price']))
                        
            if len(trades_buffer) > 1:    
                
                async with aiosqlite.connect('stock.db') as db:
                    
                    await db.executemany(""" INSERT INTO trades
                                     (time, price) VALUES (?,?)""", trades_buffer)

                    await db.commit()
                
                trades_buffer = []


asyncio.run(save_down(url))
