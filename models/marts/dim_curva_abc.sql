with performance as (
    select 
        nome_produto,
        categoria,
        sum(receita_bruta) as receita_total,
        sum(margem_contribuicao) as lucro_total
    from {{ ref('int_vendas_financeiro') }}
    group by nome_produto, categoria
),

ranking as (
    select 
        *,
        -- Divide os produtos em 3 grupos baseados no Lucro (NTILE é função de janela)
        NTILE(3) OVER (ORDER BY lucro_total DESC) as grupo_ranking
    from performance
)

select 
    nome_produto,
    categoria,
    receita_total,
    lucro_total,
    case 
        when grupo_ranking = 1 then 'A - Ouro (Alta Margem)'
        when grupo_ranking = 2 then 'B - Prata (Média Margem)'
        else 'C - Bronze (Baixa Margem)'
    end as classificacao_abc
from ranking