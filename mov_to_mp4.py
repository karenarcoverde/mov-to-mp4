import os
import subprocess

FFMPEG_PATH = r"C:\Users\karen\Downloads\FL-MESTRADO\ffmpeg.exe"  # <-- ajusta aqui

def convert_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):
        if file.lower().endswith(".mov"):
            input_file = os.path.join(input_folder, file)
            base = os.path.splitext(file)[0]
            output_file = os.path.join(output_folder, base + ".mp4")

            command = [
                FFMPEG_PATH,
                "-y",
                "-i", input_file,
                "-c:v", "copy",
                "-c:a", "copy",
                output_file
            ]

            result = subprocess.run(command, capture_output=True, text=True)

            if result.returncode == 0:
                print("Convertido:", output_file)
            else:
                print("Erro ao converter:", input_file)
                print(result.stderr)

convert_folder("imagens/", "videos_mp4/")
