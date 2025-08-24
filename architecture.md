# Arquitetura do Projeto Content Creation Agno Agents

## Diagrama de Arquitetura

```mermaid
graph TB
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
    class TavilyTool,ListCreators,GetTranscripts tools
```

## Componentes Principais

### 🎯 Camada de Entrada
- **Videos**: Vídeos MP4 organizados por criador em `videos/creator/*.mp4`
- **Web Data**: Informações externas obtidas via API Tavily

### ⚙️ Camada de Processamento
- **transcripter.py**: Extrai áudio usando FFmpeg e transcreve usando Whisper/Groq

### 💾 Camada de Dados
- **transcriptions.json**: Base estruturada de transcrições organizadas por criador
- **tmp/storage.db**: Histórico de conversas armazenado em SQLite

### 🤖 Camada Central (Agente)
- **Agent (copywriter)**: Agente principal usando GPT-4.1-mini + framework agno
- **3 Ferramentas disponíveis**:
  - TavilyTools: Pesquisa na web
  - list_available_creators: Lista criadores disponíveis
  - get_creator_transcriptions: Obtém transcrições de um criador específico

### 🎮 Camada de Interface
- **Playground Web UI**: Interface web na porta 8000 para interação com o usuário

## Fluxo de Dados

1. **Preparação dos Dados**: 
   - `transcripter.py` processa vídeos da pasta `videos/`
   - Gera arquivo `transcriptions.json` estruturado

2. **Configuração do Agente**: 
   - Agente carrega prompt do arquivo `prompts/copywriter.md`
   - Configura ferramentas e acesso aos dados de transcrição

3. **Interação do Usuário**: 
   - Usuário acessa interface web via navegador
   - Conversa com agente através do Playground

4. **Processamento de Requisições**: 
   - Agente usa ferramentas para pesquisar web e acessar transcrições
   - Gera conteúdo baseado no estilo dos criadores

5. **Persistência**: 
   - Conversas são salvas no SQLite para manter histórico
   - Dados ficam disponíveis entre sessões

## Características da Arquitetura

### ✅ Modular e Desacoplada
- Transcrição independente do agente principal
- Componentes podem ser atualizados separadamente

### ✅ Extensível
- Fácil adição de novos criadores (apenas adicionar vídeos na pasta)
- Novas ferramentas podem ser integradas facilmente

### ✅ Persistente
- Histórico de conversas mantido entre sessões
- Base de transcrições reutilizável

### ✅ Web-based
- Acesso via navegador, sem necessidade de instalação no cliente
- Interface amigável através do Playground do agno

## Tecnologias Utilizadas

- **Framework de Agentes**: agno
- **Modelo de IA**: OpenAI GPT-4.1-mini
- **Transcrição**: Whisper via Groq API
- **Processamento de Áudio**: FFmpeg
- **Pesquisa Web**: Tavily API
- **Banco de Dados**: SQLite
- **Interface Web**: FastAPI + Playground
- **Gerenciamento de Dependências**: uv
