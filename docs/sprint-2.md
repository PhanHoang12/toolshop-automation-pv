# Sprint 2 - nửa đầu, nghiệm thu 18/11

Nhánh bài làm: `feature/phanhoang-sprint2`, tạo từ main sau PR #1.

## Kết quả kiểm tra

Ngày 17/11/2026, chạy trên Chromium:

```text
python -m pytest -v -p no:cacheprovider --tracing retain-on-failure --screenshot only-on-failure
24 passed in 67.84s
```

Có 24 trường hợp: **10 API + 12 UI nghiệp vụ + 2 route**.
Hai test route cũng có marker ui, nên `pytest -m ui` chạy tổng cộng 14 trường hợp.
Bốn test smoke từ Sprint 1 vẫn được giữ nguyên và đều xanh.

## Đối chiếu sáu yêu cầu

| Yêu cầu | Phần đã chuẩn bị |
|---|---|
| Ít nhất 5 test API | 10 trường hợp trong `tests/api/` |
| Hai phương thức HTTP | GET và POST trong test giỏ hàng và đăng ký |
| Lỗi 4xx | 401, 404 trong products; 422 trong users |
| Cấu trúc JSON | Phân trang, ID, tên, giá của danh sách sản phẩm |
| API có token | Hồ sơ `/users/me` với `auth_headers` của tài khoản fixture |
| Hai test route | Chặn ảnh thật và giả lập danh sách sản phẩm rỗng |
| Hai test parametrize | Tìm kiếm đọc JSON và cặp endpoint/mã lỗi; sắp xếp UI cũng được tham số hóa |
| Hai scope | session cho API/tài khoản/auth_state; function cho logged_in_page và new_cart |
| Đăng nhập một lần | auth_state lưu storage_state; test tài khoản dùng logged_in_page |
| Ít nhất ba marker | smoke, api, ui; thêm route để tách hai bài chặn/giả lập mạng |
| 12 test UI phủ sáu nhóm, ít nhất 8 xanh | Cả 12 trường hợp nghiệp vụ đã xanh; bảng bên dưới |
| PR #2 được người khác review trước khi merge | Chờ thực hiện trên GitHub sau khi đẩy nhánh |

`new_cart` là fixture function đặt trong file `tests/api/test_carts_api.py`.
`logged_in_page` là fixture function trong `conftest.py`, còn `auth_state`
là session: một lần đăng nhập cho mỗi phiên/worker cần dùng nó.

## Phân bố test API

| File | Trường hợp | Số lượng |
|---|---|---:|
| `tests/api/test_products_api.py` | Hợp đồng JSON; bốn từ khóa; 401/404 | 7 |
| `tests/api/test_users_api.py` | Đăng ký rỗng 422; hồ sơ có token | 2 |
| `tests/api/test_carts_api.py` | Tạo giỏ riêng, thêm số lượng 2, đọc lại bằng GET | 1 |

Dữ liệu tìm kiếm ở `data/search_keywords.json` gồm pliers, hammer, saw, wrench.
Không dùng token GitHub cho các test Toolshop này; token Toolshop do fixture tạo.
Không sao chép `.env` cá nhân sang repo nhóm.

## 12 trường hợp UI nghiệp vụ

| Nhóm chức năng | Các trường hợp | Số lượng |
|---|---|---:|
| Danh sách, tìm kiếm | Tìm pliers; từ khóa không có; giá tăng dần; giá giảm dần | 4 |
| Bộ lọc | Lọc danh mục Hammer, kiểm checkbox và mọi tên sản phẩm | 1 |
| Chi tiết sản phẩm | Tên/giá khớp thẻ sản phẩm; thêm 3 Claw Hammer | 2 |
| Giỏ hàng | Số lượng 2, giá dòng và tổng giỏ đúng | 1 |
| Xác thực | Đăng nhập sai; form đăng nhập trống | 2 |
| Liên hệ, tài khoản | Form Contact trống; tài khoản dùng storage state | 2 |

Hai test route nằm riêng ở `tests/ui/test_network.py`:

- Chặn ảnh: sản phẩm vẫn hiển thị và danh sách request bị chặn không rỗng.
- Mock danh sách rỗng: đúng thông báo và zero sản phẩm.

Các locator mới nằm trong HomePage. Bộ lọc tìm qua nhãn Hammer, không dùng ID
cố định. Việc điều hướng chờ DOM sẵn sàng; HomePage còn chờ phản hồi danh sách
sản phẩm, rồi test chờ marker hoặc dữ liệu cần kiểm.

## Chạy trên máy bạn

Trong terminal repo `toolshop-automation-pv`:

```powershell
.venv\Scripts\Activate.ps1
git branch --show-current
pytest --collect-only -q -p no:cacheprovider
pytest -v -p no:cacheprovider
```

Lệnh hiển thị nhánh cần ra `feature/phanhoang-sprint2` trước khi mở PR.
Tùy chọn tắt cache chỉ tránh vấn đề quyền ghi cache cũ, không bỏ qua test.

Chạy theo từng nhóm:

```powershell
pytest -m api -v -p no:cacheprovider
pytest -m route --headed --slowmo 700 -v -p no:cacheprovider
pytest -m 'ui and not route' --headed --slowmo 700 -v -p no:cacheprovider
pytest -m smoke --headed --slowmo 700 -v -p no:cacheprovider
```

Kết quả tương ứng: 10, 2, 12 và 4 passed; các marker có thể giao nhau.

`conftest.py` cấp thư mục `.pytest-runs/run-<uuid>/` mới mỗi phiên để tránh
lỗi quyền Windows khi xóa thư mục tạm của một tài khoản khác. Thư mục gốc
kế thừa quyền của dự án; trạng thái đăng nhập trong thư mục con không được commit.

## Đẩy nhánh và tạo PR #2

Code được lưu commit local trên nhánh Sprint 2. Đẩy nhánh:

```powershell
git push -u origin feature/phanhoang-sprint2
```

Mở repo GitHub, Compare & pull request:

- Base: `main`, Compare: `feature/phanhoang-sprint2`.
- Title: `Sprint 2: API, route and UI coverage`.
- Description có thể dùng nội dung sau:

```text
Add 10 API cases, 12 business UI cases across six feature groups, and 2 route cases.
Reuse saved login state, read search data from JSON, and use parameterized tests.
Keep the four Sprint 1 smoke tests and use separate temporary storage for each run.
Validation: 24 passed in 67.84s on Chromium; POM and docstring checks passed.
```

Chọn một thành viên khác trong Reviewers. Bạn đó đọc Files changed,
kiểm tra code rồi gửi Review changes → Approve → Submit review.
Chỉ merge sau khi có Approved; giữ protect-main Active và yêu cầu 1 approval.

Không tự đánh dấu PR đã review hoặc đã merge khi bước này chưa thực sự xảy ra.

## Nghiệm thu

Sau khi PR #2 được merge:

```powershell
git switch main
git pull --ff-only origin main
pytest --collect-only -q -p no:cacheprovider
pytest -m api -v -p no:cacheprovider
pytest -v -p no:cacheprovider
```

Chiếu danh sách đủ test, kết quả API xanh và PR #2 đã merge có Approved.
Các thành viên còn lại cần có tên trong Collaborators.

Phần BDD, CI ba trình duyệt, artifact và các tình huống thanh trượt/tải tệp/tab mới
được chuẩn bị ở nửa sau Sprint 2 theo lịch giảng viên, hạn kết thúc Sprint 2 là 25/11.

## Kiểm tra quy tắc

Các lệnh sau phải không có kết quả:

```powershell
Select-String -Path tests\*\*.py -Pattern 'import requests|get_by_|locator\('
Select-String -Path pages\*.py -Pattern 'expect\(|assert '
Select-String -Path tests\*\*.py,pages\*.py -Pattern 'sleep|wait_for_timeout'
```

Không commit `.env`, `.venv`, cache, trạng thái đăng nhập, trace hoặc ảnh kết quả chạy.
