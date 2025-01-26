from django.shortcuts import render
import requests
import json
from urllib.parse import quote
from django.core.cache import cache


def product_search(request):
    search_query = request.GET.get('search_query', '')
    selected_websites = request.GET.getlist('websites')

    all_products = []

    for website in selected_websites:
        if website == 'Amazon':
            products = get_amazon_products(search_query)
            all_products.extend(products)
        elif website == 'Temu':
            products = get_temu_products(search_query)
            all_products.extend(products)

    all_products.sort(key=lambda product: product.get('price', 0))

    context = {
        'search_query': search_query,
        'selected_websites': selected_websites,
        'products': all_products,
    }
    return render(request, 'products/product_search.html', context)

def get_amazon_products(search_query):
    cache_key = f"amazon_products_{search_query}" 
    products = cache.get(cache_key)

    if products is not None:
        return products  
    url = "https://real-time-amazon-data.p.rapidapi.com/search"

    headers = {
        'x-rapidapi-key': "YOUR-API-KEY",  
        'x-rapidapi-host': "real-time-amazon-data.p.rapidapi.com"
    }

    querystring = {
        "query": search_query,
        "page": "1",
        "country": "US",
        "sort_by": "RELEVANCE",
        "product_condition": "ALL",
        "is_prime": "false",
        "deals_and_discounts": "NONE"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()

        response_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error making request to Amazon API: {e}")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON response from RapidAPI (Amazon)")
        return []

    products = []
    if 'products' in response_data['data']:
        for item in response_data['data']['products']:
            try:
                price_str = item.get('price', {}).get('current_price', None)
                price = 0 if price_str is None else float(price_str)

                product = {
                    'title': item.get('title'),
                    'price': price,
                    'image': item.get('thumbnail'),
                    'website': 'Amazon',
                    'source_url': item.get('url')
                }
                products.append(product)
            except Exception as e:
                print(f"Error extracting information of {item.get('title')}: {str(e)}")

        cache.set(cache_key, products, 300)
        return products
    else:
        print("No products found in the Amazon API response")

    return products

def get_temu_products(search_query):
    url = "https://temu-com-shopping-api-realtime-api-scrapper-from-temu-com.p.rapidapi.com/search"

    headers = {
        'x-rapidapi-key': "YOUR-API-KEY",
        'x-rapidapi-host': "temu-com-shopping-api-realtime-api-scrapper-from-temu-com.p.rapidapi.com"
    }

    querystring = {"keyword": search_query}

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()

        response_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error making request to Temu API: {e}")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON response from RapidAPI (Temu)")
        return []

    products = []
    if 'data' in response_data and 'goodsList' in response_data['data']:
        for item in response_data['data']['goodsList']:
            try:
                price_str = item['priceInfo'].get('price')
                price = 0 if not price_str else float(price_str)

                product = {
                    'title': item.get('title'),
                    'price': price,
                    'image': item.get('image'),
                    'website': 'Temu',
                    'source_url': "https://www.temu.com/" + item.get('linkUrl')
                }
                products.append(product)
            except Exception as e:
                print(f"Error extracting information of {item.get('title')}: {str(e)}")

    else:
        print("No products found in the Temu API response")

    return products

def search(request):
    websites = ['Amazon', 'Temu']
    context = {'websites': websites}
    return render(request, 'products/search.html', context)