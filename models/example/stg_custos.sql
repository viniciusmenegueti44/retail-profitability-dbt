with source as (
    select * from {{ source('retail', 'raw_custos_logistica') }}
),

renamed as (
    select
        UF as uf,
        Custo_Frete_Medio as custo_frete,
        Imposto_ICMS as aliquota_imposto
    from source
)

select * from renamed