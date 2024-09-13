def add_reservation(self, customer_name, reservation_date, party_size):
        # 새로운 예약을 추가합니다.
        reservation = {
            "customer_name": customer_name,
            "reservation_date": reservation_date,
            "party_size": party_size
        }
        self.reservations.append(reservation)
        print(f"{customer_name}님의 예약이 추가되었습니다.")