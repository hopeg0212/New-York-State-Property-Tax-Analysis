SELECT 
    municipality,
    AVG(municipal_tax_rate_outside_village_per_1000_assessed_value) AS avg_municipal_tax_rate_outside_village
FROM 
    `cis4400-hw-443410.cleaned_data.property_tax_rates`
GROUP BY 
    municipality
ORDER BY 
    avg_municipal_tax_rate_outside_village DESC;
