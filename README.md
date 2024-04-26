Como utilizar:

1º Instale a última versão de Python (https://www.python.org/downloads/)

2ª Na linha de comando digite o seguinte comando para installar o Whisper da OpenAI: 

    pip install -U openai-whisper

3ª Ainda na linha de comando digite os seguintes comandos para instalar o ffmpeg: 
    
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

    Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

Em caso de erro neste último comando utilize o seguinte:

    iex "& {$(irm get.scoop.sh)} -RunAsAdmin"

  Por fim este último comando:

    scoop install ffmpeg

3º Baixe todos os arquivos (main.py; whisper_gui.py; whisper_transcribe.py) e salve-os na mesma pasta

4º Abra a linha de comando na mesma pasta onde você salvou os arquivos acima e digite o seguinte comando para executar o programa: 

    python main.py

5º Irá aparecer uma interface de usuário simples

6º Clique em "Começar a transcrever"

7º Vai abrir uma janela pedindo para você escolher a pasta de origem onde estão os áudios que você quer transcrever, os arquivos existentes dentro da pasta não estarão listados, mas não há problema, ignore e continue

8º Logo após selecionar a pasta de origem já vai abrir outra janela pedindo para escolher a pasta onde você quer salvar as transcrições, após selecionar é só aguardar a(s) transcrição(ões) terminarem

9º Ao finalizar as transcrições irá aparecer "Todas as transcrições foram finalizadas" na interface

10º Os arquivos de texto irão estar na pasta destino que você selecionou em arquivos .txt (um por áudio).
