{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ff7fc153-56d9-4cd8-8f37-585351db39fa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Gerando dados para RetailDB...\n",
      "✅ Tabela 'raw_produtos' criada.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\ProgramData\\anaconda3\\Lib\\site-packages\\pandas\\io\\sql.py:1576: SAWarning: Unrecognized server version info '17.0.1000.7'.  Some SQL Server features may not function properly.\n",
      "  con = self.exit_stack.enter_context(con.connect())\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Tabela 'raw_custos_logistica' criada.\n",
      "✅ Tabela 'raw_vendas' criada.\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import random\n",
    "from faker import Faker\n",
    "from datetime import datetime, timedelta\n",
    "from sqlalchemy import create_engine\n",
    "import urllib\n",
    "\n",
    "# --- 1. CONEXÃO SQL SERVER ---\n",
    "server = 'Vinicius'  # Ajuste se seu servidor tiver outro nome\n",
    "database = 'RetailDB' \n",
    "driver = 'ODBC Driver 17 for SQL Server'\n",
    "params = urllib.parse.quote_plus(f\"DRIVER={{{driver}}};SERVER={server};DATABASE={database};Trusted_Connection=yes;\")\n",
    "engine = create_engine(f\"mssql+pyodbc:///?odbc_connect={params}\")\n",
    "\n",
    "fake = Faker('pt_BR')\n",
    "print(\"Gerando dados para RetailDB...\")\n",
    "\n",
    "# --- 2. TABELA DE PRODUTOS (SKUs) ---\n",
    "categorias = ['Eletrônicos', 'Moda', 'Casa', 'Beleza']\n",
    "produtos = []\n",
    "for i in range(1, 51): # 50 Produtos\n",
    "    cat = random.choice(categorias)\n",
    "    custo_base = round(random.uniform(20, 500), 2)\n",
    "    markup = 1.2 if cat == 'Eletrônicos' else 2.5 \n",
    "    preco_venda = round(custo_base * markup, 2)\n",
    "    \n",
    "    produtos.append({\n",
    "        'SKU': i,\n",
    "        'Nome_Produto': f'{cat} Item {i}',\n",
    "        'Categoria': cat,\n",
    "        'Custo_Produto': custo_base,\n",
    "        'Preco_Venda': preco_venda,\n",
    "        'Estoque_Atual': random.randint(0, 500)\n",
    "    })\n",
    "df_produtos = pd.DataFrame(produtos)\n",
    "df_produtos.to_sql('raw_produtos', engine, if_exists='replace', index=False)\n",
    "print(\"✅ Tabela 'raw_produtos' criada.\")\n",
    "\n",
    "# --- 3. TABELA DE CUSTOS LOGÍSTICOS ---\n",
    "estados = ['SP', 'RJ', 'MG', 'RS', 'PE']\n",
    "custos_log = []\n",
    "for uf in estados:\n",
    "    custos_log.append({\n",
    "        'UF': uf,\n",
    "        'Custo_Frete_Medio': round(random.uniform(15, 40), 2),\n",
    "        'Imposto_ICMS': 0.18 if uf in ['SP', 'MG'] else 0.12\n",
    "    })\n",
    "df_custos = pd.DataFrame(custos_log)\n",
    "df_custos.to_sql('raw_custos_logistica', engine, if_exists='replace', index=False)\n",
    "print(\"✅ Tabela 'raw_custos_logistica' criada.\")\n",
    "\n",
    "# --- 4. TABELA DE VENDAS (FATO) ---\n",
    "vendas = []\n",
    "for i in range(1, 5001): # 5 mil vendas\n",
    "    sku = random.randint(1, 50)\n",
    "    qtd = random.randint(1, 5)\n",
    "    uf = random.choice(estados)\n",
    "    data_venda = fake.date_between(start_date='-1y', end_date='today')\n",
    "    status = random.choices(['Ap"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "82ed5e10-7891-4515-856b-034496122d2e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
