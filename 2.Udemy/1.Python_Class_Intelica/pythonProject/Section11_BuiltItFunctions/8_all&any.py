is_connected: bool = False
has_electricity: bool = True
has_paid: bool = True

requirements: list[bool] = [is_connected, has_electricity, has_paid]

has_internet: bool = any(requirements)

any()
all()

print("Internet:", has_internet)
