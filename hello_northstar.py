weekly_sales = {
    "North":   14200,
    "South":    9100,
    "East":    16700,
    "West":    10800,
    "Central": 12400,
}

def total_sales(sales_dict):
    return sum(sales_dict.values())

def average_sales(sales_dict):
    total = total_sales(sales_dict)
    num_region = len(sales_dict)
    return total / num_region
    
def minimum_sales(sales_dict):
    return min(sales_dict.values())

def maximum_sales(sales_dict):
    return max(sales_dict.values())

for region, sales in weekly_sales.items():
    if sales > average_sales(weekly_sales):
        print(f"{region} : {sales} : Above Average")

    elif sales < average_sales(weekly_sales):
        print(f"{region} : {sales} : Below Average")

print("summary")
print("Total:" , total_sales(weekly_sales))
print("Average:" , average_sales(weekly_sales))
print("Min:" , minimum_sales(weekly_sales))
print("Max:" , maximum_sales(weekly_sales))

        
with open("region_summary_report.txt" , "w") as f:

  for region, sales in weekly_sales.items():
    if sales > average_sales(weekly_sales):
       f.write(f"{region} : {sales} : Above Average\n")

    elif sales < average_sales(weekly_sales):
        f.write(f"{region} : {sales} : Below Average\n")

  f.write("\n")
  f.write(f"Total: { total_sales(weekly_sales)}\n")
  f.write(f"Average: {average_sales(weekly_sales) }\n")
  f.write(f"Min: {minimum_sales(weekly_sales) }\n")
  f.write(f"Max: {maximum_sales(weekly_sales) }\n")

