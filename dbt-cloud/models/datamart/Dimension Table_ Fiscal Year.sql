SELECT 
    fiscal_year_ending AS fiscal_year,
    roll_year
FROM 
    `cis4400-hw-443410.cleaned_data.property_tax_rates`
GROUP BY 
    fiscal_year_ending, roll_year;
