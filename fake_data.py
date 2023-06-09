import asyncio
import websockets
import numpy as np
import time
import datetime
from random import gauss
from math import sqrt, exp
import json

def create_price(s0, mu, sigma):
    """
    Generates a price following a geometric brownian motion process based on the input of the arguments:
    - s0: Asset inital price.
    - mu: Interest rate expressed annual terms.
    - sigma: Volatility expressed annual terms. 
    """

    s0 *= exp((mu - 0.5 * sigma ** 2) * (1. / 365.) + sigma * sqrt(1./365.) * gauss(mu=0, sigma=1))
    
    return s0


async def data_serv(websocket):
    """
    Function to fetch a price and send via websockets    
    """
    
    # Set initial price
    price = 145
    
    while True:
        # Get price
        price = create_price(price, 0.05, 0.1)
        # Get random waiting time
        #ts = np.random.exponential(scale=0.1, size=(1))[0]
        
        # Get current time
        ct = time.time()
        # jsonify the data
        data = json.dumps({'time': ct, 'price':(str(round(price, 2)))})
        
        # Send data and wait for 50msec
        await websocket.send(data)
        await asyncio.sleep(0.0500) #ts)

start_server = websockets.serve(data_serv, 'localhost', 8766)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()