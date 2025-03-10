import yfinance as yf
from datetime import datetime
import pandas as pd

class Acao:
    def __init__(self, ticker):
        self.ticker = ticker  # Ticker da ação
        self.cota = None  # Cotação atual
        self.pl = None  # Preço/Lucro
        self.pvp = None  # Preço/Valor Patrimonial
        self.dy = None  # Dividend Yield anual (calculado manualmente)
        self.path_excel = None

    def load_data(self):
        """
        Carrega os dados financeiros da ação usando o yfinance
        """
        # Obter os dados da ação
        acao = yf.Ticker(self.ticker)
        dados = acao.info

        # Atribuindo valores aos atributos da classe
        self.cota = dados.get('currentPrice', 'Dado não disponível')
        self.pl = self.format_data(dados.get('trailingPE', 'Dado não disponível'))
        self.pvp = self.format_data(dados.get('priceToBook', 'Dado não disponível'))

        # Calcula o Dividend Yield de 2024 com base nos dividendos pagos no ano
        self.dy = self.calculate_dy_2024(acao)

    def calculate_dy_2024(self, acao):
        """
        Calcula o Dividend Yield (DY) de 2024 baseado nos pagamentos reais de dividendos no ano.

        :param acao: Objeto Ticker do yfinance.
        :return: Dividend Yield em percentual (%).
        """
        # Obtém todos os dividendos históricos
        dividendos = acao.dividends

        if dividendos.empty:
            return "Sem dividendos disponíveis"

        # Filtrar apenas os dividendos pagos em 2024
        dividendos_2024 = dividendos[dividendos.index.year == 2024]

        # Soma dos dividendos pagos em 2024
        total_dividendos_2024 = dividendos_2024.sum()

        # Obtém a cotação atual da ação
        try:
            preco_atual = acao.history(period="1d")["Close"].iloc[-1]
        except:
            return "Preço indisponível"

        # Calcula o Dividend Yield
        if preco_atual > 0:
            dividend_yield = (total_dividendos_2024 / preco_atual) * 100
            return round(dividend_yield, 2)  # Arredondamos para 2 casas decimais
        else:
            return "Erro no cálculo"

    def load_data_excel(self):
        """
        Carrega os dados financeiros da ação usando excel
        """
        df = pd.read_excel(self.path_excel)

        df_filtred = df[df['ticker'] == self.ticker]

        # Atribuindo valores aos atributos da classe
        self.cota = df_filtred['cota']
        self.pl = df_filtred['pl']
        self.pvp = df_filtred['pvp']
        self.dy = df_filtred['dy']

    def show_data(self):
        """
        Exibe os dados carregados da ação
        """
        print(f"Ação: {self.ticker}")
        print(f"Cota: {self.cota}")
        print(f"P/L: {self.pl}")
        print(f"P/VP: {self.pvp}")
        print(f"DY Anual (2024): {self.dy}%")

    def format_data(self, valor):
        """
        Formata um número para ter no máximo duas casas decimais.

        :param valor: O número a ser formatado.
        :return: O número formatado com no máximo duas casas decimais.
        """
        if isinstance(valor, (int, float)):
            return round(valor, 2)
        return valor

    def calcular_investimento_e_dividendos(self, quantidade_cotas):
        """
        Calcula o valor investido e o ganho em dividendos com base na quantidade de cotas.

        :param quantidade_cotas: Número de cotas adquiridas.
        :return: Tupla (investido, dividendos)
        """
        if self.cota is None or self.dy is None:
            return "Dados insuficientes para cálculo"

        investido = quantidade_cotas * self.cota
        dividendos = (self.dy / 100) * investido

        return str(round(float(investido), 3)), str(round(float(dividendos), 3))


