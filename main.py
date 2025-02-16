from moviepy import VideoFileClip, TextClip, CompositeVideoClip, ImageClip
import os


def add_images_from_folder(video, folder_path="img/"):
    """
    Carrega duas imagens da pasta 'img/', redimensiona para o tamanho padrão e posiciona lado a lado no vídeo.
    """
    # Listar os arquivos de imagem na pasta img/
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]

    if len(image_files) < 2:
        raise ValueError("A pasta img/ deve conter pelo menos duas imagens.")

    # Carregar as duas primeiras imagens da pasta
    image1_path = os.path.join(folder_path, image_files[0])
    image2_path = os.path.join(folder_path, image_files[1])

    # Criar os ImageClip a partir das imagens
    img1 = ImageClip(image1_path)
    img2 = ImageClip(image2_path)

    # Redimensionar as imagens para um tamanho padrão
    img1 = img1.resized(height=200)  # Redimensionar para uma altura de 100 px
    img2 = img2.resized(height=200)  # Redimensionar para uma altura de 100 px

    # Definir a duração das imagens
    img1 = img1.with_duration(3)
    img2 = img2.with_duration(3)

    # Posicionar as imagens lado a lado
    img1 = img1.with_position((video.size[0] // 2 - 350, video.size[1] // 2 - 430))
    img2 = img2.with_position((video.size[0] // 2 + 180, video.size[1] // 2 - 430))

    return img1, img2


def insert_ticker(video):
    """
    Cria variáveis de ticker no vídeo e posiciona na tela
    """
    # Criar o texto com a cotação (exemplo "Cota: R$ 10.00")
    ticker_text = TextClip(
        text="BBAS3",
        font="C:/Windows/Fonts/ARLRDBD.ttf",  # Caminho completo para o arquivo da fonte
        font_size=30,
        color="white"
    )

    # Criar o texto com a cotação (exemplo "Cota: R$ 20.00")
    ticker_text2 = TextClip(
        text="ITUB3",
        font="C:/Windows/Fonts/ARLRDBD.ttf",  # Caminho completo para o arquivo da fonte
        font_size=30,
        color="white"
    )

    # Definir a posição do texto (mover um pouco para a esquerda e para baixo)
    ticker_text = ticker_text.with_position((video.size[0] // 2 - 300, video.size[1] // 2 - 200)).with_duration(3)
    ticker_text2 = ticker_text2.with_position((video.size[0] // 2 + 200, video.size[1] // 2 - 200)).with_duration(3)

    return ticker_text, ticker_text2


def insert_cota(video):
    """
    Cria variáveis de cota no vídeo e posiciona na tela
    """
    cota_text = TextClip(
        text="Cota: R$ 10.00",
        font="C:/Windows/Fonts/ARLRDBD.ttf",
        font_size=50,
        color="white"
    )
    cota_text2 = TextClip(
        text="Cota: R$ 20.00",
        font="C:/Windows/Fonts/ARLRDBD.ttf",
        font_size=50,
        color="white"
    )
    cota_text = cota_text.with_position((video.size[0] // 2 - 400, video.size[1] // 2 - 40)).with_duration(3)
    cota_text2 = cota_text2.with_position((video.size[0] // 2 + 80, video.size[1] // 2 - 40)).with_duration(3)

    return cota_text, cota_text2


def insert_pl(video):
    """
    Cria variáveis de preço sobre lucro e posiciona no vídeo
    """
    pl_text = TextClip(
        text="P/L: 1.00",
        font="C:/Windows/Fonts/ARLRDBD.ttf",
        font_size=50,
        color="white"
    )
    pl_text2 = TextClip(
        text="P/L: 12.00",
        font="C:/Windows/Fonts/ARLRDBD.ttf",
        font_size=50,
        color="white"
    )
    pl_text = pl_text.with_position((video.size[0] // 2 - 400, video.size[1] // 2 + 160)).with_duration(3)
    pl_text2 = pl_text2.with_position((video.size[0] // 2 + 80, video.size[1] // 2 + 160)).with_duration(3)

    return pl_text, pl_text2


def insert_pvp(video):
    """
    Cria variáveis de preço sobre valor patrimonial e posiciona no vídeo
    """
    pvp_text = TextClip(
        text="P/VP: 1.00",
        font="C:/Windows/Fonts/ARLRDBD.ttf",
        font_size=50,
        color="white"
    )
    pvp_text2 = TextClip(
        text="P/VP: 12.00",
        font="C:/Windows/Fonts/ARLRDBD.ttf",
        font_size=50,
        color="white"
    )
    pvp_text = pvp_text.with_position((video.size[0] // 2 - 400, video.size[1] // 2 + 380)).with_duration(3)
    pvp_text2 = pvp_text2.with_position((video.size[0] // 2 + 80, video.size[1] // 2 + 380)).with_duration(3)

    return pvp_text, pvp_text2


def insert_dy(video):
    """
    Cria variáveis de dividend yield e posiciona no vídeo
    """
    dy_text = TextClip(
        text="DY: 10.00%",
        font="C:/Windows/Fonts/ARLRDBD.ttf",
        font_size=50,
        color="white"
    )
    dy_text2 = TextClip(
        text="DY: 9,56%",
        font="C:/Windows/Fonts/ARLRDBD.ttf",
        font_size=50,
        color="white"
    )
    dy_text = dy_text.with_position((video.size[0] // 2 - 400, video.size[1] // 2 + 565)).with_duration(3)
    dy_text2 = dy_text2.with_position((video.size[0] // 2 + 80, video.size[1] // 2 + 565)).with_duration(3)

    return dy_text, dy_text2


def main():
    # Carregar o template do vídeo
    video = VideoFileClip("templates/template_qual_das_duas_voce_investiria.mp4")

    # // Cria as variáveis ticker e posiciona no vídeo
    ticker_text, ticker_text2 = insert_ticker(video)

    # // Cria as variáveis cotas e posiciona na tela
    cota_text, cota_text2 = insert_cota(video)

    # // Cria as variáveis Preço / Lucro e posiciona na tela
    pl_text, pl_text2 = insert_pl(video)

    # // Cria as variáveis Preço / Valor Patrimonial
    pvp_text, pvp_text2 = insert_pvp(video)

    # // Cria as variáveis dividend yield
    dy_text, dy_text2 = insert_dy(video)

    # // Adiciona as imagens carregadas da pasta
    img1, img2 = add_images_from_folder(video)

    # Renderiza o vídeo com todos os textos e imagens
    video_editado = CompositeVideoClip([video,
                                        ticker_text, ticker_text2,
                                        cota_text, cota_text2,
                                        pl_text, pl_text2,
                                        pvp_text, pvp_text2,
                                        dy_text, dy_text2,
                                        img1, img2])

    # Exportar o vídeo editado para um arquivo de saída
    video_editado.write_videofile("output.mp4", codec="libx264", fps=video.fps)


if __name__ == "__main__":
    main()
