# GymBask Lab

Sistema de monitoramento integrado de academia, basquete, recuperação e performance física.

---

## Objetivo do projeto

Este projeto NÃO foi criado inicialmente para virar startup.

Objetivos reais:

- Aprender engenharia de software real
- Aprender arquitetura de sistemas
- Aprender backend
- Aprender frontend
- Aprender banco de dados
- Aprender modelagem de dados
- Aprender matemática aplicada ao esporte
- Aprender física aplicada ao esporte
- Futuramente aprender machine learning aplicado ao sistema

---

## O que o sistema faz

O sistema monitora:

- Treinos de academia
- Treinos de basquete
- Recuperação
- Fadiga muscular
- Fadiga cardiovascular
- Performance física

Objetivo:

Entender quanto o atleta treinou, quanto de fadiga acumulou e como isso impacta performance futura.

---

# Módulo academia

Usuário cria:

- treino A
- treino B
- treino C

Cada exercício possui:

- nome
- séries
- repetições
- carga
- músculo principal
- músculos secundários

Exemplo de cálculo:

Volume = carga × repetições × séries

Exemplo:

Supino:
100kg × 8 × 4 = 3200

---

# Módulo basquete

Usuário registra:

- duração
- tipo
- intensidade

Tipos:

- arremesso
- drible
- treino técnico
- condicionamento
- jogo

Exemplo:

Carga = duração × intensidade

90 min × RPE 8 = 720

---

# Módulo recuperação

Futuro:

- sono
- hidratação
- alimentação
- descanso

Sistema reduzirá fadiga automaticamente.

---

# Output final

- Score muscular
- Score cardiovascular
- Histórico de treinos
- Histórico de basquete
- Estado físico atual

---

# Fora da V1

- Machine learning
- Smartwatch
- Microservices
- Social features
- Mobile nativo
- Métricas avançadas

---

# Stack

## Frontend

- Next.js

## Backend

- Python
- FastAPI

## Banco

- PostgreSQL
- Neon

## ORM

- SQLAlchemy

## Testes

- Pytest
- Jest

## Deploy

- Render
- Vercel

---

# Arquitetura inicial

Monólito modular

Estrutura principal:

- backend/
- frontend/
- docs/
- scripts/

---

# Ambiente de desenvolvimento

Como você possui limitações locais:

- GitHub.dev → edição rápida
- GitHub Codespaces → desenvolvimento principal
- Neon → banco cloud
- Render → backend deploy
- Vercel → frontend deploy

---

# Estrutura atual

```bash
GYMBASK-LAB---1/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── calculations/
│   │   ├── core/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── schemas/
│   │   ├── services/
│   │
│   ├── tests/
│   ├── main.py
│   ├── README.md
│   ├── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── services/
│   │   ├── styles/
│   │   ├── types/
│   │   ├── utils/
│
├── docs/
│   ├── architecture/
│   ├── database/
│   ├── business-rules/
│   ├── api/
│   ├── roadmap/
│   ├── setup-environment.md
│
├── scripts/
│   ├── backups/
│   ├── seeds/
│   ├── sql/
│
├── commands.md
├── .gitignore
├── .env.example
└── README.md
```

---

# Roadmap macro

Fase 1 → Fundação  
Fase 2 → Arquitetura  
Fase 3 → Modelagem de domínio  
Fase 4 → Modelagem muscular  
Fase 5 → Banco de exercícios  
Fase 6 → Motor academia  
Fase 7 → Motor basquete  
Fase 8 → Motor recuperação  
Fase 9 → Motor performance  
Fase 10 → Backend  
Fase 11 → Banco  
Fase 12 → Frontend  
Fase 13 → Deploy  

---

# Status atual

Concluído até agora:

- escopo validado
- git configurado
- repositório remoto criado
- estrutura profissional criada
- workflow cloud validado
- documentação operacional criada

---

# Próximo passo

Passo 10 → Criar roadmap técnico oficial