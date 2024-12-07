SELECT 
    county,
    SUM(county_tax_levy) AS total_county_tax_levy
FROM 
    `cis4400-hw-443410.cleaned_data.property_tax_rates`
GROUP BY 
    county
ORDER BY 
    total_county_tax_levy DESC;
