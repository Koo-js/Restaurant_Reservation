def __init__(self, branch_name):
        # 레스토랑 지점의 이름을 초기화하고, 예약 리스트를 관리합니다.
        self.branch_name = branch_name
        self.reservations = []