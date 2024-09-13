@classmethod
def sum_reservations(cls, branches):
    # 모든 지점의 예약 수를 합산합니다.
    total_reservations = sum(len(branch.reservations) for branch in branches)
    return total_reservations