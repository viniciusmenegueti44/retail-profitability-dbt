with source as (
    select * from {{ source('retail', 'raw_produtos') }}
),

renamed as (
    select
        SKU as id_produto,
        Nome_Produto as nome_produto,
        Categoria as categoria,
        Custo_Produto as custo_unitario,
        Preco_Venda as preco_unitario,
        Estoque_Atual as estoque_atual
    from source
)

select * from renamed