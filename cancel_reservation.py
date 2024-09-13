def cancel_reservation(self, customer_name, reservation_date):
        # 지정된 예약을 취소하고 리스트에서 제거합니다.
        for reservation in self.reservations:
            if reservation["customer_name"] == customer_name and reservation["reservation_date"] == reservation_date:
                self.reservations.remove(reservation)
                print(f"{customer_name}님의 예약이 취소되었습니다.")
                return
        print(f"{customer_name}님의 예약을 찾을 수 없습니다.")