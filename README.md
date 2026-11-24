# Toolshop Automation PV

![CI](https://github.com/PhanHoang12/toolshop-automation-pv/actions/workflows/ci.yml/badge.svg)

Repo nhóm cho đồ án Automation Testing với Python, Playwright và pytest.

## Kết quả CI

![CI xanh](docs/screenshots/ci-green.png)

## Trace Viewer

![Trace Viewer](docs/screenshots/trace-viewer.png)

## Sprint 2 - nửa sau (25/11)

- **BDD (`tests/bdd/`)**: Luồng nghiệp vụ giỏ hàng (`tests/bdd/features/cart.feature` và `tests/bdd/test_cart_bdd.py`) dùng `Scenario Outline` + `Examples`, step gọi lại page object (`HomePage`, `ProductPage`, `CartPage`).
- **CI (`.github/workflows/ci.yml`)**: 3 trigger (`push` vào `main`, `pull_request`, `workflow_dispatch`), ma trận 3 trình duyệt (`chromium`, `firefox`, `webkit`), `fail-fast: false`, dựng Toolshop bằng Docker (`toolshop/`), chạy toàn bộ test với `-n 2 --reruns 1`, lưu HTML report và trace khi lỗi vào artifact riêng `report-${{ matrix.browser }}`.

```powershell
pytest tests/bdd -v -p no:cacheprovider
```

## Sprint 1

Bốn smoke test dùng Page Object Model trong `tests/ui/test_smoke.py`:

1. Tìm `pliers`: có kết quả, mọi tên sản phẩm chứa từ khóa.
2. Thêm 3 `Claw Hammer`: toast thành công và badge giỏ hàng bằng 3.
3. Đăng nhập bằng email không tồn tại: hiện lỗi, giữ URL đăng nhập.
4. Gửi form Contact trống: báo thiếu Subject và Message.

## Sprint 2 - nửa đầu (18/11)

Bộ test có **24 trường hợp**: 10 API, 12 UI nghiệp vụ phủ sáu nhóm chức năng
và 2 route. Ngày 17/11/2026 chạy Chromium đạt **24 passed in 67.84s**.
Bốn smoke test Sprint 1 vẫn xanh.

```powershell
pytest --collect-only -q -p no:cacheprovider
pytest -m api -v -p no:cacheprovider
pytest -v -p no:cacheprovider
```

Test UI dùng marker `ui`, API dùng `api`, test mạng có thêm `route`.
Muốn xem 12 trường hợp UI nghiệp vụ:

```powershell
pytest -m 'ui and not route' --headed --slowmo 700 -v -p no:cacheprovider
```

Xem bảng đối chiếu yêu cầu và hướng dẫn PR #2 tại [docs/sprint-2.md](docs/sprint-2.md).
Cần một thành viên khác review và Approve trước khi merge PR #2.

## Cài đặt trên Windows PowerShell

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install chromium
Copy-Item .env.example .env
python -m pytest -m smoke
```

URL lấy từ `.env`. File này và `.venv/` không được commit.

## Xem trình duyệt chạy lần lượt

```powershell
python -m pytest -m smoke --headed --slowmo 700 -v
```

## Cấu trúc

- `pages/`: locator và thao tác của từng trang.
- `tests/ui/test_smoke.py`: kịch bản, assertion và docstring ba ý.
- `conftest.py`: fixture, cấu hình URL và thuộc tính `data-test`.
- `pytest.ini`: marker và cấu hình pytest.

## Quy tắc làm việc

Mọi thay đổi vào `main` đi qua Pull Request, có ít nhất một thành viên khác
Approve trước khi merge. Các thành viên làm việc trên nhánh riêng.

Locator nằm trong `pages/`; assertion nghiệp vụ nằm trong test.
Chờ điều kiện hoặc phản hồi mạng thay vì chờ cố định.
Test đăng nhập sai không sử dụng tài khoản mẫu của lớp.

Hướng dẫn đưa Sprint 1 lên GitHub và nghiệm thu: `docs/sprint-1.md`.
