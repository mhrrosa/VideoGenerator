from moviepy import VideoFileClip, TextClip, CompositeVideoClip, ImageClip, AudioFileClip, concatenate_videoclips
import os
from Acao import Acao
import random

def add_images_from_folder(video,ticker1, ticker2, folder_path="img/"):
    """
    Carrega duas imagens da pasta 'img/', redimensiona para o tamanho padrão e posiciona lado a lado no vídeo.
    """
    # Listar os arquivos de imagem na pasta img/
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]

    image1_path = ''
    image2_path = ''

    for img in image_files:
        if ticker1 == img.split('.')[0]:
            image1_path = os.path.join(folder_path, img)

    for img in image_files:
        if ticker2 == img.split('.')[0]:
            image2_path = os.path.join(folder_path, img)

    # Criar os ImageClip a partir das imagens
    img1 = ImageClip(image1_path)
    img2 = ImageClip(image2_path)

    # Redimensionar as imagens para um tamanho padrão
    img1 = img1.resized(height=200)  # Redimensionar para uma altura de 100 px
    img2 = img2.resized(height=200)  # Redimensionar para uma altura de 100 px

    # Definir a duração das imagens
    img1 = img1.with_duration(14.3)
    img2 = img2.with_duration(14.3)

    # Posicionar as imagens lado a lado
    img1 = img1.with_position((video.size[0] // 2 - 350, video.size[1] // 2 - 430))
    img2 = img2.with_position((video.size[0] // 2 + 180, video.size[1] // 2 - 430))

    return img1, img2


def insert_ticker(video, ticker1, ticker2):
    """
    Cria variáveis de ticker no vídeo e posiciona na tela
    """
    # Criar o texto com a cotação (exemplo "Cota: R$ 10.00")
    ticker_text = TextClip(
        text=f"{ticker1}",
        font="C:/Windows/Fonts/ARLRDBD.ttf",  # Caminho completo para o arquivo da fonte
        font_size=30,
        color="white"
    )

    # Criar o texto com a cotação (exemplo "Cota: R$ 20.00")
    ticker_text2 = TextClip(
        text=f"{ticker2}",
        font="C:/Windows/Fonts/ARLRDBD.ttf",  # Caminho completo para o arquivo da fonte
        font_size=30,
        color="white"
    )

    # Definir a posição do texto (mover um pouco para a esquerda e para baixo)
    ticker_text = ticker_text.with_position((video.size[0] // 2 - 300, video.size[1] // 2 - 200)).with_duration(14.3)
    ticker_text2 = ticker_text2.with_position((video.size[0] // 2 + 200, video.size[1] // 2 - 200)).with_duration(14.3)

    return ticker_text, ticker_text2


def insert_cota(video, cota1, cota2):
    """
    Cria variáveis de cota no vídeo e posiciona na tela
    """
    cota_text = TextClip(
        text=f"Cota: {cota1}",
        font="C:/Windows/Fonts/ARLRDBD.ttf",
        font_size=50,
        color="white"
    )
    cota_text2 = TextClip(
        text=f"Cota: {cota2}",
        font="C:/Windows/Fonts/ARLRDBD.ttf",
        font_size=50,
        color="white"
    )
    cota_text = cota_text.with_position((video.size[0] // 2 - 400, video.size[1] // 2 - 40)).with_start(3.3).with_end(14.3)
    cota_text2 = cota_text2.with_position((video.size[0] // 2 + 80, video.size[1] // 2 - 40)).with_start(3.3).with_end(14.3)

    return cota_text, cota_text2


def insert_pl(video, pl1, pl2):
    """
    Cria variáveis de preço sobre lucro e posiciona no vídeo
    """
    pl_text = TextClip(
        text=f"P/L: {pl1}",
        font="C:/Windows/Fonts/ARLRDBD.ttf",
        font_size=50,
        color="white"
    )
    pl_text2 = TextClip(
        text=f"P/L: {pl2}",
        font="C:/Windows/Fonts/ARLRDBD.ttf",
        font_size=50,
        color="white"
    )
    pl_text = pl_text.with_position((video.size[0] // 2 - 400, video.size[1] // 2 + 160)).with_start(5.9).with_end(14.3)
    pl_text2 = pl_text2.with_position((video.size[0] // 2 + 80, video.size[1] // 2 + 160)).with_start(5.9).with_end(14.3)

    return pl_text, pl_text2


def insert_pvp(video, pvp1, pvp2):
    """
    Cria variáveis de preço sobre valor patrimonial e posiciona no vídeo
    """
    pvp_text = TextClip(
        text=f"P/VP: {pvp1}",
        font="C:/Windows/Fonts/ARLRDBD.ttf",
        font_size=50,
        color="white"
    )
    pvp_text2 = TextClip(
        text=f"P/VP: {pvp2}",
        font="C:/Windows/Fonts/ARLRDBD.ttf",
        font_size=50,
        color="white"
    )
    pvp_text = pvp_text.with_position((video.size[0] // 2 - 400, video.size[1] // 2 + 380)).with_start(8.8).with_end(14.3)
    pvp_text2 = pvp_text2.with_position((video.size[0] // 2 + 80, video.size[1] // 2 + 380)).with_start(8.8).with_end(14.3)


    return pvp_text, pvp_text2


def insert_dy(video, dy1, dy2):
    """
    Cria variáveis de dividend yield e posiciona no vídeo
    """
    dy_text = TextClip(
        text=f"DY: {dy1}%",
        font="C:/Windows/Fonts/ARLRDBD.ttf",
        font_size=50,
        color="white"
    )
    dy_text2 = TextClip(
        text=f"DY: {dy2}%",
        font="C:/Windows/Fonts/ARLRDBD.ttf",
        font_size=50,
        color="white"
    )
    dy_text = dy_text.with_position((video.size[0] // 2 - 400, video.size[1] // 2 + 565)).with_start(11.8).with_end(14.3)
    dy_text2 = dy_text2.with_position((video.size[0] // 2 + 80, video.size[1] // 2 + 565)).with_start(11.8).with_end(14.3)

    return dy_text, dy_text2


def get_random_song(folder_path="song/"):
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


def add_background_music(video, song_path):
    """
    Adiciona uma música de fundo ao vídeo, ajustando a duração da música para ser igual à do vídeo.
    """
    audio = AudioFileClip(song_path)

    # Ajustar duração da música
    if audio.duration < video.duration:
        audio = audio.loop(duration=video.duration)  # Repete a música até o tempo do vídeo
    else:
        audio = audio.subclipped(0, video.duration)  # Corta a música se for maior que o vídeo

    video = video.with_audio(audio)
    return video

def loop_video(video, min_duration=60):
    """
    Duplica o vídeo até atingir pelo menos a duração mínima especificada.
    """
    clips = []
    total_duration = 0

    while total_duration < min_duration:
        clips.append(video)
        total_duration += video.duration
    return concatenate_videoclips(clips)


def main():
    # Carregar o template do vídeo
    video = VideoFileClip("templates/template_qual_das_duas_voce_investiria.mp4")

    dict_exe = {
        '9': {'ticker1': 'VALE3', 'ticker2': 'GOAU4'},
    }

    # Loop para iterar sobre o dicionário de comparações
    for num_exe, tickers in dict_exe.items():
        ticker1 = tickers['ticker1']
        ticker2 = tickers['ticker2']

        # Criar objetos de ações
        acao1 = Acao(f'{ticker1}.SA')
        acao2 = Acao(f'{ticker2}.SA')

        # Carregar os dados das ações
        acao1.load_data()
        acao2.load_data()

        acao2.show_data()

        # // Cria as variáveis ticker e posiciona no vídeo
        ticker_text, ticker_text2 = insert_ticker(video=video, ticker1=ticker1, ticker2=ticker2)

        # // Cria as variáveis cotas e posiciona na tela
        cota_text, cota_text2 = insert_cota(video=video, cota1=acao1.cota, cota2=acao2.cota)

        # // Cria as variáveis Preço / Lucro e posiciona na tela
        pl_text, pl_text2 = insert_pl(video=video, pl1=acao1.pl, pl2=acao2.pl)

        # // Cria as variáveis Preço / Valor Patrimonial
        pvp_text, pvp_text2 = insert_pvp(video, pvp1=acao1.pvp, pvp2=acao2.pvp)

        # // Cria as variáveis dividend yield
        dy_text, dy_text2 = insert_dy(video, dy1=acao1.dy, dy2=acao2.dy)

        # // Adiciona as imagens carregadas da pasta
        img1, img2 = add_images_from_folder(video, ticker1, ticker2)

        # Renderiza o vídeo com todos os textos e imagens
        video_editado = CompositeVideoClip([video,
                                            ticker_text, ticker_text2,
                                            cota_text, cota_text2,
                                            pl_text, pl_text2,
                                            pvp_text, pvp_text2,
                                            dy_text, dy_text2,
                                            img1, img2])

        video_editado = loop_video(video_editado, min_duration=60)

        # Adiciona música de fundo ao vídeo
        random_song_path = get_random_song()
        video_editado = add_background_music(video_editado, random_song_path)

        # Exportar o vídeo editado para um arquivo de saída
        video_editado.write_videofile(f"videos/{ticker1}-{ticker2}{num_exe}.mp4", codec="libx264", fps=video.fps)


if __name__ == "__main__":
    main()
