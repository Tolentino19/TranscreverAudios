import os
import whisper
from datetime import datetime

def transcribe_folder(input_folder, output_folder, update_status):
    # Load the model
    model = whisper.load_model("base")

    # Get the list of audio files
    audio_files = [f for f in os.listdir(input_folder)]
    print(audio_files)

    for audio_file in audio_files:
        try:
            # Update the status
            update_status(f"Transcrevendo: {audio_file}...")

            # Full path to the audio file
            audio_path = os.path.join(input_folder, audio_file)

            # Transcribe the audio file
            result = model.transcribe(audio_path, fp16=False)

            # Get the transcription text
            transcription = result["text"]

            # Create the output text
            text = f"Arquivo: {audio_file}\nTranscrito em: {datetime.now()}\n\nTranscrição:\n{transcription}"

            # Save the transcription to a text file
            text_file = os.path.splitext(audio_file)[0] + '.txt'
            text_path = os.path.join(output_folder, text_file)
            with open(text_path, 'w') as f:
                f.write(text)

            # Update the status
            update_status(f"Transcrevendo: {audio_file}... Feito")

        except Exception as e:
            update_status(f"Erro ao transcrever {audio_file}: {e}")

    # Update the status
    update_status("Todas as transcrições foram finalizadas")
