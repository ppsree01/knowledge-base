from cloud_storage import CloudStorage

storage = CloudStorage()

storage.add_file("Get_Agoda", 23)
storage.add_file("Have_ORS", 2)
storage.add_file("Clear_Debit", 77)
storage.add_file("Grow", 3)
storage.add_file("Gallow", 4)
storage.add_file("Galloww", 5)
storage.add_file("Girroww", 5)
storage.copy_file("Grow", "Groww")

storage.display()

print(storage.get_file_size("Have_ORS"))

result = storage.find_by_prefix_and_suffix("G", "w")
for data in result:
    print(data)
