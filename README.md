# 🛒 Retail Profitability Engine

**Projeto de Engenharia de Analytics (End-to-End)** focado em calcular a rentabilidade real (Unit Economics) de um e-commerce, saindo da visão de Faturamento Bruto para Margem de Contribuição Líquida.

### 🛠️ Tech Stack
*   **Ingestão:** Python (Pandas/Faker) para simulação de transações, custos logísticos e impostos por estado.
*   **Data Warehouse:** Microsoft SQL Server.
*   **Transformação (ELT):** **dbt (data build tool)** para limpeza, modelagem dimensional e testes de qualidade.
*   **Visualização:** Power BI.

### 🧠 Regras de Negócio Aplicadas (dbt)
O projeto não utiliza apenas dados prontos. A camada `intermediate` do dbt aplica as seguintes regras:
*   Cálculo de Impostos (ICMS variável por UF).
*   Custo de Frete Médio por região.
*   **Margem de Contribuição** = Receita - (CMV + Impostos + Frete).
*   Classificação **Curva ABC** automática (Gold/Silver/Bronze) via Window Functions SQL.

### 📊 Resultado
Dashboard de rentabilidade que permite identificar produtos que geram receita, mas destroem valor (margem negativa).
