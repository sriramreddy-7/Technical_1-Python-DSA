Families={
    'Charley':
        {'sam':{'boxy','rosy'},
         'Nila':{'Pespsi'}},
    'Devi':
        {
            'Tommy':{'Tony'},
            'Timmy':{'Hamster'},
            'Tammy':{'Hamster'},
        },
    'Carlos':
        {'Diego':'cat','ferret':'Fox'}
        
}

for Parent,Children in Families.items():
    print(f"{Parent} has {len(Children)} Kid(s):")
    print(f" {',and'.join([str(Child) for Child in[*Children]])}")