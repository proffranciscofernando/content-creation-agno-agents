# Template para Sistemas de Agentes Agno

Este documento fornece um template completo para criar sistemas profissionais de agentes de IA usando o framework agno, seguindo as melhores práticas de arquitetura e documentação.

## 🎯 Visão Geral

Use este template para criar sistemas de agentes que seguem uma arquitetura estruturada, com processamento de dados inteligente, documentação automática e interface profissional.

## 📋 Metodologia

### 1. Definição do Domínio

Antes de começar, defina claramente:

- **Propósito principal**: Qual problema o sistema resolve?
- **Usuários-alvo**: Quem vai usar o sistema?
- **Dados de entrada**: Que tipo de informação será processada?
- **Saída esperada**: Qual resultado final o usuário receberá?

### 2. Arquitetura de Componentes

#### Processamento de Dados
- **Script de ingestão**: Para processar dados brutos (documentos, vídeos, APIs, etc.)
- **Formato estruturado**: JSON ou banco de dados para armazenar dados processados
- **Funções de leitura**: Para que o agente acesse os dados de forma eficiente

#### Agente Central
```python
agente = Agent(
    model=OpenAIChat(id="gpt-4.1-mini"),
    name="[nome_do_agente]",
    add_history_to_messages=True,
    num_history_runs=10,
    storage=SqliteStorage(table_name="agent_sessions", 
                          db_file="tmp/storage.db"),
    tools=[
        TavilyTools(),  # Pesquisa web
        funcao_customizada_1,
        funcao_customizada_2
    ],
    show_tool_calls=True,
    instructions=open("prompts/[agente].md").read()
)
```

#### Sistema de Ferramentas
- **Pesquisa externa**: TavilyTools para informações atualizadas
- **2-3 funções customizadas**: Para acessar dados específicos do domínio
- **Funções de listagem**: Para mostrar opções disponíveis ao usuário

## 📁 Estrutura de Arquivos

```
projeto/
├── agent.py                    # Agente principal + servidor
├── [processador].py           # Script de processamento de dados
├── [leitor].py               # Funções de acesso aos dados
├── prompts/
│   └── [agente].md           # Instruções detalhadas
├── dados/
│   └── [estrutura_organizada] # Dados organizados por categoria
├── [dados_processados].json  # Base de conhecimento estruturada
├── tmp/
│   └── storage.db           # Histórico de conversas
├── pyproject.toml           # Dependências
├── README.md               # Documentação
├── architecture.md         # Diagrama + explicação
├── generate_png.py         # Script para gerar diagramas
└── architecture_diagram.png # Visualização
```

## 📝 Prompt do Agente

O arquivo `prompts/[agente].md` deve conter:

### ROLE
- Especialização clara e específica
- Contexto sobre os dados disponíveis
- Capacidades e limitações

### WORKFLOW
1. **Análise inicial**: Como abordar requests complexos
2. **Pesquisa**: Quando e como usar ferramentas externas
3. **Processamento**: Como combinar dados internos + externos
4. **Entrega**: Formato e qualidade da resposta final

### TOOLS USAGE
- **Pesquisa web**: Para informações atualizadas
- **Dados internos**: Para exemplos e padrões específicos
- **Combinação inteligente**: Como usar ambos efetivamente

### OUTPUT QUALITY
- Critérios de qualidade específicos do domínio
- Exemplos de boas práticas
- Métricas de sucesso

## 🔧 Funcionalidades Essenciais

### Processamento Inteligente
```python
def processar_dados():
    """
    Converte dados brutos em formato estruturado
    que o agente pode usar eficientemente
    """
    pass

def listar_categorias():
    """Lista categorias/tipos disponíveis"""
    pass

def obter_dados_especificos(categoria, filtros=None):
    """Obtém dados específicos com filtros"""
    pass
```

### Interface Playground
```python
playground = Playground(agents=[agente]).get_app()

if __name__ == "__main__":
    serve_playground_app(playground, port=8000)
```

## 📊 Documentação Visual

### Script de Diagrama
- Gera automaticamente diagrama Mermaid da arquitetura
- Produz PNG via API (sem dependências pesadas)
- Código versionável + imagem visual

### Componentes do Diagrama
- **Entrada de dados** → **Processamento** → **Base estruturada**
- **Agente central** com **ferramentas conectadas**
- **Interface usuário** ↔ **Agente** ↔ **Storage**
- **Cores por categoria**: Dados, processamento, agente, interface, ferramentas

## 📦 Dependências

```toml
[project]
name = "seu-projeto-agno"
version = "0.1.0"
description = "Sistema de agentes usando agno framework"
requires-python = ">=3.12"
dependencies = [
    "agno>=1.5.0",
    "openai>=1.99.2",
    "tavily-python>=0.7.10",
    "python-dotenv>=1.1.1",
    "fastapi>=0.116.1",
    "uvicorn>=0.35.0"
]
```

## ✅ Critérios de Qualidade

### Funcional
- [x] Agente responde adequadamente ao domínio
- [x] Ferramentas integradas funcionam
- [x] Interface web acessível
- [x] Dados processados corretamente

### Profissional
- [x] Código limpo e organizado
- [x] Documentação completa
- [x] Diagramas visuais
- [x] README com instruções claras

### Escalável
- [x] Fácil adicionar novos dados
- [x] Estrutura modular
- [x] Configuração via arquivos
- [x] Logs e debugging

## 🚀 Exemplos de Aplicação

Adapte esta estrutura para qualquer domínio:

- **Análise financeira**: PDFs → dados financeiros → agente consultor
- **Suporte técnico**: Documentação → base conhecimento → agente help desk
- **Criação educacional**: Materiais → currículo estruturado → agente tutor
- **Análise legal**: Contratos → base jurídica → agente assistente
- **Marketing**: Campanhas → estratégias → agente criativo

## 🎯 Como Usar Este Template

1. **Clone ou adapte** a estrutura de arquivos
2. **Defina seu domínio** específico
3. **Implemente o processador** de dados
4. **Configure o agente** com prompt detalhado
5. **Crie funções customizadas** para seu domínio
6. **Teste e itere** até atingir qualidade desejada
7. **Documente visualmente** com diagramas
8. **Deploy** com interface profissional

## 📚 Recursos Adicionais

- [Documentação do Agno](https://docs.agno.ai)
- [Mermaid Syntax](https://mermaid.js.org/)
- [OpenAI API](https://platform.openai.com/docs)
- [Tavily API](https://tavily.com/docs)

## 🤝 Contribuição

Este template foi criado para acelerar o desenvolvimento de sistemas de agentes profissionais. Contribuições e melhorias são bem-vindas!

---

**Execute este template e obtenha um sistema profissional, documentado e visualmente atraente que demonstra as capacidades completas do framework agno!**
