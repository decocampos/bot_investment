from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

#Busca de oportunidade

#Limpando as pastas
def limpar_arquivos_pasta(caminho_pasta):
    try:
        for nome_arquivo in os.listdir(caminho_pasta):
            caminho_completo = os.path.join(caminho_pasta, nome_arquivo)
            if os.path.isfile(caminho_completo):
                os.remove(caminho_completo)
    except Exception as e:
        print(f"Erro ao limpar a pasta: {e}")

folder_path = r'put the path for a folder to receive all opportunities to buy'
limpar_arquivos_pasta(folder_path)
folder_rblc = r'put the path for a folder to receive all opportunities to sell'
limpar_arquivos_pasta(folder_rblc)

# Substitua o caminho para o ChromeDriver pelo caminho correto no seu sistema
chrome_driver_path = r'put the correct path of the chromedriver in your computer'

# Configuração do ChromeDriver sem a necessidade de executable_path
options = webdriver.ChromeOptions()
options.add_argument("--disable-extensions")  
driver = webdriver.Chrome(chrome_driver_path, chrome_options=options)
driver.get('https://www.investing.com/charts/stocks-charts')

empresas=['put a list of codes of companies that you want to buy or analize']
i=0
wait=WebDriverWait(driver, 2)

# Open the site
WebDriverWait(driver, 5)

# maximize the window
driver.maximize_window()

# scroll a little bit to prepare the screenshot
WebDriverWait(driver, 5)
element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="fullColumn"]/h1')))
driver.execute_script("arguments[0].scrollIntoView();", element)

# put the conditions of the graphics that I want to analyse
iframe = driver.find_elements(By.TAG_NAME, 'iframe')[1]
driver.switch_to.frame(iframe)
wait
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, ".no-overflow > iframe"))
wait
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "#tv_chart_container > iframe"))
wait
# open options
driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div/div[2]/div[5]/a').click()
wait
#BB
driver.find_element('xpath', '/html/body/div[13]/div[2]/div[2]/div[2]/div[2]/div/div[10]/div').click()
wait
#MA
driver.find_element('xpath', '/html/body/div[13]/div[2]/div[2]/div[2]/div[2]/div/div[47]/div').click()
wait
# RSI
driver.find_element('xpath', '/html/body/div[13]/div[2]/div[2]/div[2]/div[2]/div/div[58]/div/div').click()
wait
# scroll a little bit to prepare the screenshot
body=driver.find_element('xpath','/html/body')
body.send_keys(Keys.PAGE_UP)
body.send_keys(Keys.PAGE_UP)
body.send_keys(Keys.PAGE_UP)
body.send_keys(Keys.PAGE_UP)
body.send_keys(Keys.PAGE_UP)
#Close options
driver.find_element('xpath', '/html/body/div[13]/div[3]').click()
wait
# Candle
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/div[3]/div/div/span[1]").click()

# scroll a little bit to prepare the screenshot
WebDriverWait(driver, 5)
element=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div[2]')
driver.execute_script("arguments[0].scrollIntoView();", element)

input_field=driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div/input')
# Find the div element using its class or ID
div_element = driver.find_element('xpath', '/html/body/div[1]/div[1]/div/div[3]/table/tbody/tr[5]/td[2]/div')

# Get the value of the RSI element
inner_text = div_element.text

prefix = 'RSI (14) '

pos = inner_text.find(prefix)
number_str = inner_text[pos+len(prefix):]
# Convert the string to float
number = float(number_str)

if('decides your margin'):
    screenshot_path = os.path.join(folder_path, f"JanelaAberta_AAPL.png")
    driver.save_screenshot(screenshot_path)
elif('decides your margin'):
    screenshot_path = os.path.join(folder_path, f"Oportunidade_AAPL.png")
    driver.save_screenshot(screenshot_path)
elif('decides your margin'):
    screenshot_path = os.path.join(folder_path, f"Compra_AAPL.png")
    driver.save_screenshot(screenshot_path)
elif('decides your margin'):
    screenshot_path = os.path.join(folder_rblc, f"JanelaAberta_AAPL.png")
    driver.save_screenshot(screenshot_path)
elif('decides your margin'):
    screenshot_path = os.path.join(folder_rblc, f"Rebalancear_AAPL.png")
    driver.save_screenshot(screenshot_path)
WebDriverWait(driver, 10)

# search for the other companies
for i in range (len(empresas)):
    input_field.clear()
    input_field.send_keys(empresas[i])
    input_field.send_keys(Keys.RETURN)
    time.sleep(5)
    div_element = driver.find_element('xpath', '/html/body/div[1]/div[1]/div/div[3]/table/tbody/tr[5]/td[2]/div')
    inner_text = div_element.text
    prefix = 'RSI (14) '
    pos = inner_text.find(prefix)
    number_str = inner_text[pos+len(prefix):]
    number = float(number_str)
    #time.sleep(11)
    if(number<45 and number>40):
        screenshot_path = os.path.join(folder_path, f"JanelaAberta_{empresas[i]}.png")
        driver.save_screenshot(screenshot_path)
        #print(number)
    elif(number<=40 and number>33):
        screenshot_path = os.path.join(folder_path, f"Oportunidade_{empresas[i]}.png")
        driver.save_screenshot(screenshot_path)
        #print(number)
    elif(number<=33):
        screenshot_path = os.path.join(folder_path, f"Compra_{empresas[i]}.png")
        driver.save_screenshot(screenshot_path)
        #print(number)
    elif(number>=60 and number<70):
        screenshot_path = os.path.join(folder_rblc, f"JanelaAberta_{empresas[i]}.png")
        driver.save_screenshot(screenshot_path)
        #print(number)
    elif(number>=70):
        screenshot_path = os.path.join(folder_rblc, f"Rebalancear_{empresas[i]}.png")
        driver.save_screenshot(screenshot_path)
        #print(number)
    time.sleep(2)

# close the WebDriver instance
driver.quit()
