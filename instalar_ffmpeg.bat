@echo off
echo Configurando a política de execução...
powershell -Command "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser"

echo Baixando e instalando o Scoop...
powershell -Command "Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression"

echo Instalando o ffmpeg via Scoop...
scoop install ffmpeg

echo Todos os comandos foram executados com sucesso.
pause
