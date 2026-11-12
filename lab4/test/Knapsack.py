# bai toan cai tui (knapsack problem) - quy hoach dong

# Sức chứa tối đa của túi là 4 ô
MAX_CELLS = 4

# Danh sách đồ vật:
# price = giá trị của món đồ
# cells = số ô mà món đồ chiếm
items = {
    'a': {'price': 700, 'cells': 3},
    'b': {'price': 300, 'cells': 1},
    'c': {'price': 500, 'cells': 2},
    'd': {'price': 550, 'cells': 2},
}


def gen_table_memo(items, max_cells=MAX_CELLS):

    # Tạo bảng 2 chiều chứa toàn số 0
    # Số hàng = số món đồ
    # Số cột = sức chứa tối đa của túi
    table = [[0 for _ in range(max_cells)] for _ in range(len(items))]

    # Duyệt từng món đồ
    # row = vị trí hàng trong bảng
    # item = thông tin món đồ hiện tại
    for row, item in enumerate(items.values()):

        # Lấy giá trị và thể tích của món đồ
        price = item['price']
        cells = item['cells']

        # Duyệt sức chứa của túi từ 1 đến max_cells
        # col = chỉ số cột, bắt đầu từ 0
        # current_limit = sức chứa đang xét (1, 2, 3, 4)
        for col, current_limit in enumerate(range(1, max_cells+1)):

            # Trường hợp 1: Đang xét món đồ đầu tiên
            if row == 0:

                # Không vừa túi thì ghi 0, vừa túi thì ghi giá món đồ
                table[row][col] = 0 if cells > current_limit else price

                # Chuyển sang sức chứa tiếp theo
                continue

            # Giá trị tốt nhất nếu KHÔNG lấy món đồ hiện tại
            # Lấy kết quả từ hàng trước, cùng cột
            prev_price = table[row-1][col]

            # Trường hợp 2: Món đồ lớn hơn sức chứa hiện tại
            if cells > current_limit:

                # Không thể lấy món này, giữ kết quả hàng trước
                table[row][col] = prev_price

            # Trường hợp 3: Món đồ vừa đúng sức chứa
            elif cells == current_limit:

                # So sánh không lấy món và chỉ lấy món hiện tại
                table[row][col] = max(prev_price, price)

            # Trường hợp 4: Món đồ nhỏ hơn sức chứa
            else:

                # Tìm giá trị tốt nhất với phần sức chứa còn lại
                # Dùng row-1 để không chọn lại món hiện tại
                # col-cells là cột tương ứng với chỗ còn lại
                price_rest = table[row-1][col-cells]

                # So sánh:
                # 1. Không lấy món hiện tại: prev_price
                # 2. Lấy món hiện tại: price_rest + price
                # Chọn giá trị lớn nhất
                table[row][col] = max(prev_price, price_rest+price)

    # Trả về bảng kết quả
    return table


# Chạy chương trình khi thực thi file trực tiếp
if __name__ == '__main__':

    # Gọi hàm để tạo bảng quy hoạch động
    res = gen_table_memo(items)

    # In bảng kết quả
    print(res)
