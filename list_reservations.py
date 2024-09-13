def list_reservations(self):
        # 현재 지점의 모든 예약 상태를 출력합니다.
        print(f"{self.branch_name} 예약 목록:")
        if not self.reservations:
            print("예약이 없습니다.")
        else:
            for reservation in self.reservations:
                print(f"- {reservation['customer_name']}, {reservation['reservation_date']}, {reservation['party_size']}명")