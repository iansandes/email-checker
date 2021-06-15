# Offensive Email Checker :mailbox_with_mail:
Uma ferramenta de envio de emails via CLI com funcionalidade de filtragem de conteúdos ofensivos.

## Como rodar :rocket:
É preciso ter o [python 3](https://www.python.org/downloads/) instalado na sua máquina.

Clone o repositório e acesse o projeto:
```bash
$ git clone https://github.com/iansandes/email-checker && cd email-checker
```

Instale as dependências
```bash
$ pip install -r requirements.txt
```

Crie um arquivo `.env` a partir de `env.example`
```bash
$ cp env.example .env
```

Execute com:
```bash
$ python main.py
```

### Exemplo de execução do programa
```
❯ python main.py

 -=-=-=-=-=- Email Sender with content checker -=-=-=-=-=-
To: iansandes15@gmail.com
Subject: otario
Content: oi

Email Not Sent! The following terms contain offensive or inappropriate language:
- Otario
```
