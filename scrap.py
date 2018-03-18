import mechanicalsoup # Import the module
import pprint
pp = pprint.PrettyPrinter(indent=4)

if __name__ == "__main__": 
    
    URL = "https://www.flipkart.com"

    browser = mechanicalsoup.StatefulBrowser()
    search_page = browser.get(URL)
    ## Find the search form
    search_form = search_page.soup.find("form", {"action":"/search"})
    ## Enter Query in the search form
    #search_query = raw_input("Enter Search Term:")
    search_query = "iPhone"
    print("Searching For: %s",search_query)
    search_form.find("input", {"name": "q"})["value"] = search_query
    ## Submit the search query
    search_response = browser.submit(search_form, search_page.url)
    ## Find all the href links
    search_response_links = search_response.soup.findAll("a",{"class":"_1UoZlX"})
    ## Iterate through all products
    for link in search_response_links:
        product_url = URL + link['href']
        product_page = browser.get(product_url)
        product_name = product_page.soup.find("h1",{"class":"_3eAQiD"}).contents[1]
        product_price = product_page.soup.find("div",{"class":"_1uv9Cb"}).contents[0].contents[4]
        print("Name: %s \t Price: %s",product_name,product_price)
