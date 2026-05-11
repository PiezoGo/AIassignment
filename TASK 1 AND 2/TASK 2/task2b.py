from constraint import Problem

problem = Problem()

subcounties = [
    'Westlands', 'Dagoretti North', 'Dagoretti South', 'Langata',
    'Kibra', 'Roysambu', 'Kasarani', 'Ruaraka', 'Embakasi South',
    'Embakasi North', 'Embakasi Central', 'Embakasi East', 'Embakasi West',
    'Makadara', 'Kamukunji', 'Starehe', 'Mathare'
]

adjacencies = [
    ('Westlands', 'Dagoretti North'), ('Westlands', 'Roysambu'),
    ('Westlands', 'Starehe'), ('Westlands', 'Kamukunji'),
    ('Dagoretti North', 'Dagoretti South'), ('Dagoretti North', 'Kibra'),
    ('Dagoretti South', 'Kibra'), ('Dagoretti South', 'Langata'),
    ('Langata', 'Kibra'), ('Langata', 'Embakasi West'),
    ('Kibra', 'Makadara'), ('Kibra', 'Kamukunji'),
    ('Roysambu', 'Kasarani'), ('Roysambu', 'Starehe'),
    ('Kasarani', 'Ruaraka'), ('Kasarani', 'Embakasi North'),
    ('Ruaraka', 'Embakasi North'), ('Ruaraka', 'Mathare'),
    ('Mathare', 'Starehe'), ('Mathare', 'Kamukunji'),
    ('Starehe', 'Kamukunji'), ('Kamukunji', 'Makadara'),
    ('Makadara', 'Embakasi South'), ('Makadara', 'Embakasi Central'),
    ('Embakasi West', 'Embakasi Central'), ('Embakasi West', 'Embakasi South'),
    ('Embakasi Central', 'Embakasi East'), ('Embakasi Central', 'Embakasi South'),
    ('Embakasi Central', 'Embakasi North'), ('Embakasi East', 'Embakasi North'),
]

# Try increasing number of colours until a solution is found
for k in range(2, 6):
    p = Problem()
    colors = list(range(k))
    for sc in subcounties:
        p.addVariable(sc, colors)
    for r1, r2 in adjacencies:
        p.addConstraint(lambda a, b: a != b, (r1, r2))
    solution = p.getSolution()
    if solution:
        color_names = ['Red', 'Green', 'Blue', 'Yellow']
        print(f"Minimum colours needed: {k}\n")
        for region, c in solution.items():
            print(f"  {region:25s} -> {color_names[c]}")
        break