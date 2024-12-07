SELECT 
    municipality,
    SUM(county_tax_levy + municipality_tax_levy + school_district_tax_levy) AS total_tax_levy
FROM 
    `cis4400-hw-443410.cleaned_data.property_tax_rates`
GROUP BY 
    municipality
ORDER BY 
    total_tax_levy DESC
LIMIT 10;
