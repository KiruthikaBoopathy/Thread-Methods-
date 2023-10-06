from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.http import HttpResponse
import time
from adrf.views import APIView



#=================================================================================================================================
import requests
import concurrent.futures
class Thread_pool( APIView):
    def get(self, request):
        start = time.time()
        api_urls = [
            'https://api.zippopotam.us/us/33162',
            'https://data.binance.com/api/v3/ticker/24hr',
            'https://jsonplaceholder.typicode.com/posts/3',
            'https://jsonplaceholder.typicode.com/posts/4'
        ]

        def fetch_data(url):
            response = requests.get( url )
            if response.status_code == 200:
                return response.json()
            return {'error': f'Failed to retrieve data from {url}'}

        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list( executor.map( fetch_data, api_urls ) )

        data = [{"data": result} for result in results]
        end = time.time()
        execution_time = end - start
        final=({"execution_time": execution_time,"data": data})
        return Response(final)


#========================================================================================================================#
import asyncio
from adrf.views import APIView





class Asyncio(APIView):
    async def get(self,request):
        start = time.time()
        async def fetch_data1(url):
            response = await asyncio.to_thread(requests.get, url)
            if response.status_code == 200:
                return response.json()
            return {'error': f'Failed to retrieve data from {url}'}
        api_urls = ['https://api.zippopotam.us/us/33162',
            'https://api.data.gov.sg/v1/environment/air-temperature',
            'https://jsonplaceholder.typicode.com/posts/3',
            'https://jsonplaceholder.typicode.com/posts/4']
        tasks = [fetch_data1(url) for url in api_urls]
        results = await asyncio.gather(*tasks)
        data=[{"data": result} for result in results]
        end = time.time()
        execution_time = end - start
        final = { "total": execution_time,"data": data,}
        return Response(final)


#========================================================================================================================#

import multiprocessing

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {'error': f'Failed to retrieve data from {url}'}

class Multiprocessing(APIView):
    def get(self, request):
        start = time.time()
        api_urls = [
            'https://api.zippopotam.us/us/33162',
            'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur.json',
            'https://jsonplaceholder.typicode.com/posts/3',
            'https://jsonplaceholder.typicode.com/posts/4'
        ]

        with multiprocessing.Pool(processes=len(api_urls)) as pool:
            results = pool.map(fetch_data, api_urls)

        data = [{"data": result} for result in results]
        end=time.time()
        execution_time = end - start
        final=({"execution_time":execution_time,"data":data})

        # Combine the data into a single string for the response
      #  response_data = "\n".join([str(item) for item in data])

        return Response(final)

#======================================================================================================================#


import httpx


async def fetch(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            return response.json()
        return {'error': f'Failed to retrieve data from {url}'}

class Httpx(APIView):
    def get(self, request):
        start = time.time()
        api_urls = [
            'https://catfact.ninja/fact',
            'https://status.digitalocean.com/api/v2/summary.json',
            'https://jsonplaceholder.typicode.com/posts/3',
            'https://jsonplaceholder.typicode.com/posts/4'
        ]

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        results = loop.run_until_complete(asyncio.gather(*[fetch(url) for url in api_urls]))
        loop.close()

        data = [{"data": result} for result in results]
        end = time.time()
        execution_time = end - start
        final = ({"execution_time": execution_time, "data": data})


        return Response(final)

#==============================================================================================================================


import aiohttp
import asyncio



class Aiohttp(APIView):
    async def get(self, request):
        start = time.time()
        async def fetch_data(url):
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        return await response.json()
                    return {'error': f'Failed to retrieve data from {url}'}

        api_urls = [
                'https://www.boredapi.com/api/activity',
                'http://ergast.com/api/f1/drivers.json',
                'https://jsonplaceholder.typicode.com/posts/3',
                'https://jsonplaceholder.typicode.com/posts/4'
            ]
        tasks = [fetch_data(url) for url in api_urls]
        results = await asyncio.gather(*tasks)

        data = [{"data": result} for result in results]
        end = time.time()
        execution_time = end - start
        final = ({"execution_time": execution_time, "data": data})

        return Response(final)













