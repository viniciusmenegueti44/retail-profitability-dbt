with source as (
    select * from {{ source('retail', 'raw_vendas') }}
),

renamed as (
    select
        ID_Venda as id_venda,
        CAST(Data_Venda AS DATE) as data_venda, -- Remove horas
        SKU as id_produto,
        Qtd as quantidade,
        UF_Entrega as uf,
        Status as status_pedido
    from source
)

select * from renamed