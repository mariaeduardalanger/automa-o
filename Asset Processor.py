import os
import sys
from PIL import Image
from pydub import AudioSegment

# --- CONFIGURAÇÃO DE CAMINHOS ---
BASE_DIR = r'C:\Users\maria\Documents\portfolio programação'
INPUT_DIR = os.path.join(BASE_DIR, 'assets_brutos')
OUTPUT_DIR = os.path.join(BASE_DIR, 'assets_processados')

# FORÇAR O CAMINHO DO FFMPEG (Onde o motor do áudio mora)
FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"
FFPROBE_PATH = r"C:\ffmpeg\bin\ffprobe.exe"

AudioSegment.converter = FFMPEG_PATH
AudioSegment.ffprobe = FFPROBE_PATH

IMAGE_SIZE = (20, 20)
AUDIO_FORMAT = "wav" 

def check_tools():
    """Verifica se o FFmpeg está acessível antes de tentar converter o som."""
    print("--- VERIFICANDO FERRAMENTAS ---")
    ffmpeg_ok = os.path.exists(FFMPEG_PATH)
    ffprobe_ok = os.path.exists(FFPROBE_PATH)
    
    if ffmpeg_ok and ffprobe_ok:
        print("✅ FFmpeg e FFprobe encontrados com sucesso!")
        return True
    else:
        if not ffmpeg_ok: print(f"❌ ALERTA: FFmpeg não está em {FFMPEG_PATH}")
        if not ffprobe_ok: print(f"❌ ALERTA: FFprobe não está em {FFPROBE_PATH}")
        print("DICA: Verifique se extraiu a pasta 'bin' corretamente para dentro de C:\\ffmpeg")
        return False

def process_assets():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    if not os.path.exists(INPUT_DIR):
        print(f"❌ Erro: Pasta '{INPUT_DIR}' não encontrada.")
        return

    arquivos = os.listdir(INPUT_DIR)
    if not arquivos:
        print("⚠️ Pasta vazia! Coloque fotos ou músicas em 'assets_brutos'.")
        return

    for filename in arquivos:
        file_path = os.path.join(INPUT_DIR, filename)
        base_name, ext = os.path.splitext(filename)
        ext = ext.lower()

        # --- PROCESSAR IMAGENS ---
        if ext in ['.png', '.jpg', '.jpeg', '.bmp', '.jfif']:
            try:
                with Image.open(file_path) as img:
                    img = img.convert("RGB")
                    img_res = img.resize(IMAGE_SIZE, Image.Resampling.NEAREST)
                    img_res.save(os.path.join(OUTPUT_DIR, f"{base_name}.png"), "PNG")
                    print(f"✔ Imagem: {filename} -> 20x20")
            except Exception as e:
                print(f"✘ Erro na imagem {filename}: {e}")

        # --- PROCESSAR ÁUDIO ---
        elif ext in ['.mp3', '.wav', '.ogg', '.flac']:
            try:
                audio = AudioSegment.from_file(file_path)
                out_path = os.path.join(OUTPUT_DIR, f"{base_name}.{AUDIO_FORMAT}")
                audio.export(out_path, format=AUDIO_FORMAT)
                print(f"✔ Áudio: {filename} -> {AUDIO_FORMAT}")
            except Exception as e:
                print(f"✘ Erro no áudio {filename}: {e}")

if __name__ == "__main__":
    print("\n--- INICIANDO SCRIPT ---")
    check_tools()
    process_assets()
    print("--- FIM DO PROCESSO ---\n")