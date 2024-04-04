# Projeto pass.in NLW Unite 2024.1


## Do que se trata

### pass.in

O **pass.in** é uma aplicação focada na **gestão de participantes em eventos presenciais**. Ela oferece uma solução prática para que organizadores possam cadastrar eventos e criar páginas públicas de inscrição. Os participantes inscritos têm a possibilidade de emitir credenciais para o check-in no dia do evento, enquanto o sistema gerencia a entrada por meio de um scan das credenciais.

### Tecnologias Utilizadas

Este projeto, desenvolvido inteiramente em Python, desfruta das seguintes dependências:

- Flask
- DBeaver
- SQLite
- SQLAlchemy

## Requisitos

### Funcionalidades

- [ ] O organizador pode cadastrar um novo evento atribuindo seu Título, Detalhes, Slug e Quantidade máxima de pessoas.

- [ ] O organizador pode visualizar dados de um determinado evento através de seu ID.

- [ ] O organizador pode visualizar a lista de participantes do evento através do ID do respectivo evento que ele deseja consultar.

- [ ] O participante pode se inscrever em um evento através do preenchimento de seus dados (nome, e-mail).

- [ ] O participante pode visualizar seu crachá de inscrição, que conterá o seu nome, e-mail, ID, o ID do evento que ele se inscreveu e a data e hora de sua inscrição.

- [ ] O participante pode realizar o seu check-in no evento.

### Regras de Negócio

- [ ] Um participante só pode se inscrever uma única vez em cada evento.
- [ ] Inscrições só são permitidas em eventos com vagas disponíveis.
- [ ] O check-in no evento é único para cada participante.


## Minha Experiência com Esse Projeto

Participar deste projeto durante um evento da Rocketseat foi uma jornada intensa de aprendizado em apenas 4 dias, da qual destacou-se pelos seguintes tópicos:

- **Arquitetura de Projetos**: Observar a abordagem de um desenvolvedor Python Sênior na arquitetura de uma aplicação ampliou significativamente minha visão sobre desenvolvimento.

- **Organização de Arquivos**: Aprendi a importância da organização lógica de arquivos e pastas para a clareza do projeto.

- **Qualidade > Quantidade**: A experiência reforçou a necessidade de priorizar a qualidade em todos os aspectos do código, desde o seu escopo até a nomenclatura de variáveis, classes e funções.

- **Tratativa de Erros**: A criação de um diretório dedicado ao tratamento de erros me impactou positivamente, pois destacou a importância de uma boa experiência de usuário, antecipando e gerenciando possíveis problemas.

