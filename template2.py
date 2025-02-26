from moviepy import VideoFileClip, TextClip, CompositeVideoClip, ImageClip, AudioFileClip, concatenate_videoclips
import os
from Acao import Acao
import random
from moviepy.video.fx.LumContrast import LumContrast

def add_images_from_folder(video,ticker1, folder_path="img/"):
    """
    Carrega duas imagens da pasta 'img/', redimensiona para o tamanho padrão e posiciona lado a lado no vídeo.
    """
    # Listar os arquivos de imagem na pasta img/
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]

    image1_path = ''

    for img in image_files:
        if ticker1 == img.split('.')[0]:
            image1_path = os.path.join(folder_path, img)


    # Criar os ImageClip a partir das imagens
    img1 = ImageClip(image1_path)

    # Redimensionar as imagens para um tamanho padrão
    img1 = img1.resized(height=400)  # Redimensionar para uma altura de 100 px

    # Definir a duração das imagens
    img1 = img1.with_duration(60)

    # Posicionar as imagens lado a lado
    img1 = img1.with_position((video.size[0] // 2 - 180, video.size[1] // 2 - 1200))

    return img1


def insert_ticker(video, ticker1):
    """
    Cria variáveis de ticker no vídeo e posiciona na tela
    """
    # Criar o texto com a cotação (exemplo "Cota: R$ 10.00")
    ticker_text = TextClip(
        text=f"{ticker1}",
        font="C:/Windows/Fonts/IMPACT.ttf",  # Caminho completo para o arquivo da fonte
        font_size=80,
        color="white"
    )

    # Definir a posição do texto (mover um pouco para a esquerda e para baixo)
    ticker_text = ticker_text.with_position((video.size[0] // 2 - 80, video.size[1] // 2 - 700)).with_duration(60)

    return ticker_text

def insert_marca(video):
    """
    Cria variáveis de ticker no vídeo e posiciona na tela
    """
    # Criar o texto com a cotação (exemplo "Cota: R$ 10.00")
    ticker_text = TextClip(
        text=f"@rosa.investe",
        font="C:/Windows/Fonts/IMPACT.ttf",  # Caminho completo para o arquivo da fonte
        font_size=80,
        color="white"
    )

    # Definir a posição do texto (mover um pouco para a esquerda e para baixo)
    ticker_text = ticker_text.with_position((video.size[0] // 2 - 200, video.size[1] // 2 + 800)).with_duration(60)

    return ticker_text


def loop_video(video, min_duration=60):
    """
    Duplica o vídeo até atingir pelo menos a duração mínima especificada.
    """
    clips = []
    total_duration = 0

    while total_duration < min_duration:
        print(total_duration)
        clips.append(video)
        total_duration += video.duration
    return concatenate_videoclips(clips)

def get_random_template(folder_path="song/"):
    """
    Retorna um caminho de música aleatória da pasta especificada.
    """
    # Listar os arquivos de música na pasta song/
    song_files = [f for f in os.listdir(folder_path) if f.endswith(('.mp3', '.wav', '.ogg'))]

    if not song_files:
        raise ValueError("Nenhuma música encontrada na pasta.")

    # Escolher um arquivo de música aleatório
    random_song = random.choice(song_files)
    return os.path.join(folder_path, random_song)

def insert_title(video):
    """
    Cria variáveis de ticker no vídeo e posiciona na tela
    """
    # Criar o texto com a cotação (exemplo "Cota: R$ 10.00")
    title_text = TextClip(
        text=f"QUANTO DE DIVIDENDO",
        font="C:/Windows/Fonts/IMPACT.ttf",  # Caminho completo para o arquivo da fonte
        font_size=110,
        color="white",
        stroke_color="black",  # Cor da borda
        stroke_width=5  # Espessura da borda
    )
    title_text2 = TextClip(
        text=f"POSSO RECEBER?",
        font="C:/Windows/Fonts/IMPACT.ttf",  # Caminho completo para o arquivo da fonte
        font_size=120,
        color="white",
        stroke_color="black",  # Cor da borda
        stroke_width=5  # Espessura da borda
    )
    # Definir a posição do texto (mover um pouco para a esquerda e para baixo)
    title_text = title_text.with_position((video.size[0] // 2 - 490, video.size[1] // 2 - 1550)).with_duration(60)
    title_text2 = title_text2.with_position((video.size[0] // 2 - 490, video.size[1] // 2 - 1380)).with_duration(60)


    return title_text, title_text2


def insert_table_fix(video, acao):
    """
    Cria variáveis de ticker no vídeo e posiciona na tela
    """

    # header
    h1 = TextClip(
        text=f"COTAS",
        font="C:/Windows/Fonts/IMPACT.ttf",  # Caminho completo para o arquivo da fonte
        font_size=80,
        color="white",
        stroke_color="black",  # Cor da borda
        stroke_width=5  # Espessura da borda
    )
    h2 = TextClip(
        text=f"INVESTIDO",
        font="C:/Windows/Fonts/IMPACT.ttf",  # Caminho completo para o arquivo da fonte
        font_size=80,
        color="white",
        stroke_color="black",  # Cor da borda
        stroke_width=5  # Espessura da borda
    )
    h3 = TextClip(
        text=f"DIVIDENDOS",
        font="C:/Windows/Fonts/IMPACT.ttf",  # Caminho completo para o arquivo da fonte
        font_size=80,
        color="white",
        stroke_color="black",  # Cor da borda
        stroke_width=5  # Espessura da borda
    )

    # Criar o texto com a cotação (exemplo "Cota: R$ 10.00")
    t1 = TextClip(
        text=f"1",
        font="C:/Windows/Fonts/IMPACT.ttf",  # Caminho completo para o arquivo da fonte
        font_size=80,
        color="white",
        stroke_color="black",  # Cor da borda
        stroke_width=5  # Espessura da borda
    )
    t2 = TextClip(
        text=f"10",
        font="C:/Windows/Fonts/IMPACT.ttf",  # Caminho completo para o arquivo da fonte
        font_size=80,
        color="white",
        stroke_color="black",  # Cor da borda
        stroke_width=5  # Espessura da borda
    )
    t3 = TextClip(
        text=f"100",
        font="C:/Windows/Fonts/IMPACT.ttf",  # Caminho completo para o arquivo da fonte
        font_size=80,
        color="white",
        stroke_color="black",  # Cor da borda
        stroke_width=5  # Espessura da borda
    )
    t4 = TextClip(
        text=f"1000",
        font="C:/Windows/Fonts/IMPACT.ttf",  # Caminho completo para o arquivo da fonte
        font_size=80,
        color="white",
        stroke_color="black",  # Cor da borda
        stroke_width=5  # Espessura da borda
    )
    investido1, dividendos1 = acao.calcular_investimento_e_dividendos(1)
    investido2, dividendos2 = acao.calcular_investimento_e_dividendos(10)
    investido3, dividendos3 = acao.calcular_investimento_e_dividendos(100)
    investido4, dividendos4 = acao.calcular_investimento_e_dividendos(1000)

    v1 = TextClip(
        text=f"R$ {dividendos1}",
        font="C:/Windows/Fonts/IMPACT.ttf",  # Caminho completo para o arquivo da fonte
        font_size=80,
        color="white",
        stroke_color="black",  # Cor da borda
        stroke_width=5  # Espessura da borda
    )
    v2 = TextClip(
        text=f"R$ {dividendos2}",
        font="C:/Windows/Fonts/IMPACT.ttf",  # Caminho completo para o arquivo da fonte
        font_size=80,
        color="white",
        stroke_color="black",  # Cor da borda
        stroke_width=5  # Espessura da borda
    )
    v3 = TextClip(
        text=f"R$ {dividendos3}",
        font="C:/Windows/Fonts/IMPACT.ttf",  # Caminho completo para o arquivo da fonte
        font_size=80,
        color="white",
        stroke_color="black",  # Cor da borda
        stroke_width=5  # Espessura da borda
    )
    v4 = TextClip(
        text=f"R$ {dividendos4}",
        font="C:/Windows/Fonts/IMPACT.ttf",  # Caminho completo para o arquivo da fonte
        font_size=80,
        color="white",
        stroke_color="black",  # Cor da borda
        stroke_width=5  # Espessura da borda
    )

    i1 = TextClip(
        text=f"R$ {investido1}",
        font="C:/Windows/Fonts/IMPACT.ttf",  # Caminho completo para o arquivo da fonte
        font_size=80,
        color="white",
        stroke_color="black",  # Cor da borda
        stroke_width=5  # Espessura da borda
    )
    i2 = TextClip(
        text=f"R$ {investido2}",
        font="C:/Windows/Fonts/IMPACT.ttf",  # Caminho completo para o arquivo da fonte
        font_size=80,
        color="white",
        stroke_color="black",  # Cor da borda
        stroke_width=5  # Espessura da borda
    )
    i3 = TextClip(
        text=f"R$ {investido3}",
        font="C:/Windows/Fonts/IMPACT.ttf",  # Caminho completo para o arquivo da fonte
        font_size=80,
        color="white",
        stroke_color="black",  # Cor da borda
        stroke_width=5  # Espessura da borda
    )
    i4 = TextClip(
        text=f"R$ {investido4}",
        font="C:/Windows/Fonts/IMPACT.ttf",  # Caminho completo para o arquivo da fonte
        font_size=80,
        color="white",
        stroke_color="black",  # Cor da borda
        stroke_width=5  # Espessura da borda
    )
    #header
    h1 = h1.with_position((video.size[0] // 2 - 850, video.size[1] // 2 - 200)).with_duration(60)
    h2 = h2.with_position((video.size[0] // 2 - 300, video.size[1] // 2 - 200)).with_duration(60)
    h3 = h3.with_position((video.size[0] // 2 + 400, video.size[1] // 2 - 200)).with_duration(60)

    # Definir a posição do texto (mover um pouco para a esquerda e para baixo)
    # lado - cima
    t1 = t1.with_position((video.size[0] // 2 - 800, video.size[1] // 2 + 0)).with_duration(60)
    t2 = t2.with_position((video.size[0] // 2 - 800, video.size[1] // 2 + 200)).with_duration(60)
    t3 = t3.with_position((video.size[0] // 2 - 800, video.size[1] // 2 + 400)).with_duration(60)
    t4 = t4.with_position((video.size[0] // 2 - 800, video.size[1] // 2 + 600)).with_duration(60)

    #valores
    v1 = v1.with_position((video.size[0] // 2 + 480, video.size[1] // 2 + 0)).with_duration(60)
    v2 = v2.with_position((video.size[0] // 2 + 480, video.size[1] // 2 + 200)).with_duration(60)
    v3 = v3.with_position((video.size[0] // 2 + 480, video.size[1] // 2 + 400)).with_duration(60)
    v4 = v4.with_position((video.size[0] // 2 + 480, video.size[1] // 2 + 600)).with_duration(60)

    i1 = i1.with_position((video.size[0] // 2 - 230, video.size[1] // 2 + 0)).with_duration(60)
    i2 = i2.with_position((video.size[0] // 2 - 230, video.size[1] // 2 + 200)).with_duration(60)
    i3 = i3.with_position((video.size[0] // 2 - 230, video.size[1] // 2 + 400)).with_duration(60)
    i4 = i4.with_position((video.size[0] // 2 - 230, video.size[1] // 2 + 600)).with_duration(60)

    return h1, h2, h3, t1, t2, t3, t4, v1, v2, v3, v4, i1, i2, i3, i4

def gerar():

    dict_exe = {
        '2': {'ticker1': 'AURE3', 'path': 'templates/template2/trilho_trem.mp4'},
        '3': {'ticker1': 'WEGE3', 'path': 'templates/template2/trilho_trem.mp4'},
        '4': {'ticker1': 'PETR4', 'path': 'templates/template2/trilho_trem.mp4'},
        '5': {'ticker1': 'CPLE3', 'path': 'templates/template2/flor.mp4'},
        '6': {'ticker1': 'TAEE4', 'path': 'templates/template2/trilho_trem.mp4'},
        '7': {'ticker1': 'VALE3', 'path': 'templates/template2/ondas_mar.mp4'},
    }

    # Loop para iterar sobre o dicionário de comparações
    for num_exe, tickers in dict_exe.items():
        # Carregar o vídeo
        video = VideoFileClip(f"{tickers['path']}").with_duration(60)
        video = video.resized(height=1920, width=1080)
        # Instanciar o efeito LumContrast corretamente
        lum_contrast = LumContrast(lum=-50)

        # Aplicar o efeito de redução de brilho
        video = lum_contrast.apply(video)  # Chamada correta para aplicar o efeito

        ticker1 = tickers['ticker1']


        # Criar objetos de ações
        acao1 = Acao(f'{ticker1}')


        # Carregar os dados das ações
        acao1.path_excel = 'data/template2/data.xlsx'
        acao1.load_data_excel()

        # // Cria as variáveis ticker e posiciona no vídeo
        title_text, title_text2 = insert_title(video=video)

        # // Cria as variáveis ticker e posiciona no vídeo
        ticker_text = insert_ticker(video=video, ticker1=ticker1)

        marca_text = insert_marca(video=video)

        # // Adiciona as imagens carregadas da pasta
        img1 = add_images_from_folder(video=video, ticker1=ticker1)

        h1, h2, h3, t1, t2, t3, t4, v1, v2, v3, v4, i1, i2, i3, i4 = insert_table_fix(video=video, acao=acao1)

        # Renderiza o vídeo com todos os textos e imagens
        video_editado = CompositeVideoClip([video,
                                            ticker_text,
                                            marca_text,
                                            img1,
                                            title_text,
                                            title_text2,
                                            h1, h2, h3,
                                            t1, t2, t3, t4,
                                            v1, v2, v3, v4,
                                            i1, i2, i3, i4])

        #video_editado = loop_video(video_editado, min_duration=60)

        # Exportar o vídeo editado para um arquivo de saída
        video_editado.write_videofile(f"videos/template2/{ticker1}-{num_exe}.mp4", codec="libx264", fps=video.fps)


