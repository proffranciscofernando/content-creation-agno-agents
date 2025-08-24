#!/usr/bin/env python3
"""
Script para gerar imagens PNG/SVG do diagrama de arquitetura.
Usa a API gratuita do mermaid.ink - rápido e sem dependências.

Uso:
    python3 generate_png.py        # Gera PNG (padrão)
    python3 generate_png.py svg    # Gera SVG  
    python3 generate_png.py both   # Gera PNG + SVG
"""

import urllib.request
import urllib.parse
import base64
import os

def generate_architecture_diagram():
    """Retorna o código Mermaid do diagrama."""
    return '''graph TB
    %% Input Sources
    Videos[("🎥 Videos<br/>videos/creator/*.mp4")]
    WebData[("🌐 Web Data<br/>via Tavily API")]
    
    %% Processing Layer
    Transcripter["📝 transcripter.py<br/>FFmpeg + Whisper/Groq"]
    
    %% Data Storage
    TranscriptDB[("📊 transcriptions.json<br/>Structured by Creator")]
    SQLiteDB[("💾 tmp/storage.db<br/>Chat History")]
    
    %% Core Agent
    Agent["🤖 Agent (copywriter)<br/>GPT-4.1-mini + agno"]
    
    %% Tools
    TavilyTool["🔍 TavilyTools<br/>Web Search"]
    ListCreators["📋 list_available_creators<br/>Custom Function"]
    GetTranscripts["📖 get_creator_transcriptions<br/>Custom Function"]
    
    %% Prompt System
    Prompt["📜 prompts/copywriter.md<br/>System Instructions"]
    
    %% Interface
    Playground["🎮 Playground Web UI<br/>Port 8000"]
    User["👤 User<br/>Browser Interface"]
    
    %% Data Flow
    Videos --> Transcripter
    Transcripter --> TranscriptDB
    
    %% Agent Configuration
    Prompt --> Agent
    TranscriptDB --> ListCreators
    TranscriptDB --> GetTranscripts
    WebData --> TavilyTool
    
    %% Agent Tools
    TavilyTool --> Agent
    ListCreators --> Agent
    GetTranscripts --> Agent
    
    %% Storage
    Agent --> SQLiteDB
    SQLiteDB --> Agent
    
    %% User Interface
    Agent --> Playground
    Playground --> User
    User --> Playground
    Playground --> Agent
    
    %% Styling
    classDef storage fill:#e1f5fe
    classDef processing fill:#f3e5f5
    classDef interface fill:#e8f5e8
    classDef agent fill:#fff3e0
    classDef tools fill:#fce4ec
    
    class TranscriptDB,SQLiteDB storage
    class Transcripter processing
    class Playground,User interface
    class Agent agent
    class TavilyTool,ListCreators,GetTranscripts tools'''

def generate_png_via_api(output_file="architecture_diagram.png"):
    """
    Gera PNG usando a API gratuita do mermaid.ink.
    
    Args:
        output_file (str): Nome do arquivo PNG de saída
    
    Returns:
        bool: True se sucesso
    """
    try:
        # Obter código Mermaid
        mermaid_code = generate_architecture_diagram()
        
        # Codificar em base64
        encoded = base64.b64encode(mermaid_code.encode('utf-8')).decode('ascii')
        
        # URL da API mermaid.ink
        url = f"https://mermaid.ink/img/{encoded}"
        
        print(f"🔄 Gerando PNG via mermaid.ink...")
        print(f"📡 URL: {url[:80]}...")
        
        # Fazer requisição
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                # Salvar imagem
                with open(output_file, 'wb') as f:
                    f.write(response.read())
                
                print(f"✅ PNG gerado com sucesso: {output_file}")
                return True
            else:
                print(f"❌ Erro na API: Status {response.status}")
                return False
                
    except Exception as e:
        print(f"❌ Erro ao gerar PNG: {e}")
        return False

def generate_svg_via_api(output_file="architecture_diagram.svg"):
    """
    Gera SVG usando a API gratuita do mermaid.ink.
    
    Args:
        output_file (str): Nome do arquivo SVG de saída
    
    Returns:
        bool: True se sucesso
    """
    try:
        # Obter código Mermaid
        mermaid_code = generate_architecture_diagram()
        
        # Codificar em base64
        encoded = base64.b64encode(mermaid_code.encode('utf-8')).decode('ascii')
        
        # URL da API mermaid.ink para SVG
        url = f"https://mermaid.ink/svg/{encoded}"
        
        print(f"🔄 Gerando SVG via mermaid.ink...")
        
        # Fazer requisição
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                # Salvar imagem
                with open(output_file, 'wb') as f:
                    f.write(response.read())
                
                print(f"✅ SVG gerado com sucesso: {output_file}")
                return True
            else:
                print(f"❌ Erro na API: Status {response.status}")
                return False
                
    except Exception as e:
        print(f"❌ Erro ao gerar SVG: {e}")
        return False

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "png":
            generate_png_via_api()
        elif command == "svg":
            generate_svg_via_api()
        elif command == "both":
            generate_png_via_api()
            generate_svg_via_api()
        else:
            print("❌ Comando inválido!")
            print("Uso: python3 generate_png.py [png|svg|both]")
            print("  png  - Gera imagem PNG")
            print("  svg  - Gera imagem SVG") 
            print("  both - Gera PNG e SVG")
    else:
        # Padrão: gerar PNG
        generate_png_via_api()
