from cloud_storage import CloudStorage

storage = CloudStorage()

storage.add_file("Get_Agoda", 23)
storage.add_file("Have_ORS", 2)
storage.add_file("Clear_Debit", 77)
storage.add_file("Grow", 3)

storage.copy_file("Grow", "Groww")

storage.display()

print(storage.get_file_size("Have_ORS"))
