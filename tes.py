image_url_list = ['https://storage.googleapis.com/trifacto/Apple/airpods', 'https://storage.googleapis.com/trifacto/Dell%20Technologies%20/laptop', 'https://storage.googleapis.com/trifacto/Sony/television', 'https://storage.googleapis.com/trifacto/bosch/washing%20machine']


products = [{'_id': '6308c7af7e18bd2b4ae6af21', 'Company_name': 'Apple', 'Product_name': 'airpods', 'Price': '26300', 'Inventory': '20', 'Categories': 'electronics', 'Manufacturing_site': 'California', 'Description': 'a new class of in-ear headphones', 'Time': '26/08/2022 18:46:31'},

{'_id': '6308c8347e18bd2b4ae6af23', 'Company_name': 'Dell Technologies ', 'Product_name': 'laptop', 'Price': '226300', 'Inventory': '24', 'Categories': 'electronics', 'Manufacturing_site': 'North Ryde', 'Description': 'Inspiron keeps you connected to what matters most to you', 'Time': '26/08/2022 18:48:44'},

{'_id': '6308c8827e18bd2b4ae6af24', 'Company_name': 'Sony', 'Product_name': 'television', 'Price': '25000', 'Inventory': '32', 'Categories': 'electronics', 'Manufacturing_site': 'Japan', 'Description': 'upscaling technology in our latest TVs brings everything you watch to life in our stunning 4K quality', 'Time': '26/08/2022 18:50:02'},

{'_id': '6308ccc89fe18640579c93d8', 'Company_name': 'bosch', 'Product_name': 'washing machine', 'Price': '50000', 'Inventory': '50', 'Categories': 'electronics', 'Manufacturing_site': 'germany', 'Description': ' Inverter Touch Control Fully Automatic Front Loading Washing Machine with In - built Heater', 'Time': '26/08/2022 19:08:16'}]


for product in products:

    product_str = [product['Company_name'], product['Product_name']]
    
    print(product_str)
	
    for item in image_url_list:
        
        print (item)
        
        if product_str[0] and product_str[1] in item:
            
            print ('got it')
            break
        	