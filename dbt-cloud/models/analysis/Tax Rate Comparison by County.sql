SELECT 
    county,
    AVG(county_tax_rate_outside_village_per_1000_assessed_value) AS avg_tax_rate_outside_village,
    AVG(county_tax_rate_inside_village_per_1000_assessed_value) AS avg_tax_rate_inside_village
FROM 
    `cis4400-hw-443410.cleaned_data.property_tax_rates`
GROUP BY 
    county
ORDER BY 
    avg_tax_rate_outside_village DESC;
