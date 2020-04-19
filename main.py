from seleniumwire import webdriver


driver = webdriver.Firefox(".")

driver.get('https://www.lephoceen.fr')

for request in driver.requests:
    if request.response:
        print(
            request.path,
            request.response.status_code,
            request.response.headers.get('Content-Type')
        )
driver.close()