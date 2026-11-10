# Toolshop Automation PV

Repo nhóm cho đồ án Automation Testing với Python, Playwright và pytest.

## Sprint 1

Bốn smoke test dùng Page Object Model trong `tests/ui/test_smoke.py`:

1. Tìm `pliers`: có kết quả, mọi tên sản phẩm chứa từ khóa.
2. Thêm 3 `Claw Hammer`: toast thành công và badge giỏ hàng bằng 3.
3. Đăng nhập bằng email không tồn tại: hiện lỗi, giữ URL đăng nhập.
4. Gửi form Contact trống: báo thiếu Subject và Message.

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
