# Sprint 1: đưa bài nhóm lên GitHub

## Đã chuẩn bị trên máy

- Khung kiểm thử và toàn bộ page object đã hoàn thành buổi 1.
- `.venv` riêng, thư viện theo `requirements.txt`, Chromium, `.env` từ mẫu.
- Đúng 4 smoke test dùng POM, mỗi test có marker và docstring ba ý.
- Chạy thực tế trên Chromium ngày 10/11/2026: **4 passed in 24.56s**.
- Kiểm tra tĩnh đạt: không locator trong test, không assertion trong page object,
  không chờ cố định, không bỏ qua test.
- Quy tắc GitHub `protect-main` đã kiểm tra: Active, nhánh main, yêu cầu 1 approval.

## 1. Khởi tạo main của repo đang trống

Repo GitHub ban đầu chưa có commit hoặc nhánh main. Trên máy đã chuẩn bị
nhánh `main` chỉ chứa commit README khởi tạo, và nhánh `feature/sprint1`
chứa commit khung kiểm thử cùng 4 test để đưa qua PR.

Trong terminal của repo nhóm:

```powershell
git push -u origin main
```

Nếu GitHub chặn commit khởi tạo do quy tắc bắt buộc PR: vào Settings →
Rulesets → protect-main, tạm đặt Enforcement status thành Disabled và Save;
chạy lại lệnh push main; sau đó bật lại Active và Save ngay, trước khi
đưa commit bài làm lên PR. Chỉ README khởi tạo được đẩy ở bước này.

## 2. Đẩy nhánh bài làm và mở PR #1

```powershell
git push -u origin feature/sprint1
```

Trên GitHub chọn Compare & pull request:

- Base: `main`, Compare: `feature/sprint1`.
- Tiêu đề: `Sprint 1: framework and smoke tests`.
- Mô tả: chép kết quả `pytest -m smoke` và ghi `4 passed`.
- Tạo Pull Request. Thêm một thành viên khác làm Reviewer sau khi họ đã nhận lời mời.

## 3. Thêm thành viên và review thật

1. Settings → Collaborators → Add people, nhập tài khoản GitHub từng thành viên.
2. Các bạn nhận lời mời để có quyền truy cập repo.
3. Reviewer mở PR → Files changed, kiểm tra locator, assertion, cách chờ,
   marker và docstring; Review changes → Approve → Submit review.
4. Sau khi có Approved, người mở PR chọn Merge pull request.

Người tạo PR không thể tự Approve PR của mình. Không đánh dấu hoàn thành
bước review trước khi một thành viên khác thực sự review và gửi approval.

## 4. Chuẩn bị nghiệm thu 11/11

Sau khi merge, lấy bản main mới về máy:

```powershell
git switch main
git pull --ff-only origin main
.venv\Scripts\Activate.ps1
python -m pytest -m smoke
```

Chiếu ba bằng chứng:

- Quy tắc protect-main Active, áp dụng main và yêu cầu 1 approval.
- PR #1 ở trạng thái Merged, có Approved của thành viên khác.
- Terminal chạy smoke trên main: 4 passed.

Cả nhóm phải có tên trong Collaborators. Kiểm tra `.env` không xuất hiện
trong Files changed của PR; `.venv`, cache và kết quả chạy cũng không được commit.

## Lệnh kiểm tra quy tắc trên PowerShell

Ba lệnh phải không in kết quả:

```powershell
Select-String -Path tests\ui\*.py -Pattern 'get_by_|locator\('
Select-String -Path pages\*.py -Pattern 'expect\(|assert '
Select-String -Path tests\ui\*.py,pages\*.py -Pattern 'sleep|wait_for_timeout'
```
