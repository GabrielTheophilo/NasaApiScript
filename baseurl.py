from apikey import ApiKey
class Data:
    data = ''
    def __init__():
        #print("##########################################")
        print("Gostaria de ver quais tipos de resultados?")
        print("1 - Hoje")
        print("2 - Uma data específica")
        #print("3 - Entre uma data e outra")
        a = int(input(""))
        while a<=0 or a>3:
            print("*Escolha inválida*")
            a = int(input(""))
        if a==1:
            Data.data = ''
        elif a==2:
            data = Data.StartDate()
            Data.data += f'date={data}&'
        elif a==3:
            data = Data.StartDate()
            Data.data += f'start_date={data}&'
            data1 = Data.StartDate()
            Data.data += f'end_date={data1}&'

    def StartDate():
        date_day = int(input("Insira um dia: "))
        while (date_day<=0 or date_day>31):
            date_day = int(input("Insira um dia: "))
        
        date_month = int(input("Insira um mês: "))
        while(date_month<=0 or date_month>12):
            date_month = int(input("Insira um mês: "))
            
        date_year = int(input("Insira um ano: "))
        while (date_year<1999 or date_year>2022):
            date_year = int(input("Insira um ano: "))
        
        return str(f'{date_year}-{date_month}-{date_day}')


class BaseUrl():
    data = Data.__init__()
    url = 'https://api.nasa.gov/planetary/apod?' 
    if Data.data != "":
        url += Data.data
    url += (f'api_key={ApiKey.apikey}')
    def __init__():
        print(BaseUrl.url)

if __name__ == '__main__':
    BaseUrl.__init__()