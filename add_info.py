restaurant1 = ReservationSystem("강남점")
restaurant2 = ReservationSystem("홍대점")

restaurant1.add_reservation("홍길동", "2024-05-20", 4)
restaurant2.add_reservation("김철수", "2024-05-21", 2)

restaurant1.list_reservations()
restaurant2.list_reservations()

total_reservations = ReservationSystem.sum_reservations([restaurant1, restaurant2])
print(f"전체 레스토랑 예약 수: {total_reservations}")