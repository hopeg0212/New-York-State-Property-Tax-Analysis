SELECT 
    MD5(municipality) AS municipality_id,
    municipality,
    county
FROM 
    `cis4400-hw-443410.cleaned_data.property_tax_rates`
GROUP BY 
    municipality, county;
