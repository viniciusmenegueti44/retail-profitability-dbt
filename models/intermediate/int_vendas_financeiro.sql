with vendas as (
    select * from {{ ref('stg_vendas') }}
),
produtos as (
    select * from {{ ref('stg_produtos') }}
),
custos as (
    select * from {{ ref('stg_custos') }}
),

calculado as (
    select
        v.id_venda,
        v.data_venda,
        p.nome_produto,
        p.categoria,
        
        -- Métricas de Receita
        (v.quantidade * p.preco_unitario) as receita_bruta,
        
        -- Cálculo de Custos Complexos (Custo Prod + Frete + Imposto sobre Venda)
        (v.quantidade * p.custo_unitario) as custo_mercadoria,
        (v.quantidade * c.custo_frete) as custo_logistico,
        ((v.quantidade * p.preco_unitario) * c.aliquota_imposto) as custo_imposto,
        
        -- Margem de Contribuição (Lucro Líquido Operacional)
        (v.quantidade * p.preco_unitario) - 
        (
            (v.quantidade * p.custo_unitario) + 
            (v.quantidade * c.custo_frete) + 
            ((v.quantidade * p.preco_unitario) * c.aliquota_imposto)
        ) as margem_contribuicao

    from vendas v
    left join produtos p on v.id_produto = p.id_produto
    left join custos c on v.uf = c.uf
    
    where v.status_pedido = 'Aprovado' -- Ignora devoluções no faturamento
)

select * from calculado