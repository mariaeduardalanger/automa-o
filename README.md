# 🛠️ Media Asset Processor

Um script de automação em Python desenvolvido para padronizar arquivos de mídia (imagens e áudios) em massa. Ideal para pipelines de desenvolvimento de jogos (como Pygame) ou sistemas que exigem assets com resoluções e formatos fixos.

## 🚀 Funcionalidades

- **Processamento de Imagem:**
  - Redimensionamento automático para **20x20 pixels**.
  - Uso de filtro `NEAREST` para preservação de nitidez em **Pixel Art**.
  - Conversão de múltiplos formatos (`.jpg`, `.bmp`, `.jfif`, etc) para `.png` padronizado.
- **Processamento de Áudio:**
  - Conversão de formatos variados (`.mp3`, `.ogg`, `.flac`) para `.wav`.
  - Integração robusta com **FFmpeg**.
- **Segurança e Logs:**
  - Verificação prévia de ferramentas externas (FFmpeg/FFprobe).
  - Tratamento de exceções individual por arquivo (um erro não trava o processo).

## 📦 Pré-requisitos

Antes de começar, você precisará ter instalado:
- [Python 3.x](https://www.python.org/)
- [FFmpeg](https://ffmpeg.org/download.html) (Essencial para o processamento de áudio)

## 🔧 Instalação

1. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
