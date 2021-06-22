from pytube import YouTube

n_videos = input('Quantos vídeos você quer baixar? Digite apenas o número:')
links = []

# Quantidade de vídeos que deseja baixar
for i in range(int(n_videos)):
    temp = input('Digite o link do vídeo {} °:'.format(i+1))
    
    # Adiciona o link do vídeo na lista de links 
    links.append(temp)

# Realizando o loop para baixar os vídeos informados
for j in range(len(links)):

    # Cria objeto com URL do vídeo a ser baixado
    video = YouTube(links[j])

    # Configura a melhor qualidade dos vídeos
    stream = video.streams.get_highest_resolution()

    # Faz o download do vídeo e o salva na pasta 'saída'
    stream.download(output_path='./saida')

    print('{}° vídeo baixado'.format(j+1))

print('fim do processo =D')