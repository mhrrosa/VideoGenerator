import yfinance as yf


class Acao:
    def __init__(self, ticker):
        self.ticker = ticker  # Ticker da ação
        self.cota = None  # Cotação atual
        self.pl = None  # Preço/Lucro
        self.pvp = None  # Preço/Valor Patrimonial
        self.dy = None  # Dividend Yield anual

    def load_data(self):
        """
        Carrega os dados financeiros da ação usando o yfinance
        """
        # Obter os dados da ação
        acao = yf.Ticker(self.ticker)
        dados = acao.info

        # Atribuindo valores aos atributos da classe
        self.cota = dados.get('currentPrice', 'Dado não disponível')
        self.pl = dados.get('trailingPE', 'Dado não disponível')
        self.pvp = dados.get('priceToBook', 'Dado não disponível')
        self.dy = dados.get('dividendYield', 'Dado não disponível') * 100  # Convertendo para porcentagem

    def show_data(self):
        """
        Exibe os dados carregados da ação
        """
        print(f"Ação: {self.ticker}")
        print(f"Cota: {self.cota}")
        print(f"P/L: {self.pl}")
        print(f"P/VP: {self.pvp}")
        print(f"DY Anual: {self.dy}%")
